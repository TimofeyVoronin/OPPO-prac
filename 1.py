import shlex

class Моря:
    # Определяем класс "Моря" с соответствующими свойствами
    def __init__(self, название, глубина, соленость):
        self.название = название        # Инициализируем свойство "название"
        self.глубина = глубина          # Инициализируем свойство "глубина"
        self.соленость = соленость      # Инициализируем свойство "соленость"

    def __str__(self):
        # Определяем строковое представление объекта для удобного вывода
        return f'"{self.название}" {self.глубина} {self.соленость}'

# Чтение данных из файла 'sea.txt' и вывод на экран
with open('sea.txt', 'r', encoding='utf-8') as file:
    for s in file:
        # Используем shlex.split для корректной обработки кавычек
        tokens = shlex.split(s.strip())

        # Проверяем, что есть минимум 3 токена
        if len(tokens) < 3:
            print(f"Ошибка в строке: {s.strip()}")
            continue

        # Извлечение глубины и солености из последних двух токенов
        соленость = float(tokens[-1])        # Последний токен - соленость
        глубина = float(tokens[-2])          # Предпоследний токен - глубина

        # Остальные токены составляют название, объединяем их обратно в строку
        название_tokens = tokens[:-2]        # Все токены кроме последних двух
        название = ' '.join(название_tokens) # Объединяем название из отдельных слов

        # Создаем объект класса "Моря" с полученными данными
        sea = Моря(название, глубина, соленость)

        # Выводим объект на экран
        print(sea)
