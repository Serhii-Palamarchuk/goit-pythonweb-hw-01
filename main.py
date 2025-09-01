"""
Головний модуль для запуску домашнього завдання GoIT Python Web HW-01
"""

import logging
import sys
from typing import NoReturn

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def run_task1() -> None:
    """Запуск першого завдання - Патерн Фабрика"""
    logger.info("Запуск завдання 1: Патерн Фабрика")
    try:
        import task1

        task1.main()
    except ImportError as e:
        logger.error("Не вдалося імпортувати task1: %s", e)
    except Exception as e:
        logger.error("Помилка при виконанні task1: %s", e)


def run_task2() -> None:
    """Запуск другого завдання - SOLID принципи"""
    logger.info("Запуск завдання 2: SOLID принципи")
    try:
        import task2

        task2.main()
    except ImportError as e:
        logger.error("Не вдалося імпортувати task2: %s", e)
    except Exception as e:
        logger.error("Помилка при виконанні task2: %s", e)


def show_menu() -> None:
    """Відображає меню вибору завдання"""
    print("\n" + "=" * 50)
    print("GoIT Python Web Development - Домашнє завдання 1")
    print("=" * 50)
    print("1. Завдання 1: Патерн Фабрика")
    print("2. Завдання 2: SOLID принципи")
    print("3. Вийти")
    print("=" * 50)


def main() -> NoReturn:
    """Головна функція програми"""
    logger.info("Запуск програми домашнього завдання")

    while True:
        show_menu()
        choice = input("Оберіть завдання (1-3): ").strip()

        if choice == "1":
            run_task1()
        elif choice == "2":
            run_task2()
        elif choice == "3":
            logger.info("Програма завершена")
            sys.exit(0)
        else:
            print("Невірний вибір. Будь ласка, оберіть 1, 2 або 3.")

        input("\nНатисніть Enter для продовження...")


if __name__ == "__main__":
    main()
