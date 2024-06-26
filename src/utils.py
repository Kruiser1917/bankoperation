import json
import os

from src.logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path)


def read_transactions_from_json(file_path):
    try:
        logger.info('чтение файла file.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from file: {file_path}")
    return None
