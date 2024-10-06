# sea.py

import re
from exceptions import InvalidInputError

class Sea:
    """Класс, представляющий море с соответствующими свойствами."""

    def __init__(self, tokens):
        """Инициализирует объект Sea.

        Args:
            tokens (list): Список токенов в исходном порядке.

        Raises:
            InvalidInputError: Если свойства некорректны.
        """
        self.tokens = tokens
        self.name = None
        self.depth = None
        self.salinity = None

        self.parse_tokens()

    def parse_tokens(self):
        """Разбирает токены для извлечения названия, глубины и солености."""
        name_token = None
        depth_token = None
        salinity_token = None

        for token in self.tokens:
            if token.startswith('"') and token.endswith('"'):
                if name_token is not None:
                    raise InvalidInputError("Допускается только одно название, заключенное в двойные кавычки.")
                if token.count('"') != 2:
                    raise InvalidInputError("Некорректное использование двойных кавычек.")
                name_token = token
                self.name = name_token.strip('"')
                if not self.name:
                    raise InvalidInputError("Название моря не может быть пустым.")
                if re.search(r'\d', self.name):
                    raise InvalidInputError("Название моря не может содержать цифры.")
            else:
                if depth_token is None:
                    depth_token = token
                elif salinity_token is None:
                    salinity_token = token
                else:
                    raise InvalidInputError("Непредвиденный дополнительный токен.")

        if name_token is None:
            raise InvalidInputError("Название моря должно быть заключено в двойные кавычки.")

        try:
            self.depth = float(depth_token)
            if self.depth < 0:
                raise InvalidInputError("Глубина не может быть отрицательной.")
        except ValueError:
            raise InvalidInputError("Глубина должна быть числовым значением.")

        try:
            self.salinity = float(salinity_token)
            if self.salinity < 0:
                raise InvalidInputError("Соленость не может быть отрицательной.")
        except ValueError:
            raise InvalidInputError("Соленость должна быть числовым значением.")

    def __str__(self):
        """Возвращает строковое представление объекта Sea."""
        return ' '.join(self.tokens)
