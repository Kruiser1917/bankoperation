import logging
from src.utils import read_transactions_from_json
from src.masks import mask_card_number, mask_account_number
from src.widget import format_datetime_to_date, universal_masking

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def sort_by_date(transactions, descending=True):
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)

if __name__ == "__main__":
    transactions = read_transactions_from_json()

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
    sorted_transactions = sort_by_date(transactions, descending=True)
    logger.info(sorted_transactions)
