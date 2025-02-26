from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)


students: dict = {}
student_counter = 1


class StudentAPI(MethodView):
    def get(self, student_id=None):
        if student_id is None:
            return jsonify(list(students.values()))
        student = students.get(student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404
        return jsonify(student)

    def post(self):
        global student_counter
        data = request.get_json()
        if not all(k in data for k in ('name', 'age', 'grade')):
            return jsonify({'error': 'Missing required fields'})
        student_id = student_counter
        students[student_id] = {
            'id': student_id,
            'name': data['name'],
            'age': data['age'],
            'grade': data['grade']
        }
        student_counter += 1
        return jsonify(students[student_id])

    def put(self, student_id):
        if student_id not in students:
            return jsonify({'error': 'Student not found'}), 404
        data = request.get_json()
        students[student_id].update({
            'name': data['name'],
            'age': data['age'],
            'grade': data['grade']
        })
        return jsonify(students[student_id])

    def delete(self, student_id):
        if student_id not in students:
            return jsonify({'error': 'Student not found'}), 404
        del students[student_id]
        return jsonify({'message': 'Student deleted'})


student_view = StudentAPI.as_view('student_api')
app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
app.add_url_rule('/students/<int:student_id>',
                 view_func=student_view, methods=['GET', 'PUT', 'DELETE'])


app.run(debug=True)
