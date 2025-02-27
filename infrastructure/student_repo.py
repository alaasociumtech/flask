from .base_repo import BaseRepository
from domain.entities.student import Student


class StudentRepository(BaseRepository[Student]):
    def add_student(self, name: str, age: int, grade: str) -> Student:
        student = Student(self.counter, name, age, grade)
        return self.add(student)

    def update_student(self, student_id: int, name: str,
                       age: int, grade: str) -> Student:
        if student_id in self.storage:
            updated_student = Student(student_id, name, age, grade)
            return self.update(student_id, updated_student)
        return None
