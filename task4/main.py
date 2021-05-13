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


def main():
    parser = get_parser_arguments()
    namespace = parser.parse_args(sys.argv[1:])
    students = StudentFileReader.read_file(namespace.students)
    rooms = RoomsFileReader.read_file(namespace.rooms)
    conn = connect_to_database(config)
    if conn:
        cursor = conn.cursor()
        RoomsDB.load_rooms_to_db(config['database'], rooms, cursor)
        StudentDB.load_students_to_db(config['database'], students, cursor)
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()
