from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice", "age": 21},
    {"id": 2, "name": "Bob", "age": 22}
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Student API Running"}), 200


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200


@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404


@app.route("/students", methods=["POST"])
def add_student():
    new_student = request.json
    students.append(new_student)
    return jsonify(new_student), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
