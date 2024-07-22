from fastapi.testclient import TestClient
from app.main import app, get_db
from app.database import Base, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_submit_data():
    response = client.post("/submitData", json={
        "user_name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+123456789",
        "title": "Test Peak",
        "latitude": 45.0,
        "longitude": 75.0,
        "height": 1500.0
    })
    assert response.status_code == 200
    assert response.json()["status"] == 200
    assert response.json()["message"] == "Отправлено успешно"
    assert "id" in response.json()

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_request():
    response = client.post(
        "/requests/",
        json={
            "name": "test user",
            "phone": "1234567890",
            "email": "test@example.com",
            "direction": "Hiking",
            "level": "Beginner",
            "start_date": "2023-05-01",
            "duration": 7,
            "price": 500.0
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "test user"
    assert response.json()["status"] == "new"

def test_read_request():
    response = client.get("/requests/1")
    assert response.status_code == 200
    assert response.json()["name"] == "test user"