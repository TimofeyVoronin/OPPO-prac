import shlex

class Моря:
    def __init__(self, tokens):
        self.tokens = tokens  # Сохраняем токены в исходном порядке

    def __str__(self):
        return ' '.join(self.tokens)  # Выводим токены без изменения порядка

# Чтение данных из файла 'sea.txt' и вывод на экран
with open('sea.txt', 'r', encoding='utf-8') as file:
    for s in file:
        lexer = shlex.shlex(s.strip(), posix=False)
        lexer.whitespace_split = True
        tokens = list(lexer)

        if len(tokens) != 3:
            print(f"Ошибка в строке: {s.strip()}")
            continue

        # Ищем название моря в кавычках
        sea_name_token = None
        for t in tokens:
            if t.startswith('"') and t.endswith('"'):
                sea_name_token = t
                break

        if sea_name_token is None:
            print(f"Ошибка: Название моря должно быть в кавычках в строке: {s.strip()}")
            continue

        sea_name = sea_name_token.strip('"')
        # Проверяем, что название моря не является числом
        try:
            float(sea_name)
            print(f"Ошибка: Название моря не должно быть числом в строке: {s.strip()}")
            continue
        except ValueError:
            pass  # Название не является числом

        # Остальные два токена должны быть числами (глубина и соленость)
        other_tokens = tokens.copy()
        other_tokens.remove(sea_name_token)
        try:
            numbers = [float(t) for t in other_tokens]
        except ValueError:
            print(f"Ошибка: Глубина и соленость должны быть числами в строке: {s.strip()}")
            continue

        # Проверяем, что глубина и соленость не отрицательные
        if any(n < 0 for n in numbers):
            print(f"Ошибка: Отрицательные значения недопустимы в строке: {s.strip()}")
            continue

        # Создаем объект Моря с сохранением исходной последовательности токенов
        sea = Моря(tokens)
        print(sea)
