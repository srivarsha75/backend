# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Student API Running" in res.data

def test_get_students(client):
    res = client.get("/students")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert any(s["name"] == "Alice" for s in data)

def test_get_single_student(client):
    res = client.get("/students/1")
    assert res.status_code == 200
    student = res.get_json()
    assert student["id"] == 1

def test_add_student(client):
    new_student = {"id": 999, "name": "CI Tester", "age": 30}
    res = client.post("/students", json=new_student)
    assert res.status_code == 201
    assert res.get_json() == new_student
