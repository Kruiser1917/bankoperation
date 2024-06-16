import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('logs/utils.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def read_transactions_from_json(filepath='data/transactions.json'):
    try:
        with open(filepath, 'r') as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from file: {filepath}")
    return None
