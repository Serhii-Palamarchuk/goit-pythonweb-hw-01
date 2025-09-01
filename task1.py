"""
Завдання 1: Патерн Фабрика
Реалізація системи створення транспортних засобів з регіональними специфікаціями
"""

import logging
from abc import ABC, abstractmethod
from typing import Protocol

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    """Абстрактний базовий клас для всіх транспортних засобів"""

    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        """Абстрактний метод для запуску двигуна"""
        pass


class Car(Vehicle):
    """Клас автомобіля"""

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    """Клас мотоцикла"""

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory(ABC):
    """Абстрактна фабрика для створення транспортних засобів"""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        """Створює автомобіль з відповідною специфікацією"""
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        """Створює мотоцикл з відповідною специфікацією"""
        pass


class USVehicleFactory(VehicleFactory):
    """Фабрика для створення транспортних засобів за американськими специфікаціями"""

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    """Фабрика для створення транспортних засобів за європейськими специфікаціями"""

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


def main() -> None:
    """Демонстрація роботи фабрик"""
    logger.info("=== Демонстрація патерну Фабрика ===")

    # Створення американської фабрики
    us_factory = USVehicleFactory()
    logger.info("Створено американську фабрику")

    # Створення європейської фабрики
    eu_factory = EUVehicleFactory()
    logger.info("Створено європейську фабрику")

    # Створення транспортних засобів за американськими специфікаціями
    logger.info("\n--- Американські транспортні засоби ---")
    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    us_car.start_engine()
    us_motorcycle.start_engine()

    # Створення транспортних засобів за європейськими специфікаціями
    logger.info("\n--- Європейські транспортні засоби ---")
    eu_car = eu_factory.create_car("BMW", "X5")
    eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Panigale")

    eu_car.start_engine()
    eu_motorcycle.start_engine()


if __name__ == "__main__":
    main()
