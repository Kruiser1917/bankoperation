from typing import List, Dict, Generator


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]:
    """
    Генератор, фильтрующий транзакции по указанной валюте.
    :param transactions: Список транзакций
    :param currency: Валюта для фильтрации
    :return: Генератор транзакций с указанной валютой
    """
    for transaction in transactions:
        if 'operationAmount' in transaction and 'currency' in transaction['operationAmount']:
            if transaction['operationAmount']['currency']['code'] == currency:
                yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Генератор, возвращающий описание каждой транзакции.
    :param transactions: Список транзакций
    :return: Генератор описаний транзакций
    """
    for transaction in transactions:
        if 'description' in transaction:
            yield transaction['description']


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    :param start: Начальный номер
    :param end: Конечный номер
    :return: Генератор номеров карт
    """
    for num in range(start, end + 1):
        card_number = f"{num:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
