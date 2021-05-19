import json
from dataclasses import dataclass
from mysql.connector import Error


@dataclass()
class Student():
    id: int
    birthday: str
    name: str
    room: int
    sex: chr


class StudentFileReader():
    @staticmethod
    def read_file(path: str) -> list:
        """Read objects from JSON file"""
        try:
            with open(path, 'r') as file:
                students = json.loads(file.read())
                students = [
                    Student(student['id'], student['birthday'], student['name'], student['room'], student['sex']) for
                    student in students]
            return students
        except FileNotFoundError:
            raise Exception('Json file not found')
        except Exception as MyException:
            raise MyException


class StudentDB():
    @staticmethod
    def load_students_to_db(cursor,db: str, students: list):
        try:
            cursor.execute('USE {db}'.format(db=db))
            for student in students:
                params = (student.id, student.birthday, student.name, student.room, student.sex)
                cursor.execute("INSERT INTO students  VALUES(%s,%s,%s,%s,%s)", params)
        except Error as e:
            raise Exception("Can't load students to db", e)
