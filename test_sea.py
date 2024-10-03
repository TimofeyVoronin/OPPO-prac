# test_sea.py

import unittest
from sea import Sea
from main import parse_input
from exceptions import InvalidInputError

class TestSea(unittest.TestCase):

    def test_sea_creation(self):
        sea = Sea("Балтийское море", 55.0, 7.0)
        self.assertEqual(sea.name, "Балтийское море")
        self.assertEqual(sea.depth, 55.0)
        self.assertEqual(sea.salinity, 7.0)

    def test_negative_depth(self):
        with self.assertRaises(ValueError):
            Sea("Мертвое море", -1, 33.7)

    def test_negative_salinity(self):
        with self.assertRaises(ValueError):
            Sea("Красное море", 2211, -40)

class TestParseInput(unittest.TestCase):

    def test_parse_correct_input_without_quotes(self):
        input_str = "Балтийское море 55.0 7.0"
        name, depth, salinity = parse_input(input_str)
        self.assertEqual(name, "Балтийское море")
        self.assertEqual(depth, 55.0)
        self.assertEqual(salinity, 7.0)

    def test_parse_correct_input_with_quotes(self):
        input_str = '"Море Лаптевых" 3400 30.0'
        name, depth, salinity = parse_input(input_str)
        self.assertEqual(name, "Море Лаптевых")
        self.assertEqual(depth, 3400.0)
        self.assertEqual(salinity, 30.0)

    def test_parse_incorrect_input_missing_data(self):
        input_str = "Балтийское море 55.0"
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

    def test_parse_incorrect_input_non_numeric(self):
        input_str = "Балтийское море глубина соленость"
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

    def test_parse_empty_name(self):
        input_str = "55.0 7.0"
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

if __name__ == '__main__':
    unittest.main()
