# GoIT Python Web Development - Домашнє завдання 1

Цей проект містить рішення двох завдань з використанням патернів проектування та принципів SOLID.

## Структура проекту

```
goit-pythonweb-hw-01/
├── main.py          # Головний файл для запуску завдань
├── task1.py         # Завдання 1: Патерн Фабрика
├── task2.py         # Завдання 2: SOLID принципи
├── pyproject.toml   # Конфігурація Poetry
└── README.md        # Цей файл
```

## Вимоги

- Python 3.8+
- Poetry (для управління залежностями)

## Встановлення

1. Клонуйте репозиторій:
```bash
git clone <repository-url>
cd goit-pythonweb-hw-01
```

2. Встановіть Poetry (якщо не встановлено):
```bash
# Windows PowerShell
Invoke-RestMethod -Uri https://install.python-poetry.org | py -
```

3. Встановіть залежності:
```bash
poetry install --no-root
```

## Запуск

### Запуск через головне меню:
```bash
poetry run python main.py
```

### Запуск окремих завдань:
```bash
# Завдання 1: Патерн Фабрика
poetry run python task1.py

# Завдання 2: SOLID принципи
poetry run python task2.py
```

## Завдання 1: Патерн Фабрика

Реалізує систему створення транспортних засобів з різними регіональними специфікаціями:

### Основні компоненти:
- `Vehicle` - абстрактний базовий клас
- `Car`, `Motorcycle` - конкретні типи транспорту
- `VehicleFactory` - абстрактна фабрика
- `USVehicleFactory`, `EUVehicleFactory` - конкретні фабрики

### Особливості:
- Використання типізації
- Логування замість print
- Дотримання принципів OOP
- Форматування за допомогою black

## Завдання 2: SOLID принципи

Реалізує систему керування бібліотекою книг з дотриманням всіх принципів SOLID:

### SOLID принципи:
1. **SRP** (Single Responsibility Principle) - клас `Book` відповідає тільки за представлення книги
2. **OCP** (Open/Closed Principle) - клас `Library` можна розширювати без модифікації
3. **LSP** (Liskov Substitution Principle) - будь-яка реалізація `LibraryInterface` може замінити `Library`
4. **ISP** (Interface Segregation Principle) - `LibraryInterface` містить тільки необхідні методи
5. **DIP** (Dependency Inversion Principle) - `LibraryManager` залежить від абстракції, а не від конкретної реалізації

### Основні компоненти:
- `Book` - модель книги
- `LibraryInterface` - інтерфейс бібліотеки
- `Library` - основна реалізація бібліотеки
- `LibraryManager` - менеджер для керування бібліотекою

## Форматування коду

Для форматування використовується black:
```bash
poetry run black .
```

## Перевірка типів

Для перевірки типізації використовується mypy:
```bash
poetry run mypy .
```

## Логування

Всі програми використовують модуль `logging` замість `print` для виведення інформації. Логування налаштовано на рівень INFO з форматом, що включає час, рівень та повідомлення.

## Автор

Serhii Palamarchuk

## Ліцензія

Цей проект ліцензований під умовами MIT License.
Тема 1. Python Development
