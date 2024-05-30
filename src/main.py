import pprint
from typing import Union

from src.decorators import log
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.widget import format_datetime_to_date, universal_masking

# Список словарей для processing.py
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615004591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]

# Список словарей для generators.py
transactions1 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Номер операции",
        "from": "Cчет 75186830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:26:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Cчет 19768645243227258542",
        "to": "Счет 75651667583060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Cчет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 895515941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Номер операции",
        "from": "Visa Platinum 22427837705343588",
        "to": "Счет 14226426821044501587"
    }
]

# Маскирование счетов и карт
print(universal_masking("Visa Platinum 70087922890606361"))
print(universal_masking("Счет 73564108430153874305"))

# Форматирование даты
print(format_datetime_to_date("2018-07-11T02:26:18.671407"))

# Фильтрация по состоянию
pp = pprint.PrettyPrinter()
executed_transactions = filter_by_state(transactions)
pp.pprint(executed_transactions)

canceled_transactions = filter_by_state(transactions, state="CANCELED")
pp.pprint(canceled_transactions)

# Сортировка по дате
sorted_transactions = sort_by_date(transactions)
pp.pprint(sorted_transactions)

# Сортировка по дате в порядке возрастания
sorted_transactions = sort_by_date(transactions)
pp.pprint(sorted_transactions)

# Фильтрация по валюте
usd_transactions = filter_by_currency(transactions1, currency="USD")
for _ in range(3):
    print(next(usd_transactions)['id'])

# Описание транзакций
descriptions = transaction_descriptions(transactions1)
for i in range(5):
    print(next(descriptions))

# Генерация номеров карт
for card_number in card_number_generator(start=1, end=5):
    print(card_number)


# Примеры использования декоратора
@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Функция вызова декоратора с файлом сохранения 'mylog.txt'."""
    return x + y


my_function(1, 2)


@log(filename="mylog.txt")
def my_function_error(x: int, y: int) -> Union[int, float, None]:
    """Функция вызова декоратора с ошибкой и сохранением вывода в файл 'mylog.txt'."""
    return x / y


my_function_error(6, 5)


@log()
def my_function_log_not_filename(x: int, y: int) -> Union[int, float, None]:
    """Функция вызова декоратора без файла сохранения и вывод в консоль."""
    return x / y


my_function_log_not_filename(4, 2)


@log()
def my_function_log_not_filename_error(x: int, y: int) -> Union[int, float, None]:
    """Функция вызова декоратора с ошибкой без файла сохранения и вывод в консоль."""
    return x / y


my_function_log_not_filename_error(8, 3)
