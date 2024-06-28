# Banking Operations Widget

Этот проект представляет собой виджет для обработки клиентских банковских операций. 
Виджет предоставляет функции для фильтрации и сортировки банковских транзакций по их состоянию и дате.


## Описание
Этот проект предназначен для обработки и анализа финансовых транзакций. Включает в себя различные функции для маскировки данных, фильтрации и сортировки транзакций, а также генерации номеров карт.

## Функциональность

### Маскирование Данных
Функции для маскировки номеров карт и счетов:
- `mask_card_number`
- `mask_account_number`
- `universal_masking`

### Обработка и Анализ Транзакций
Функции для фильтрации и сортировки транзакций:
- `filter_by_state`
- `sort_by_date`

### Генераторы
Генераторы для работы с массивами транзакций:
- `filter_by_currency`
- `transaction_descriptions`
- `card_number_generator`

### Логирование
Логирование осуществляется с использованием библиотеки `logging`. Логи записываются в файлы, расположенные в папке `logs` в корне проекта. Каждый модуль имеет свой отдельный логер.

#### Примеры Логеров
- Логер для модуля `masks` записывает логи в файл `logs/masks.log`.
- Логер для модуля `widget` записывает логи в файл `logs/widget.log`.

Формат записи лога:

## Установка зависимостей

Для установки зависимостей используйте Poetry:

```bash
poetry install
```
## Тестирование

Проект покрыт тестами с использованием библиотеки `pytest`. Для запуска тестов выполните команду:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

## Новые функции

### Генераторы для обработки транзакций

#### filter_by_currency


Маскирует номер карты или счета.
=======
for _ in range(3):

    print(next(usd_transactions)["id"])

## Декораторы

### log

Декоратор `log` логирует вызовы функции и их результаты. Логи могут записываться в файл или выводиться в консоль.

### Примеры Использования
Примеры использования функций и декораторов приведены в модуле `main.py`.

## Установка и Запуск
1. Установите необходимые зависимости с помощью Poetry:
    ```bash
    poetry install
    ```

2. Запустите скрипт:
    ```bash
    poetry run python src/main.py
    ```

## Тестирование
Проект включает в себя тесты, которые можно запустить с помощью команды:
```bash
poetry run pytest --cov=src --cov-report=term-missing
```


## Функции

Возвращает описания каждой транзакции по очереди.
card_number_generator(start: int, end: int) -> Iterator[str]

Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
processing.py
filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]

Фильтрует транзакции по состоянию.
sort_by_date(transactions: List[Dict[str, Any]], order: bool = True) -> List[Dict[str, Any]]

Сортирует транзакции по дате.
widget.py
format_datetime_to_date(datetime_str: str) -> str

Форматирует строку даты и времени в формат даты.
universal_masking(input_str: str) -> str

## Новый функционал

Проект теперь поддерживает считывание данных о финансовых транзакциях из файлов форматов CSV и XLSX. 

### Как использовать

Для запуска скрипта с использованием файла JSON:
```bash
python src/main.py data/transactions.json
```
