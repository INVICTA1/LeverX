import argparse
import sys
from models.students import StudentFileReader, StudentDB, Student
from models.rooms import RoomsFileReader, RoomsDB, Room
from models.sqlreader import PathFinder, SqlDB, SqlFileReader
from models.serializer import XMLSerializer, JsonSerializer
from config import config


def get_parser_arguments():
    """Creating params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--students', type=str, default=None, help='Path to the students json file')
    parser.add_argument('-r', '--rooms', type=str, default=None, help='Path to the rooms json file')
    parser.add_argument('-f', '--format', choices=['xml', 'json'], type=str.lower, default=None,
                        help='Output format of the results')
    return parser


def main():
    procedures = [
        'usp_find_list_rooms_with_students',
        'usp_top5_rooms_with_min_average_age',
        'usp_top5_rooms_with_diff_age',
        'usp_find_list_rooms_with_mixed_students',
    ]
    sql_dirs = [
        'databases',
        'tables',
        'procedures',
    ]
    extension = '.sql'
    db_dir = 'db\\'
    output_file = {'xml': XMLSerializer.output_xml, 'json': JsonSerializer.output_json}
    parser = get_parser_arguments()
    namespace = parser.parse_args(sys.argv[1:])
    with SqlDB.connect_to_database(config) as conn:
        cursor = conn.cursor()
        sql_files = PathFinder.find_path_files(dirs=sql_dirs, path=db_dir, extension=extension)
        for file in sql_files:
            sql_file = SqlFileReader.read_sql_files(file)
            SqlDB.upload_sql_file(cursor, sql_file)

        students = StudentFileReader.read_file(namespace.students)
        rooms = RoomsFileReader.read_file(namespace.rooms)

        RoomsDB.load_rooms_to_db(cursor, db=config['database'], rooms=rooms, )
        StudentDB.load_students_to_db(cursor, db=config['database'], students=students)

        SqlDB.create_index(cursor, index='in_std_room', table='students', column='room')

        conn.commit()
        for procedure in procedures:
            result = SqlDB.call_procedure(cursor, procedure)
            name_file = procedure + '.' + namespace.format
            output_file[namespace.format](result, name_file)


if __name__ == '__main__':
    main()
