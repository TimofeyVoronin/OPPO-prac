# main.py

import shlex
import re
from sea import Sea
from exceptions import InvalidInputError

def read_input(filename='sea.txt'):
    """Читает строки из файла.

    Args:
        filename (str, optional): Имя файла для чтения. По умолчанию 'sea.txt'.

    Returns:
        list: Список строк из файла.

    Raises:
        FileNotFoundError: Если файл не найден.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{filename}' не найден.")

def parse_input(input_str):
    """Разбирает входную строку и извлекает токены в исходном порядке.

    Args:
        input_str (str): Входная строка.

    Returns:
        list: Список токенов в исходном порядке.

    Raises:
        InvalidInputError: Если входная строка некорректна.
    """
    # Возвращаем пустой список для пустой строки
    if not input_str.strip():
        return []

    tokens = shlex.split(input_str.strip(), posix=False)
    if len(tokens) != 3:
        raise InvalidInputError("В строке должно быть ровно три элемента.")

    name_token = None
    depth_token = None
    salinity_token = None

    # Ищем название моря в кавычках
    for token in tokens:
        if token.startswith('"') and token.endswith('"'):
            if name_token is not None:
                raise InvalidInputError("Допускается только одно название, заключенное в двойные кавычки.")
            if token.count('"') != 2:
                raise InvalidInputError("Некорректное использование двойных кавычек.")
            name_token = token
            name = name_token.strip('"')
            if not name:
                raise InvalidInputError("Название моря не может быть пустым.")
            if re.search(r'\d', name):
                raise InvalidInputError("Название моря не может содержать цифры.")
        else:
            # Это должно быть глубина или соленость
            if depth_token is None:
                depth_token = token
            elif salinity_token is None:
                salinity_token = token
            else:
                raise InvalidInputError("Непредвиденный дополнительный токен.")

    if name_token is None:
        raise InvalidInputError("Название моря должно быть заключено в двойные кавычки.")

    # Проверяем глубину и соленость
    try:
        depth = float(depth_token)
        if depth < 0:
            raise InvalidInputError("Глубина не может быть отрицательной.")
    except ValueError:
        raise InvalidInputError("Глубина должна быть числовым значением.")

    try:
        salinity = float(salinity_token)
        if salinity < 0:
            raise InvalidInputError("Соленость не может быть отрицательной.")
    except ValueError:
        raise InvalidInputError("Соленость должна быть числовым значением.")

    return tokens  # Возвращаем токены в исходном порядке

def main():
    """Основная функция программы."""
    try:
        input_lines = read_input()
        for line in input_lines:
            line = line.rstrip('\n')
            if not line.strip():
                print()  # Выводим пустую строку для пустого ввода
                continue
            try:
                tokens = parse_input(line)
                sea = Sea(tokens)
                print(' '.join(tokens))
            except InvalidInputError as e:
                print(f"Ошибка в строке '{line}': {e}")
    except FileNotFoundError as e:
        print(e)

if __name__ == '__main__':
    main()
