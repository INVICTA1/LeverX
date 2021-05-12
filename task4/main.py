import argparse
import sys
from models.students import *
from models.rooms import *


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


if __name__ == '__main__':
    main()
