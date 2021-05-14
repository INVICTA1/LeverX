import json
from dataclasses import dataclass


@dataclass()
class Student():
    id: int
    name: str
    room: int


class StudentFileReader():
    @staticmethod
    def read_file(path: str) -> list:
        """Read objects from JSON file"""
        try:
            with open(path, 'r') as file:
                students = json.loads(file.read())
                students = [Student(student['id'], student['name'], student['room']) for student in students]
            return students
        except FileNotFoundError:
            raise Exception('Json file not found')
        except Exception as MyException:
            raise MyException
