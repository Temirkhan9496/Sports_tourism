import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f"postgresql://{os.getenv('FSTR_DB_LOGIN')}:" \
               f"{os.getenv('FSTR_DB_PASS')}@" \
               f"{os.getenv('FSTR_DB_HOST')}:" \
               f"{os.getenv('FSTR_DB_PORT')}/" \
               f"{os.getenv('FSTR_DB_NAME')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    from . import models
    Base.metadata.create_all(bind=engine)