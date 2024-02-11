if __name__ == "__main__":
    from typing import List
    
    class Vehicle:
        """
        Базовый класс, представляющий транспортное средство.
        """

        def __init__(self, brand: str, model: str, year: int):
            """
            Конструктор класса Vehicle.

            Параметры:
            - brand (str): Марка транспортного средства.
            - model (str): Модель транспортного средства.
            - year (int): Год выпуска транспортного средства.
            """
            self.brand = brand
            self.model = model
            self.year = year

        def get_vehicle_info(self) -> str:
            """
            Возвращает основную информацию о транспортном средстве.

            Возвращает:
            - str: Строка с основной информацией о транспортном средстве.
            """
            return f"{self.year} {self.brand} {self.model}"

        def __str__(self) -> str:
            """
            Строковое представление объекта Vehicle.
            """
            return f"{self.year} {self.brand} {self.model}"

        def __repr__(self) -> str:
            """
            Машинно-ориентированное представление объекта Vehicle.
            """
            return f"Vehicle(brand={self.brand!r}, model={self.model!r}, year={self.year!r})"


    class SportsCar(Vehicle):
        """
        Подкласс, представляющий спортивный автомобиль, унаследованный от класса Vehicle.
        """

        def __init__(self, brand: str, model: str, year: int, top_speed: float):
            """
            Конструктор класса SportsCar.

            Параметры:
            - brand (str): Марка спортивного автомобиля.
            - model (str): Модель спортивного автомобиля.
            - year (int): Год выпуска спортивного автомобиля.
            - top_speed (float): Максимальная скорость спортивного автомобиля в милях в час.
            """
            super().__init__(brand, model, year)
            self.top_speed = top_speed

        def accelerate(self, speed_increase: float, nitrous_oxide: bool = False) -> None:
            """
            Ускоряет спортивный автомобиль, увеличивая его максимальную скорость.

            Параметры:
            - speed_increase (float): Прирост скорости в милях в час.
            - nitrous_oxide (bool): Флаг использования азота для ускорения (по умолчанию False).

            Примечание:
            Метод перегружен для добавления возможности использования азота для дополнительного ускорения.
            Если флаг nitrous_oxide установлен в True, скорость увеличится на бОльшее значение.
            """
            if nitrous_oxide:
                self.top_speed += speed_increase * 1.5  # Увеличение скорости с азотом
            else:
                self.top_speed += speed_increase

        def __str__(self) -> str:
            """
            Строковое представление объекта SportsCar.
            """
            return f"{super().__str__()} - Максимальная скорость: {self.top_speed} MPH"

        def __repr__(self) -> str:
            """
            Машинно-ориентированное строковое представление объекта SportsCar.
            """
            return f"SportsCar(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, top_speed={self.top_speed!r})"


    class LuxuryCar(Vehicle):
        """
        Подкласс, представляющий представительский автомобиль, унаследованный от класса Vehicle.
        """

        def __init__(self, brand: str, model: str, year: int, luxury_features: list):
            """
            Конструктор класса LuxuryCar.

            Параметры:
            - brand (str): Марка представительского автомобиля.
            - model (str): Модель представительского автомобиля.
            - year (int): Год выпуска представительского автомобиля.
            - luxury_features (list): Список роскошных особенностей представительского автомобиля.
            """
            super().__init__(brand, model, year)
            self.luxury_features: List[str] = luxury_features

        @staticmethod
        def activate_luxury_feature(feature: str) -> str:
            """
            Активирует указанную роскошную особенность представительского автомобиля.

            Параметры:
            - feature (str): Название роскошной особенности.

            Возвращает:
            - str: Сообщение об активации роскошной особенности.
            """
            return f"Активирована роскошная особенность: {feature}"

        def __str__(self) -> str:
            """
            Перегруженный метод для строкового представления объекта LuxuryCar.

            Возвращает:
            - str: Форматированная строка с информацией о представительском автомобиле.
            """
            return f"{super().__str__()} - Роскошные особенности: {', '.join(self.luxury_features)}.\nЭтот автомобиль поддерживает высокий стандарт комфорта."

        def __repr__(self) -> str:
            """
            Машинно-ориентированное строковое представление объекта LuxuryCar.
            """
            return f"LuxuryCar(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, luxury_features={self.luxury_features!r})"
    pass
