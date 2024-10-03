# main.py

import shlex
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
    """Разбирает входную строку и извлекает название, глубину и соленость.

    Args:
        input_str (str): Входная строка.

    Returns:
        tuple: Кортеж из названия (str), глубины (float) и солености (float).

    Raises:
        InvalidInputError: Если входная строка некорректна.
    """
    # Используем shlex.split для корректной обработки кавычек
    tokens = shlex.split(input_str.strip())
    if len(tokens) < 3:
        raise InvalidInputError("Недостаточно данных для создания объекта Sea.")

    try:
        salinity = float(tokens[-1])
        depth = float(tokens[-2])
    except ValueError:
        raise InvalidInputError("Глубина и соленость должны быть числовыми значениями.")

    name_tokens = tokens[:-2]
    if not name_tokens:
        raise InvalidInputError("Название моря не может быть пустым.")

    name = ' '.join(name_tokens)
    return name, depth, salinity

def main():
    """Основная функция программы."""
    try:
        input_lines = read_input()
        for line in input_lines:
            try:
                name, depth, salinity = parse_input(line)
                sea = Sea(name, depth, salinity)
                print(sea)
            except (InvalidInputError, ValueError) as e:
                print(f"Ошибка в строке '{line.strip()}': {e}")
    except FileNotFoundError as e:
        print(e)

if __name__ == '__main__':
    main()
