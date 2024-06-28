import logging
import sys
from datetime import datetime

from src.masks import mask_account_number, mask_card_number
from src.utils import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_excel
from src.widget import format_datetime_to_date

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def sort_by_date(transactions, descending=True):
    """
    Сортирует транзакции по дате.

    Args:
        transactions (list): Список транзакций.
        descending (bool): Если True, сортировка будет в порядке убывания.

    Returns:
        list: Отсортированный список транзакций.
    """
    transactions_with_date = []
    for transaction in transactions:
        try:
            if isinstance(transaction['date'], str):
                transaction['date'] = datetime.fromisoformat(transaction['date'])
            transactions_with_date.append(transaction)
        except (KeyError, ValueError) as e:
            logger.error(f"Error parsing date in transaction: {e}")
    return sorted(transactions_with_date, key=lambda x: x['date'], reverse=descending)


def main(file_path):
    """
    Основная функция для запуска скрипта.

    Args:
        file_path (str): Путь к файлу с транзакциями.

    Returns:
        None
    """
    if file_path.endswith('.json'):
        transactions = read_transactions_from_json(file_path)
    elif file_path.endswith('.csv'):
        transactions = read_transactions_from_csv(file_path)
    elif file_path.endswith('.xlsx'):
        transactions = read_transactions_from_excel(file_path)
    else:
        logger.error("Unsupported file format")
        return

    for transaction in transactions:
        logger.info(format_datetime_to_date(transaction['date']))
        if 'card' in transaction:
            try:
                logger.info(mask_card_number(transaction['card']))
            except ValueError as e:
                logger.error(e)
        if 'account' in transaction:
            try:
                logger.info(mask_account_number(transaction['account']))
            except ValueError as e:
                logger.error(e)

    sorted_transactions = sort_by_date(transactions)
    print(sorted_transactions)
    mask_card = mask_card_number('1234567890123456')
    print(mask_card)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python main.py <path_to_transactions_file>")
    else:
        main(sys.argv[1])
