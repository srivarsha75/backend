# backend/tests/test_app.py
import json
import pytest
from app import app    # this works if pytest runs with working directory set to the folder that contains app.py

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    res = client.get("/")
    assert res.status_code == 200
    data = res.get_json()
    assert "message" in data

def test_get_students(client):
    res = client.get("/students")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    # at least two students exist (based on your app)
    assert any(s.get("name") == "Alice" for s in data)

def test_get_single_student(client):
    res = client.get("/students/1")
    assert res.status_code == 200
    data = res.get_json()
    assert data["id"] == 1

def test_add_student(client):
    new_student = {"id": 999, "name": "CI Tester", "age": 30}
    res = client.post("/students", json=new_student)
    assert res.status_code == 201
    assert res.get_json() == new_student
