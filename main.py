# main.py
import shlex
from sea import Sea

def read_input(filename='sea.txt'):
    """Читает строки из файла.

    Args:
        filename (str, optional): Имя файла для чтения. По умолчанию 'sea.txt'.

    Returns:
        list: Список строк из файла.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def parse_input(input_str):
    """Разбирает входную строку и извлекает название, глубину и соленость.

    Args:
        input_str (str): Входная строка.

    Returns:
        tuple: Кортеж из названия (str), глубины (float) и солености (float).
    """
    # Используем shlex.split для корректной обработки кавычек
    tokens = shlex.split(input_str.strip())

    # Проверяем, что есть минимум 3 токена
    if len(tokens) < 3:
        raise ValueError(f"Ошибка в строке: {input_str.strip()}")

    # Извлечение глубины и солености из последних двух токенов
    salinity = float(tokens[-1])   # Последний токен - соленость
    depth = float(tokens[-2])      # Предпоследний токен - глубина

    # Остальные токены составляют название, объединяем их обратно в строку
    name_tokens = tokens[:-2]      # Все токены кроме последних двух
    name = ' '.join(name_tokens)   # Объединяем название из отдельных слов

    return name, depth, salinity

def main():
    """Основная функция программы."""
    try:
        input_lines = read_input()
        for input_str in input_lines:
            try:
                name, depth, salinity = parse_input(input_str)
                sea = Sea(name, depth, salinity)
                print(sea)
            except ValueError as e:
                print(e)
    except FileNotFoundError:
        print("Файл 'sea.txt' не найден.")

if __name__ == '__main__':
    main()
