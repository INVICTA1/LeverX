import argparse
import sys
import json
from lxml import etree
from students import Student, StudentFileReader
from rooms import Room, RoomsFileReader


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


def get_parser_arguments():
    """Creating params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--students', type=str, default=None, help='Path to the students json file')
    parser.add_argument('-r', '--rooms', type=str, default=None, help='Path to the rooms json file')
    parser.add_argument('-f', '--format', choices=['xml', 'json'], type=str.lower, default=None,
                        help='Output format of the results')
    return parser


def output_xml(result: dict):
    """Output data to a XML file"""

    name_file = r'result\result.xml'
    try:
        data = etree.Element('data')
        for key, value in result.items():
            room = etree.SubElement(data, 'room', id=str(key))
            room.text = value['name']
            for stud in value['students']:
                student = etree.SubElement(room, 'student')
                student.text = stud
        data = etree.ElementTree(data)
        with open(name_file, 'wb') as file:
            data.write(file, xml_declaration=True, pretty_print=True)
    except Exception as MyException:
        raise MyException


def output_json(result: dict):
    """Output data to a JSON file"""

    name_file = r'result\result.json'
    try:
        with open(name_file, 'w+', encoding='utf-8', ) as file:
            json.dump(result, file, ensure_ascii=False, indent=4)
    except Exception as MyException:
        raise Exception("Can't' output JSON data", MyException)


def main():
    parser = get_parser_arguments()
    namespace = parser.parse_args(sys.argv[1:])
    students = StudentFileReader.read_file(namespace.students)
    rooms = RoomsFileReader.read_file(namespace.rooms)
    result = combine_rooms_and_students(rooms, students)
    if namespace.format == 'xml':
        output_xml(result)
    elif namespace.format == 'json':
        output_json(result)


if __name__ == '__main__':
    main()
