import random
import string
from datetime import datetime


def generate_card_number():
    return ''.join(random.choices(string.digits, k=16))


def filter_by_currency(transactions, currency_code):
    return [transaction for transaction in transactions if transaction['currency'] == currency_code]


def generate_transaction():
    return {
        'id': random.randint(1000, 9999),
        'amount': random.uniform(1.0, 1000.0),
        'currency': random.choice(['USD', 'EUR', 'RUB']),
        'date': datetime.now().isoformat()
    }
