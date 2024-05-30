# src/processing.py

from typing import List, Dict


def filter_by_state(records: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
    records (List[Dict]): Список словарей.
    state (str, optional): Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
    List[Dict]: Новый список, содержащий только словари с указанным значением 'state'.
    """
    return [record for record in records if record.get('state') == state]


def sort_by_date(records: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    Args:
    records (List[Dict]): Список словарей.
    descending (bool, optional): Порядок сортировки. True для убывания, False для возрастания. По умолчанию True.

    Returns:
    List[Dict]: Новый список, отсортированный по ключу 'date'.
    """
    return sorted(records, key=lambda x: x['date'], reverse=descending)
