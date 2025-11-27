from app import app

def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Student API Running"}

def test_get_students():
    client = app.test_client()
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_single_student():
    client = app.test_client()
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.get_json()["id"] == 1

def test_add_student():
    client = app.test_client()
    new_student = {"id": 3, "name": "Charlie", "age": 23}
    response = client.post("/students", json=new_student)
    assert response.status_code == 201
    assert response.get_json() == new_student
