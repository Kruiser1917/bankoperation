# src/decorators.py

import functools
import logging
import sys  # Добавляем импорт sys
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций и их результатов.

    Args:
        filename (Optional[str]): Имя файла для логов. Если не задано, логи выводятся в консоль.

    Returns:
        Callable: Декорированная функция.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()

    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(handler)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                print(f"{func.__name__} ok")  # Печатаем в stdout
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}", file=sys.stderr)  # Печатаем в stderr
                logger.error(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator
