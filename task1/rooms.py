import json


class Room():

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return '({id}; {name})'.format(id=self.id, name=self.name)


class RoomsFileReader():
    @staticmethod
    def read_file(path: str) -> list:
        """Read objects from JSON file"""
        try:
            with open(path, 'r') as file:
                rooms = json.loads(file.read())
                rooms = [Room(room['id'], room['name']) for room in rooms]
            return rooms
        except FileNotFoundError:
            raise Exception('Json file not found')
        except BaseException as e:
            raise Exception("Can't process rooms file")
