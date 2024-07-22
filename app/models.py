from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class StatusEnum(enum.Enum):
    new = "new"
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"

class Pereval(Base):
    __tablename__ = "pereval"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    title = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.new)

class StatusEnum(enum.Enum):
    new = "new"
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    direction = Column(String)
    level = Column(String)
    start_date = Column(String)
    duration = Column(Integer)
    price = Column(Float)
    status = Column(Enum(StatusEnum), default=StatusEnum.new)