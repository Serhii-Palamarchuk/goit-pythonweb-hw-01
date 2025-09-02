"""
Централізований модуль для налаштування логування
Дотримання принципу DRY (Don't Repeat Yourself)
"""

import logging
import sys
from typing import Optional


def setup_logger(
    name: Optional[str] = None,
    level: int = logging.INFO,
    format_string: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
) -> logging.Logger:
    """
    Налаштовує та повертає логер з заданими параметрами

    Args:
        name: Ім'я логера (якщо None, буде використано root logger)
        level: Рівень логування
        format_string: Формат повідомлень логування

    Returns:
        Налаштований логер
    """
    logger = logging.getLogger(name)

    # Запобігаємо дублюванню обробників при повторному виклику
    if logger.handlers:
        return logger

    logger.setLevel(level)

    # Створюємо обробник для виведення в консоль
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    # Створюємо форматер
    formatter = logging.Formatter(format_string)
    handler.setFormatter(formatter)

    # Додаємо обробник до логера
    logger.addHandler(handler)

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Отримує логер для конкретного модуля

    Args:
        name: Ім'я модуля (зазвичай __name__)

    Returns:
        Логер для модуля
    """
    return setup_logger(name)


# Глобальний логер для випадків, коли потрібен швидкий доступ
default_logger = setup_logger("goit-hw01")
