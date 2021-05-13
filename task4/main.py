import argparse
import sys
import mysql.connector
import json
from mysql.connector import Error
from models.students import *
from models.rooms import *
from config import config


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


def call_procedure(cursor, procedure):
    """Call procedure and return result"""

    try:
        cursor.callproc(procedure)
        for result in cursor.stored_results():
            print(result)
            print(result.fetchall())
            return result.fetchall()
    except (BaseException, Error) as e:
        raise ("Can't call procedure", e)


def output_json(result: dict, name_procedure):
    """Output data to a JSON file"""

    name_file = r'result\\' + name_procedure + '.json'
    try:
        with open(name_file, 'w+', encoding='utf-8', ) as file:
            json.dump(result, file, ensure_ascii=False, indent=4)
    except BaseException as e:
        raise Exception("Can't' output JSON data", e)


def main():
    procedures = [
        # 'usp_find_list_rooms_with_students',
        'usp_top5_rooms_with_min_average_age',
        # 'usp_top5_rooms_with_diff_age',
        # 'usp_find_list_rooms_with_mixed_students',
    ]
    parser = get_parser_arguments()
    namespace = parser.parse_args(sys.argv[1:])
    conn = connect_to_database(config)
    if conn:
        # students = StudentFileReader.read_file(namespace.students)
        # rooms = RoomsFileReader.read_file(namespace.rooms)
        cursor = conn.cursor()
        # upload sql
        # RoomsDB.load_rooms_to_db(config['database'], rooms, cursor)
        # StudentDB.load_students_to_db(config['database'], students, cursor)
        # добавить индекс
        conn.commit()
        for procedure in procedures:
            result = call_procedure(cursor, procedure)
            if namespace.format == 'xml':
                output_xml(result)
            elif namespace.format == 'json':
                output_json(result,procedure)
        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()
