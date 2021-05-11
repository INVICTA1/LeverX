import json


class Student():
    def __init__(self, id: int, name: str, room: int):
        self.id = id
        self.name = name
        self.room = room

    def __repr__(self):
        return '({id}; {name};{room})'.format(id=self.id,
                                              name=self.name,
                                              room=self.room)


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
