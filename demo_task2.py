"""
Приклад автоматичного тестування другого завдання
"""

import logging
from task2 import Library, LibraryManager

# Налаштування логування для тестів
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def test_task2_demo() -> None:
    """Демонстрація роботи системи бібліотеки"""
    logger.info("=== Демонстрація системи бібліотеки ===")

    # Створення бібліотеки та менеджера
    library = Library()
    manager = LibraryManager(library)

    # Додавання книг
    logger.info("\n--- Додавання книг ---")
    manager.add_book("1984", "George Orwell", "1949")
    manager.add_book("Brave New World", "Aldous Huxley", "1932")
    manager.add_book("Fahrenheit 451", "Ray Bradbury", "1953")

    # Показ всіх книг
    logger.info("\n--- Всі книги в бібліотеці ---")
    manager.show_books()

    # Видалення книги
    logger.info("\n--- Видалення книги ---")
    manager.remove_book("Brave New World")

    # Показ книг після видалення
    logger.info("\n--- Книги після видалення ---")
    manager.show_books()

    # Спроба видалити неіснуючу книгу
    logger.info("\n--- Спроба видалити неіснуючу книгу ---")
    manager.remove_book("Nonexistent Book")

    # Тестування валідації
    logger.info("\n--- Тестування валідації ---")
    manager.add_book("", "Author", "2023")  # Порожня назва
    manager.add_book("Title", "", "2023")  # Порожній автор
    manager.remove_book("")  # Порожня назва для видалення

    logger.info("\n=== Демонстрація завершена ===")


if __name__ == "__main__":
    test_task2_demo()
