import json
from dataclasses import dataclass


@dataclass()
class Room():
    id: int
    name: str


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
        except Exception as MyException:
            raise MyException
