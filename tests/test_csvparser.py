import sys
sys.path.append("..")

import csv_parser
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


if __name__ == '__main__':
    unittest.main()
