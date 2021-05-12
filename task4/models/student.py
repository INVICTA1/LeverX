import json


class Student():
    def __init__(self, id: int, name: str, room: int, sex: chr, birthday: str):
        self.id = id
        self.name = name
        self.room = room
        self.sex = sex
        self.birthday = birthday

    def __repr__(self):
        return '({id}; {name};{room};{sex};{birthday})'.format(id=self.id,
                                                               name=self.name,
                                                               room=self.room,
                                                               sex=self.sex,
                                                               birthday=self.birthday)


class StudentFileReader():
    @staticmethod
    def read_file(path: str) -> list:
        """Read objects from JSON file"""
        try:
            with open(path, 'r') as file:
                students = json.loads(file.read())
                students = [
                    Student(student['id'], student['name'], student['room'], student['sex'], student['birthday']) for
                    student in students]
            return students
        except FileNotFoundError:
            raise Exception('Json file not found')
        except Exception as MyException:
            raise MyException
