# main.py
from sea import Sea

def read_input():
    """Читает строку ввода от пользователя.

    Returns:
        str: Введенная пользователем строка.
    """
    return input()

def parse_input(input_str):
    """Разбирает входную строку и извлекает название, глубину и соленость.

    Args:
        input_str (str): Входная строка.

    Returns:
        tuple: Кортеж из названия (str), глубины (float) и солености (float).
    """
    tokens = input_str.strip().split()
    salinity = float(tokens[-1])   # Последний токен - соленость
    depth = float(tokens[-2])      # Предпоследний токен - глубина
    name_tokens = tokens[:-2]      # Все токены кроме последних двух
    name = ' '.join(name_tokens)   # Объединяем название из отдельных слов
    return name, depth, salinity

def save_to_file(sea, filename='моря.txt'):
    """Сохраняет объект Sea в файл.

    Args:
        sea (Sea): Объект Sea для сохранения.
        filename (str, optional): Имя файла для сохранения. По умолчанию 'моря.txt'.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{sea}\n')

def main():
    """Основная функция программы."""
    input_str = read_input()
    name, depth, salinity = parse_input(input_str)
    sea = Sea(name, depth, salinity)
    print(sea)
    save_to_file(sea)

if __name__ == '__main__':
    main()
