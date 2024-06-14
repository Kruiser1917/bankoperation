from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует транзакции по состоянию.
    :param transactions: Список транзакций
    :param state: Состояние транзакций для фильтрации (по умолчанию "EXECUTED")
    :return: Отфильтрованный список транзакций
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: List[Dict], ascending: bool = False) -> List[Dict]:
    """
    Сортирует транзакции по дате.
    :param transactions: Список транзакций
    :param ascending: Сортировка в порядке возрастания (по умолчанию False)
    :return: Отсортированный список транзакций
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=not ascending)
