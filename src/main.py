import logging

from src.masks import mask_account_number, mask_card_number
from src.utils import read_transactions_from_json
from src.widget import format_datetime_to_date

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def sort_by_date(transactions, descending=True):
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)


if __name__ == "__main__":
    file_path = '../data/operations.json'
    transactions = read_transactions_from_json(file_path)

    # Примеры вызовов функций
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

    # Сортировка транзакций по дате
    sorted_transactions = sort_by_date(transactions)
    print(sorted_transactions)
    mask_card = mask_card_number('1234567890123456')
    print(mask_card)
