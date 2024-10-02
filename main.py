# main.py

# Импортируем необходимые классы и исключения из модулей sea и exceptions
from sea import Sea
from exceptions import InvalidInputError

def read_input():
    """Читает строку ввода от пользователя.

    Returns:
        str: Введенная пользователем строка.
    """
    # Просим пользователя ввести данные о море
    return input("Введите название моря, глубину и соленость через пробел: ")

def parse_input(input_str):
    """Разбирает входную строку и извлекает название, глубину и соленость.

    Args:
        input_str (str): Входная строка.

    Returns:
        tuple: Кортеж из названия (str), глубины (float) и солености (float).

    Raises:
        InvalidInputError: Если входная строка некорректна.
    """
    # Удаляем пробелы в начале и конце строки и разбиваем по пробелам
    tokens = input_str.strip().split()
    # Проверяем, что в строке достаточно токенов
    if len(tokens) < 3:
        raise InvalidInputError("Недостаточно данных для создания объекта Sea.")

    try:
        # Пробуем преобразовать последние два токена в числа (глубина и соленость)
        salinity = float(tokens[-1])   # Последний токен - соленость
        depth = float(tokens[-2])      # Предпоследний токен - глубина
    except ValueError:
        # Если преобразование не удалось, выбрасываем исключение
        raise InvalidInputError("Глубина и соленость должны быть числовыми значениями.")

    # Остальные токены считаем названием моря
    name_tokens = tokens[:-2]
    # Проверяем, что название не пустое
    if not name_tokens:
        raise InvalidInputError("Название моря не может быть пустым.")

    # Объединяем токены названия обратно в строку
    name = ' '.join(name_tokens)
    return name, depth, salinity

def save_to_file(sea, filename='моря.txt'):
    """Сохраняет объект Sea в файл.

    Args:
        sea (Sea): Объект Sea для сохранения.
        filename (str, optional): Имя файла для сохранения. По умолчанию 'моря.txt'.
    """
    try:
        # Открываем файл для добавления информации
        with open(filename, 'a', encoding='utf-8') as file:
            # Записываем строковое представление объекта Sea в файл
            file.write(f'{sea}\n')
    except IOError as e:
        # Выводим сообщение об ошибке, если не удалось записать в файл
        print(f"Ошибка при записи в файл: {e}")

def main():
    """Основная функция программы."""
    try:
        # Читаем ввод пользователя
        input_str = read_input()
        # Разбираем введенную строку и извлекаем данные
        name, depth, salinity = parse_input(input_str)
        # Создаем объект Sea с полученными данными
        sea = Sea(name, depth, salinity)
        # Выводим информацию об объекте Sea
        print(sea)
        # Сохраняем информацию об объекте Sea в файл
        save_to_file(sea)
    except InvalidInputError as e:
        # Обрабатываем ошибки, связанные с некорректным вводом данных
        print(f"Ошибка ввода: {e}")
    except ValueError as e:
        # Обрабатываем ошибки, связанные с неверными значениями глубины или солености
        print(f"Ошибка значения: {e}")
    except Exception as e:
        # Обрабатываем любые другие непредвиденные ошибки
        print(f"Непредвиденная ошибка: {e}")

# Проверяем, что скрипт запущен напрямую, а не импортирован
if __name__ == '__main__':
    main()
