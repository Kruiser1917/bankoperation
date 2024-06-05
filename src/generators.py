from typing import Dict, Generator, List


def filter_by_currency(transactions, currency):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Генерирует описания операций.

    Args:
        transactions (List[Dict]): Список операций.

    Yields:
        str: Описание операции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


# src/generators.py


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start (int): Начальный номер.
        end (int): Конечный номер.

    Yields:
        str: Номер банковской карты в формате 'XXXX XXXX XXXX XXXX'.
    """
    for num in range(start, end + 1):
        card_number = f"{num:016}"
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number
