import argparse
import sys
from models.students import *
from models.rooms import *

import mysql.connector
from config import config
from mysql.connector import Error


def connect_to_database(config):
    """Connect to mysql server with config params"""

    try:
        conn = mysql.connector.connect(**config)
        return conn
    except Error as e:
        raise ("Can't connect to database", e)


def get_parser_arguments():
    """Creating params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--students', type=str, default=None, help='Path to the students json file')
    parser.add_argument('-r', '--rooms', type=str, default=None, help='Path to the rooms json file')
    parser.add_argument('-f', '--format', choices=['xml', 'json'], type=str.lower, default=None,
                        help='Output format of the results')
    return parser


def load_students_to_db(db, table, students, cursor):
    try:
        cursor.execute('USE {db}'.format(db=db))
        for student in students:
            cursor.execute("INSERT INTO {table} VALUES({student})".format(table=table, student=student))
    except Error as e:
        raise Exception("Can't load students to db", e)


def load_rooms_to_db(db, table, rooms, cursor):
    try:
        cursor.execute('USE {db}'.format(db=db))
        for room in rooms:
            cursor.execute("INSERT INTO {table} VALUES({room})".format(table=table, room=room))
    except Error as e:
        raise Exception("Can''t load students to db", e)


def main():
    parser = get_parser_arguments()
    namespace = parser.parse_args(sys.argv[1:])
    students = StudentFileReader.read_file(namespace.students)
    rooms = RoomsFileReader.read_file(namespace.rooms)
    conn = connect_to_database(config)
    if conn:
        cursor = conn.cursor()
        load_rooms_to_db(config['database'], 'rooms', rooms, cursor)
        load_students_to_db(config['database'], 'students', students, cursor)
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()
