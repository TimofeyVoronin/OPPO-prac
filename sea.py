# sea.py
class Sea:
    """Класс, представляющий море с соответствующими свойствами."""

    def __init__(self, name, depth, salinity):
        """Инициализирует объект Sea.

        Args:
            name (str): Название моря.
            depth (float): Глубина моря.
            salinity (float): Соленость моря.
        """
        self.name = name
        self.depth = depth
        self.salinity = salinity

    def __str__(self):
        """Возвращает строковое представление объекта Sea."""
        return f'"{self.name}" {self.depth} {self.salinity}'
