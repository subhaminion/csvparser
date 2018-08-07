import sys
sys.path.append("..")

import os
import io
import json
import csv_parser
import tempfile
import unittest
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ParseError


class TestParserMethods(unittest.TestCase):

    def setUp(self):
        self.valid_data = {
            "name": "Valid Name",
            "address": "Valid Address, With valid St name, and Number :D",
            "stars": 5,
            "contact": "Subham Bhattacharjee",
            "phone": "+91 90467 89016",
            "uri": "http://www.sbcharjee.co"
        }

        self.invalid_name = {
            "name": 1565
        }

        self.invalid_uri = {
            "uri": "garbage",
        }

        self.invalid_stars_negative = {
            "stars": -5
        }

        self.invalid_stars_string = {
            "stars": 'random'
        }

        self.new_json_file, self.json_file = tempfile.mkstemp()
        with io.open(self.json_file, 'w', encoding='utf8') as f:
            json.dump(self.valid_data, f, ensure_ascii=False)

        with open(self.json_file, 'r') as f:
            self.valid_json_file_output = f.read()

        self.new_xml_file, self.xml_file = tempfile.mkstemp()
        with io.open(self.xml_file, 'w') as f:
            f.write(csv_parser.convert_row_to_xml(self.valid_data))

        with open(self.xml_file, 'r') as f:
            self.valid_xml_file_output = f.read()

    def test_is_valid_name(self):
        self.assertTrue(csv_parser.is_valid_name(self.valid_data))

    def test_is_valid_name_false(self):
        self.assertFalse(csv_parser.is_valid_name(self.invalid_name))

    def test_is_valid_url(self):
        self.assertTrue(csv_parser.is_valid_url(self.valid_data))

    def test_is_valid_url_false(self):
        self.assertFalse(csv_parser.is_valid_url(self.invalid_uri))

    def test_is_valid_stars(self):
        self.assertTrue(csv_parser.is_valid_stars(self.valid_data))

    def test_is_valid_stars_false(self):
        self.assertFalse(csv_parser.is_valid_stars(self.invalid_stars_negative))

    def test_is_valid_stars_raise_exception(self):
        self.assertRaises(ValueError, csv_parser.is_valid_stars, self.invalid_stars_string)

    def test_validate_fields(self):
        self.assertTrue(csv_parser.validate_fields(self.valid_data))

    def test_convert_row_to_xml(self):
        xml = csv_parser.convert_row_to_xml(self.valid_data)
        try:
            parsed_xml = ET.fromstring(xml)
        except ParseError:
            self.assertTrue(False)

    def test_generate_json_file_output(self):
        cwd = os.getcwd()
        csv_parser.generate_json_file(self.valid_data, cwd)
        filename = 'hotels.json'
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                output = f.read()
        os.remove(filename)
        self.assertMultiLineEqual(self.valid_json_file_output, output)

    def test_generate_xml_file_output(self):
        output = csv_parser.convert_row_to_xml(self.valid_data)
        self.assertMultiLineEqual(self.valid_xml_file_output, output)


if __name__ == '__main__':
    unittest.main()
