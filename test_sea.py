# test_sea.py

import unittest
from sea import Sea
from main import parse_input
from exceptions import InvalidInputError

class TestSea(unittest.TestCase):

    def test_sea_creation(self):
        tokens = ['"Балтийское море"', '55.0', '7.0']
        sea = Sea(tokens)
        self.assertEqual(sea.name, "Балтийское море")
        self.assertEqual(sea.depth, 55.0)
        self.assertEqual(sea.salinity, 7.0)

    def test_negative_depth(self):
        tokens = ['"Мертвое море"', '-1', '33.7']
        with self.assertRaises(InvalidInputError):
            Sea(tokens)

    def test_negative_salinity(self):
        tokens = ['"Красное море"', '2211', '-40']
        with self.assertRaises(InvalidInputError):
            Sea(tokens)

class TestParseInput(unittest.TestCase):

    def test_parse_correct_input(self):
        inputs = [
            '"Море Лаптевых" 3400 30.0',
            '3400 "Море Лаптевых" 30.0',
            '3400 30.0 "Море Лаптевых"'
        ]
        for input_str in inputs:
            tokens = parse_input(input_str)
            self.assertEqual(len(tokens), 3)
            self.assertIn('"Море Лаптевых"', tokens)
            self.assertIn('3400', tokens)
            self.assertIn('30.0', tokens)

    def test_parse_empty_line(self):
        input_str = ''
        tokens = parse_input(input_str)
        self.assertEqual(tokens, [])

    def test_parse_incorrect_input_missing_quotes(self):
        input_str = 'Балтийское море 55.0 7.0'
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

    def test_parse_incorrect_input_empty_name(self):
        input_str = '"" 55.0 7.0'
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

    def test_parse_incorrect_input_name_with_digits(self):
        input_str = '"Море123" 55.0 7.0'
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

    def test_parse_incorrect_input_non_numeric(self):
        input_str = '"Балтийское море" глубина соленость'
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

    def test_parse_incorrect_order(self):
        input_str = '55.0 "Балтийское море" "7.0"'
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

    def test_parse_incorrect_quotes_in_depth_salinity(self):
        inputs = [
            '"Балтийское море" "55.0" 7.0',
            '"Балтийское море" 55.0 "7.0"',
            '3400 "Море Лаптевых" "30.0"'
        ]
        for input_str in inputs:
            with self.assertRaises(InvalidInputError):
                parse_input(input_str)

if __name__ == '__main__':
    unittest.main()
