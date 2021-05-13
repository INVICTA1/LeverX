import json


class Student():
    def __init__(self, id: int, birthday: str, name: str, room: int, sex: chr):
        self.id = id
        self.birthday = birthday
        self.name = name
        self.room = room
        self.sex = sex

    def __repr__(self):
        return "{id},'{birthday}','{name}',{room},'{sex}'".format(id=self.id,
                                                             birthday=self.birthday,
                                                             name=self.name,
                                                             room=self.room,
                                                             sex=self.sex)


class StudentFileReader():
    @staticmethod
    def read_file(path: str) -> list:
        """Read objects from JSON file"""
        try:
            with open(path, 'r') as file:
                students = json.loads(file.read())
                students = [
                    Student(student['id'],student['birthday'], student['name'], student['room'], student['sex'] ) for
                    student in students]
            return students
        except FileNotFoundError:
            raise Exception('Json file not found')
        except Exception as MyException:
            raise MyException
