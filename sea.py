# sea.py

class Sea:
    """Класс, представляющий море с соответствующими свойствами."""

    def __init__(self, name, depth, salinity):
        """Инициализирует объект Sea.

        Args:
            name (str): Название моря.
            depth (float): Глубина моря.
            salinity (float): Соленость моря.

        Raises:
            ValueError: Если глубина или соленость имеют некорректные значения.
        """
        self.name = name  # Устанавливаем название моря
        self.depth = self.validate_depth(depth)  # Проверяем и устанавливаем глубину
        self.salinity = self.validate_salinity(salinity)  # Проверяем и устанавливаем соленость

    @staticmethod
    def validate_depth(depth):
        """Проверяет корректность значения глубины.

        Args:
            depth (float): Значение глубины.

        Returns:
            float: Корректное значение глубины.

        Raises:
            ValueError: Если глубина отрицательная.
        """
        if depth < 0:
            raise ValueError("Глубина не может быть отрицательной.")  # Выбрасываем исключение при отрицательной глубине
        return depth  # Возвращаем корректное значение глубины

    @staticmethod
    def validate_salinity(salinity):
        """Проверяет корректность значения солености.

        Args:
            salinity (float): Значение солености.

        Returns:
            float: Корректное значение солености.

        Raises:
            ValueError: Если соленость отрицательная.
        """
        if salinity < 0:
            raise ValueError("Соленость не может быть отрицательной.")  # Выбрасываем исключение при отрицательной солености
        return salinity  # Возвращаем корректное значение солености

    def __str__(self):
        """Возвращает строковое представление объекта Sea."""
        return f'"{self.name}" {self.depth} {self.salinity}'  # Формируем строку для вывода
