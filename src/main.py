import logging
import sys
from datetime import datetime

from src.masks import mask_account_number, mask_card_number
from src.utils import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_excel
from src.widget import format_datetime_to_date

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def sort_by_date(transactions, descending=True):
    transactions_with_date = []
    for t in transactions:
        date_value = t.get('date')
        if date_value:
            if isinstance(date_value, (float, int)):
                # Если дата представлена числом, преобразуем её в строку
                date_str = str(date_value)
                try:
                    date_obj = datetime.fromisoformat(date_str)
                    t['date'] = date_obj.isoformat()
                except ValueError:
                    logger.error(f"Invalid date format: {date_value}")
            elif isinstance(date_value, str):
                try:
                    date_obj = datetime.fromisoformat(date_value)
                    t['date'] = date_obj.isoformat()
                except ValueError:
                    logger.error(f"Invalid date format: {date_value}")
            transactions_with_date.append(t)
    return sorted(transactions_with_date, key=lambda x: x['date'], reverse=descending)


def main(file_path):
    if file_path.endswith('.json'):
        transactions = read_transactions_from_json(file_path)
    elif file_path.endswith('.csv'):
        transactions = read_transactions_from_csv(file_path)
    elif file_path.endswith('.xlsx'):
        transactions = read_transactions_from_excel(file_path)
    else:
        logger.error("Unsupported file format")
        return

    if transactions is None:
        logger.error("No transactions found")
        return

    for transaction in transactions:
        date_value = transaction.get('date')
        if date_value is not None:
            if isinstance(date_value, str):
                try:
                    logger.info(format_datetime_to_date(date_value))
                except ValueError as e:
                    logger.error(f"Invalid date format in transaction: {date_value} - {e}")
            else:
                logger.error(f"Invalid date format: {date_value}")

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

    # Сортировка транзакций по дате
    sorted_transactions = sort_by_date(transactions)
    print(sorted_transactions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python main.py <path_to_transactions_file>")
    else:
        main(sys.argv[1])
