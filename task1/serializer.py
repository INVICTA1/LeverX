import json
from lxml import etree


class XMLSerializer():
    @classmethod
    def create_xml_data(self, result: dict):
        """Creating structure XML file"""

        data = etree.Element('data')
        for key, value in result.items():
            room = etree.SubElement(data, 'room', id=str(key))
            room.text = value['name']
            for stud in value['students']:
                student = etree.SubElement(room, 'student')
                student.text = stud
        data = etree.ElementTree(data)
        return data

    @staticmethod
    def output_xml(result: dict, name_file: str):
        """Output data to a XML file"""

        try:
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
            with open(name_file, 'w+', encoding='utf-8', ) as file:
                json.dump(result, file, ensure_ascii=False, indent=4)
        except Exception as MyException:
            raise Exception("Can't' output JSON data", MyException)
