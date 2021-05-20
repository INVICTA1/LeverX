import os
import mysql.connector
import re
from mysql.connector import Error


class PathFinder():
    @classmethod
    def walk_tree(self, path: str):
        """Recursive search of the directory"""

        for root, dirs, files in os.walk(path):
            for dir in dirs:
                yield root, dir

    @classmethod
    def find_path_files_in_dir(self, dirparent: str, dir: str, extension: str) -> list:
        """Find paths to files in directory """

        paths_files = []
        for root, dirs, files in os.walk(dirparent + '\\' + dir):
            for file in files:
                if os.path.splitext(file)[-1] == extension:
                    paths_files.append(root + '\\' + file)
        return paths_files

    @staticmethod
    def find_path_files(dirs, path, extension):
        """Find files with extension in directory"""
        result = []
        for dir in dirs:
            for dirparent, dirname in PathFinder.walk_tree(path):
                if dirname == dir:
                    result.extend(PathFinder.find_path_files_in_dir(dirparent, dir, extension))
        return result


class SqlFileReader():
    @staticmethod
    def read_sql_files(file_path: str):
        """Parsing sql script and executing this code"""

        try:
            with open(file_path) as sql_file:
                return sql_file.read().strip()
        except (Exception) as e:
            raise ("Can't read SQL files", e)


class SqlDB():
    @staticmethod
    def connect_to_database(config):
        """Connect to mysql server with config params"""

        try:
            conn = mysql.connector.connect(**config)
            return conn
        except Error as e:
            raise ("Can't connect to databases", e)

    @staticmethod
    def call_procedure(cursor, procedure):
        """Call procedure and return result"""

        try:
            cursor.callproc(procedure)
            for result in cursor.stored_results():
                return result.fetchall()
        except (Exception, Error) as e:
            raise ("Can't call procedure", e)

    @classmethod
    def execute_sql_script(self, cursor, sql_script: str):
        """Split SQL code on functions and execute this functions"""

        try:
            functions = sql_script.strip().split(';')
            for function in functions:
                if function:
                    cursor.execute(function)
        except (Exception, Error) as e:
            raise ("Can't execute sql script", e)

    @staticmethod
    def upload_sql_file(cursor, sql_script):
        """Parsing sql script and executing this code"""

        try:
            instructions = re.findall('\$\$([^$]*)\$\$', sql_script)
            if instructions:
                sql_script = re.findall('([^$]*)DELIMITER', sql_script)[0]
                SqlDB.execute_sql_script(cursor, sql_script)
                for instruction in instructions:
                    cursor.execute(instruction)
            else:
                SqlDB.execute_sql_script(cursor, sql_script)
        except (Exception, Error) as e:
            raise ("Can't upload SQL files", e)

    @staticmethod
    def create_index(cursor, index, table, column):
        """Creating index in Mysql Table"""

        cursor.execute('create index {index} on {table}({column});'.format(index=index,
                                                                           table=table,
                                                                           column=column))
