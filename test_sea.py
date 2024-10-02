# test_sea.py

import unittest
from sea import Sea  # Импортируем класс Sea из файла sea.py
from main import parse_input  # Импортируем функцию parse_input из main.py
from exceptions import InvalidInputError  # Импортируем пользовательское исключение

# Определяем класс тестов для класса Sea
class TestSea(unittest.TestCase):

    # Тестируем корректное создание объекта Sea
    def test_sea_creation(self):
        # Создаем объект Sea с корректными параметрами
        sea = Sea("Балтийское море", 55.0, 7.0)
        # Проверяем, что имя моря установлено правильно
        self.assertEqual(sea.name, "Балтийское море")
        # Проверяем, что глубина моря установлена правильно
        self.assertEqual(sea.depth, 55.0)
        # Проверяем, что соленость моря установлена правильно
        self.assertEqual(sea.salinity, 7.0)

    # Тестируем создание объекта Sea с отрицательной глубиной
    def test_negative_depth(self):
        # Ожидаем, что при попытке установить отрицательную глубину будет вызвано исключение ValueError
        with self.assertRaises(ValueError):
            Sea("Мертвое море", -1, 33.7)

    # Тестируем создание объекта Sea с отрицательной соленостью
    def test_negative_salinity(self):
        # Ожидаем, что при попытке установить отрицательную соленость будет вызвано исключение ValueError
        with self.assertRaises(ValueError):
            Sea("Красное море", 2211, -40)

# Определяем класс тестов для функции parse_input
class TestParseInput(unittest.TestCase):

    # Тестируем корректный разбор входной строки
    def test_parse_correct_input(self):
        # Входная строка с корректными данными
        input_str = "Балтийское море 55.0 7.0"
        # Разбираем входную строку и получаем имя, глубину и соленость
        name, depth, salinity = parse_input(input_str)
        # Проверяем, что имя получено корректно
        self.assertEqual(name, "Балтийское море")
        # Проверяем, что глубина получена корректно
        self.assertEqual(depth, 55.0)
        # Проверяем, что соленость получена корректно
        self.assertEqual(salinity, 7.0)

    # Тестируем разбор строки с отсутствующими данными
    def test_parse_incorrect_input_missing_data(self):
        # Входная строка с недостаточным количеством данных
        input_str = "Балтийское море 55.0"
        # Ожидаем, что при разборе будет вызвано исключение InvalidInputError
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

    # Тестируем разбор строки с нечисловыми значениями глубины и солености
    def test_parse_incorrect_input_non_numeric(self):
        # Входная строка с нечисловыми значениями
        input_str = "Балтийское море глубина соленость"
        # Ожидаем, что при разборе будет вызвано исключение InvalidInputError
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

    # Тестируем разбор строки без указания названия моря
    def test_parse_empty_name(self):
        # Входная строка без названия моря
        input_str = "55.0 7.0"
        # Ожидаем, что при разборе будет вызвано исключение InvalidInputError
        with self.assertRaises(InvalidInputError):
            parse_input(input_str)

# Запускаем тесты, если скрипт выполняется напрямую
if __name__ == '__main__':
    unittest.main()
