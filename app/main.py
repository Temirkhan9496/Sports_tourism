from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from app.models import Base, Pereval

DATABASE_URL = f"postgresql://{os.getenv('FSTR_DB_LOGIN')}:{os.getenv('FSTR_DB_PASS')}@{os.getenv('FSTR_DB_HOST')}:{os.getenv('FSTR_DB_PORT')}/{os.getenv('FSTR_DB_NAME')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class PerevalCreate(BaseModel):
    user_name: str
    email: EmailStr
    phone: str
    title: str
    latitude: float
    longitude: float
    height: float

class PerevalResponse(BaseModel):
    status: int
    message: str
    id: int = None

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/requests/", response_model=schemas.Request)
def create_request(request: schemas.RequestCreate, db: Session = Depends(get_db)):
    db_request = models.Request(**request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

@app.get("/requests/{request_id}", response_model=schemas.Request)
def read_request(request_id: int, db: Session = Depends(get_db)):
    db_request = db.query(models.Request).filter(models.Request.id == request_id).first()
    if db_request is None:
        raise HTTPException(status_code=404, detail="Request not found")
    return db_request

if __name__ == "__main__":
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.post("/submitData", response_model=PerevalResponse)
def submit_data(data: PerevalCreate):
    session = SessionLocal()
    new_pereval = Pereval(
        user_name=data.user_name,
        email=data.email,
        phone=data.phone,
        title=data.title,
        latitude=data.latitude,
        longitude=data.longitude,
        height=data.height
    )
    session.add(new_pereval)
    session.commit()
    session.refresh(new_pereval)

    return PerevalResponse(status=200, message="Отправлено успешно", id=new_pereval.id)
