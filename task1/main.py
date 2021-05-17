import argparse
import json
from lxml import etree
from students import Student, StudentFileReader
from rooms import Room, RoomsFileReader
from serializer import XMLSerializer, JsonSerializer


def get_parser_arguments():
    """Creating params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--students', type=str, default=None, help='Path to the students json file')
    parser.add_argument('-r', '--rooms', type=str, default=None, help='Path to the rooms json file')
    parser.add_argument('-f', '--format', choices=['xml', 'json'], type=str.lower, default=None,
                        help='Output format of the results')

    return parser


def combine_rooms_and_students(rooms: list, students: list) -> dict:
    """Combine room and student data and return the result"""

    result = {}
    for room in rooms:
        result[room.id] = {'name': room.name, 'students': []}
    for student in students:
        if result.get(student.room):
            result[student.room]['students'].append(student.name)
        elif result.get('swr'):
            result['swr']['students_without_room'].append(student.name)
        else:
            result['swr'] = {'students_without_room': []}
    return result


def main():
    name_file = r'result\result.'
    output_file = {'xml': XMLSerializer.output_xml, 'json': JsonSerializer.output_json}
    parser = get_parser_arguments()
    namespace = parser.parse_args()
    students = StudentFileReader.read_file(namespace.students)
    rooms = RoomsFileReader.read_file(namespace.rooms)
    result = combine_rooms_and_students(rooms, students)
    output_file[namespace.format](result, name_file + namespace.format)


if __name__ == '__main__':
    main()
