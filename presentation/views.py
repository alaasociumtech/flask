from flask import jsonify, request
from flask.views import MethodView
from infrastructure.student_repo import StudentRepository

student_repo = StudentRepository()


class StudentAPI(MethodView):
    def get(self, student_id=None):
        if student_id is None:
            return jsonify([s.to_dict() for s in student_repo.get_all()])
        student = student_repo.get(student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404
        return jsonify(student.to_dict())

    def post(self):
        data = request.get_json()
        if not all(k in data for k in ('name', 'age', 'grade')):
            return jsonify({'error': 'Missing required fields'}), 400
        student = student_repo.add_student(
            data['name'], data['age'], data['grade'])
        return jsonify(student.to_dict())

    def put(self, student_id):
        if student_repo.get(student_id) is None:
            return jsonify({'error': 'Student not found'}), 404
        data = request.get_json()
        student = student_repo.update_student(
            student_id, data['name'], data['age'], data['grade'])
        return jsonify(student.to_dict())

    def delete(self, student_id):
        if not student_repo.delete(student_id):
            return jsonify({'error': 'Student not found'}), 404
        return jsonify({'message': 'Student deleted'})
