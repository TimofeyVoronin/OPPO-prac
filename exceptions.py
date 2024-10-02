# exceptions.py

class SeaError(Exception):
    """Базовый класс исключений для модуля sea."""
    pass  # Пока нет дополнительных атрибутов или методов

class InvalidInputError(SeaError):
    """Исключение для некорректного ввода пользователя."""
    pass  # Используется для сигнализации об ошибках ввода
