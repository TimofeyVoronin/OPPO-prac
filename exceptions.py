# exceptions.py

class SeaError(Exception):
    """Базовый класс исключений для модуля sea."""
    pass

class InvalidInputError(SeaError):
    """Исключение для некорректного ввода пользователя."""
    pass
