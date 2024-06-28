import json
import os
import pandas as pd

from src.logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path)

def read_transactions_from_json(file_path):
    try:
        logger.info('Чтение файла JSON')
        with open(file_path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON из файла: {file_path}")
    return None

def read_transactions_from_csv(file_path):
    try:
        logger.info('Чтение файла CSV')
        transactions = pd.read_csv(file_path).to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
    except pd.errors.EmptyDataError:
        logger.error(f"Ошибка чтения CSV файла: {file_path}")
    return None

def read_transactions_from_excel(file_path):
    try:
        logger.info('Чтение файла XLSX')
        transactions = pd.read_excel(file_path).to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
    except ValueError as e:
        logger.error(f"Ошибка чтения XLSX файла: {file_path} - {e}")
    return None
