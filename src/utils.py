import json
import os
import pandas as pd
import logging


def setup_logger(name, log_file, level=logging.INFO):
    """Set up a logger."""
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path)


def read_transactions_from_json(file_path):
    """Read transactions from a JSON file."""
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
    """Read transactions from a CSV file."""
    try:
        logger.info('Чтение файла CSV')
        transactions = pd.read_csv(file_path).to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        logger.error(f"Error reading CSV file: {file_path}")
    return None


def read_transactions_from_excel(file_path):
    """Read transactions from an Excel file."""
    try:
        logger.info('Чтение файла XLSX')
        transactions = pd.read_excel(file_path).to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        logger.error(f"Error reading Excel file: {file_path}")
    return None
