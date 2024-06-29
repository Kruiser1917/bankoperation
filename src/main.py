import logging
import sys

from filters import filter_transactions_by_keyword, categorize_transactions
from utils import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_excel
from widget import format_datetime_to_date

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def sort_by_date(transactions, descending=True):
    """Sort transactions by date."""
    transactions_with_date = [t for t in transactions if 'date' in t]
    return sorted(transactions_with_date, key=lambda x: x['date'], reverse=descending)


def main(file_path):
    """
    Main function to interact with the user and process transactions.

    :param file_path: Path to the file with transactions
    """
    if file_path.endswith('.json'):
        transactions = read_transactions_from_json(file_path)
    elif file_path.endswith('.csv'):
        transactions = read_transactions_from_csv(file_path)
    elif file_path.endswith('.xlsx'):
        transactions = read_transactions_from_excel(file_path)
    else:
        logger.error("Unsupported file format. Please use JSON, CSV, or XLSX.")
        return

    if not transactions:
        logger.error("No transactions found.")
        return

    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").upper()
    filtered_transactions = [t for t in transactions if t.get('state', '').upper() == status]

    if not filtered_transactions:
        logger.error(f"Статус операции '{status}' недоступен.")
        return

    sort_choice = input("Отсортировать операции по дате? (Да/Нет): ").lower()
    if sort_choice == 'да':
        order_choice = input("Отсортировать по возрастанию или по убыванию?: ").lower()
        descending = order_choice == 'по убыванию'
        filtered_transactions = sort_by_date(filtered_transactions, descending)

    currency_choice = input("Выводить только рублевые транзакции? (Да/Нет): ").lower()
    if currency_choice == 'да':
        filtered_transactions = [t for t in filtered_transactions if t.get('amount', '').endswith('руб.')]

    keyword_choice = input("Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").lower()
    if keyword_choice == 'да':
        keyword = input("Введите слово для фильтрации: ")
        filtered_transactions = filter_transactions_by_keyword(filtered_transactions, keyword)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{format_datetime_to_date(transaction['date'])} {transaction.get('description', '')}")
            if 'card' in transaction:
                print(f"Счет {transaction['card']}")
            if 'amount' in transaction:
                print(f"Сумма: {transaction['amount']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python main.py <path_to_transactions_file>")
    else:
        main(sys.argv[1])
