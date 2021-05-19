import json
from mysql.connector import Error
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


class RoomsDB():
    @staticmethod
    def load_rooms_to_db(cursor, db: str, rooms: list):
        try:
            cursor.execute('USE {db}'.format(db=db))
            for room in rooms:
                params = (room.id, room.name)
                cursor.execute("INSERT INTO rooms VALUES(%s,%s)", params)
        except Error as e:
            raise Exception("Can't load students to db", e)
