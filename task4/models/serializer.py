import json
from lxml import etree


class XMLSerializer():
    @classmethod
    def create_xml_data(self, result: dict):
        """Creating structure XML file"""

        data = etree.Element('data')
        for row in result:
            if len(row) == 2:
                room = etree.SubElement(data, 'room')
                room.text = row[0]
                num_students = etree.SubElement(room, 'num_students')
                num_students.text = str(row[1])
            elif len(row) == 1:
                room = etree.SubElement(data, 'room')
                room.text = row[0]
        data = etree.ElementTree(data)
        return data

    @staticmethod
    def output_xml(result: dict, name_file: str):
        """Output data to a XML file"""

        try:
            name_file = r'result\xml\\' + name_file
            xml_data = XMLSerializer.create_xml_data(result)
            with open(name_file, 'wb') as file:
                xml_data.write(file, xml_declaration=True, pretty_print=True)
        except Exception as MyException:
            raise MyException


class JsonSerializer():
    @staticmethod
    def output_json(result: dict, name_file: str):
        """Output data to a JSON file"""

        try:
            name_file = r'result\json\\' + name_file
            with open(name_file, 'w+', encoding='utf-8', ) as file:
                json.dump(result, file, ensure_ascii=False, indent=4)
        except Exception as MyException:
            raise Exception("Can't' output JSON data", MyException)
