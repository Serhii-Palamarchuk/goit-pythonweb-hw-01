"""
Завдання 2: SOLID принципи
Реалізація системи керування бібліотекою книг з дотриманням SOLID принципів
"""

from abc import ABC, abstractmethod
from typing import List

from logger import get_logger

# Отримуємо логер для цього модуля
logger = get_logger(__name__)


class Book:
    """Клас для представлення книги (SRP - єдина відповідальність)"""

    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.title == other.title


class LibraryInterface(ABC):
    """Інтерфейс для бібліотеки (ISP - розділення інтерфейсів)"""

    @abstractmethod
    def add_book(self, title: str, author: str, year: str) -> None:
        """Додає книгу до бібліотеки"""

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        """Видаляє книгу з бібліотеки. Повертає True якщо видалення успішне"""

    @abstractmethod
    def show_books(self) -> None:
        """Відображає всі книги в бібліотеці"""

    @abstractmethod
    def get_books(self) -> List[Book]:
        """Повертає список всіх книг"""


class Library(LibraryInterface):
    """
    Основна реалізація бібліотеки (OCP - відкритість/закритість, LSP - підстановка Лісков)
    """

    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, title: str, author: str, year: str) -> None:
        """Додає книгу до бібліотеки"""
        book = Book(title, author, year)
        self._books.append(book)
        logger.info("Додано книгу: %s", book)

    def remove_book(self, title: str) -> bool:
        """Видаляє книгу з бібліотеки"""
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                logger.info("Видалено книгу: %s", book)
                return True
        logger.warning("Книгу з назвою '%s' не знайдено", title)
        return False

    def show_books(self) -> None:
        """Відображає всі книги в бібліотеці"""
        if not self._books:
            logger.info("Бібліотека порожня")
            return

        logger.info("Книги в бібліотеці:")
        for book in self._books:
            logger.info("  %s", book)

    def get_books(self) -> List[Book]:
        """Повертає список всіх книг"""
        return self._books.copy()


class LibraryManager:
    """
    Менеджер для керування бібліотекою (DIP - інверсія залежностей)
    Залежить від абстракції (LibraryInterface), а не від конкретної реалізації
    """

    def __init__(self, library: LibraryInterface) -> None:
        self._library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        """Додає книгу через бібліотеку"""
        if not title.strip() or not author.strip() or not year.strip():
            logger.error("Всі поля (назва, автор, рік) повинні бути заповнені")
            return
        self._library.add_book(title.strip(), author.strip(), year.strip())

    def remove_book(self, title: str) -> None:
        """Видаляє книгу через бібліотеку"""
        if not title.strip():
            logger.error("Назва книги не може бути порожньою")
            return
        self._library.remove_book(title.strip())

    def show_books(self) -> None:
        """Відображає книги через бібліотеку"""
        self._library.show_books()


def main() -> None:
    """Головна функція програми"""
    library = Library()
    manager = LibraryManager(library)

    logger.info("=== Система керування бібліотекою ===")
    logger.info("Доступні команди: add, remove, show, exit")

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            logger.info("Програма завершена")
            break
        else:
            logger.error("Невірна команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
