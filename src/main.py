import json
import csv
import pandas as pd
import re
import os


def filter_transactions_by_description(transactions, search_string):
    """
    Фильтрует список транзакций по заданной строке в описании.

    :param transactions: Список словарей с данными о транзакциях
    :param search_string: Строка для поиска в описаниях транзакций
    :return: Отфильтрованный список транзакций
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def count_transactions_by_category(transactions, categories):
    """
    Подсчитывает количество транзакций в каждой категории.

    :param transactions: Список словарей с данными о транзакциях
    :param categories: Список категорий для подсчета
    :return: Словарь с количеством транзакций в каждой категории
    """
    category_counts = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
    return category_counts


def find_file(extension, directory):
    """
    Ищет файл с указанным расширением в заданной директории.

    :param extension: Расширение файла для поиска
    :param directory: Директория для поиска файла
    :return: Путь к найденному файлу или None, если файл не найден
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                return os.path.join(root, file)
    return None


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта меню: ").strip()

    transactions = []
    data_directory = 'C:\\Users\\aptik\\Desktop\\Parser_project\\bankoperation\\data'  # Укажите путь к вашей директории данных

    if choice == '1':
        print("Для обработки выбран JSON-файл.")
        file_path = find_file('.json', data_directory)
        if not file_path:
            print("JSON-файл не найден.")
            return
        with open(file_path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
    elif choice == '2':
        print("Для обработки выбран CSV-файл.")
        file_path = find_file('.csv', data_directory)
        if not file_path:
            print("CSV-файл не найден.")
            return
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            transactions = [row for row in reader]
    elif choice == '3':
        print("Для обработки выбран XLSX-файл.")
        file_path = find_file('.xlsx', data_directory)
        if not file_path:
            print("XLSX-файл не найден.")
            return
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient='records')
    else:
        print("Неверный ввод. Завершение программы.")
        return

    print("Первые несколько транзакций для проверки:")
    for transaction in transactions[:5]:
        print(transaction)

    status_options = ['EXECUTED', 'CANCELED', 'PENDING']

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").strip().upper()
        if status in status_options:
            break
        print(f"Статус операции '{status}' недоступен.")

    filtered_transactions = [t for t in transactions if t.get('status', '').upper() == status]
    print(f"Операции отфильтрованы по статусу '{status}'")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == 'да':
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = sort_order != 'по возрастанию'
        filtered_transactions.sort(key=lambda x: x.get('date', ''), reverse=reverse)

    rubles_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rubles_choice == 'да':
        filtered_transactions = [t for t in filtered_transactions if 'руб' in t.get('amount', '')]

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search_choice == 'да':
        search_string = input("Введите строку для поиска в описаниях транзакций: ").strip()
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(transaction)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
