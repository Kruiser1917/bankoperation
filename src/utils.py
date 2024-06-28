import json
import os

import pandas as pd

from src.logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path)


def read_transactions_from_json(file_path):
    """
    Читает финансовые транзакции из JSON-файла.

    Args:
        file_path (str): Путь к JSON-файлу.

    Returns:
        list: Список транзакций, если файл успешно прочитан и распознан.
        None: Если произошла ошибка при чтении или парсинге файла.
    """
    try:
        logger.info('Чтение файла JSON')
        with open(file_path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from file: {file_path}")
    return None


def read_transactions_from_csv(file_path):
    """
    Читает финансовые транзакции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        list: Список транзакций, если файл успешно прочитан.
        None: Если произошла ошибка при чтении файла.
    """
    try:
        logger.info('Чтение файла CSV')
        transactions = pd.read_csv(file_path).to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        logger.error(f"No data: {file_path}")
    return None


def read_transactions_from_excel(file_path):
    """
    Читает финансовые транзакции из XLSX-файла.

    Args:
        file_path (str): Путь к XLSX-файлу.

    Returns:
        list: Список транзакций, если файл успешно прочитан.
        None: Если произошла ошибка при чтении файла.
    """
    try:
        logger.info('Чтение файла XLSX')
        transactions = pd.read_excel(file_path).to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        logger.error(f"No data: {file_path}")
    return None
