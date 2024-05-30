# Модуль widget с функцией для обработки входных данных и применения маскировки
from src.masks import mask_account_number
from src.masks import mask_card_number


def universal_masking(input_data: str) -> str:
    """
    Маскирует номер кредитной карты или счета в зависимости от входных данных.

    Args:
        input_data (str): Входная строка с типом и номером (например, "Visa 1234567890123456").

    Returns:
        str: Исходная строка с маскированным номером.
    """

    parts = input_data.split()
    if parts[0] == "Счет":
        account_number = parts[-1]
        masked_number = mask_account_number(account_number)
        return f"{' '.join(parts[:-1])} {masked_number}"
    else:
        card_number = "".join(parts[-4:])
        if len(card_number) == 16:
            masked_number = mask_card_number(card_number)
            return f"{' '.join(parts[:-4])} {masked_number[:4]} {masked_number[5:7]}{masked_number[7:9]} {masked_number[10:14]} {masked_number[15:]}"
        else:
            return f"{' '.join(parts[:-4])} Card number must be exactly 16 digits long"


# Функция для преобразования строки с датой и временем в формате
# ISO в строку даты в формате DD.MM.YYYY


def format_datetime_to_date(datetime_str: str) -> str:
    """
    Преобразует строку с датой и временем в формате ISO в строку даты в формате DD.MM.YYYY.

    Args:
    datetime_str (str): Строка даты и времени в формате ISO, например, "2018-07-11T02:26:18.671407".

    Returns:
    str: Строка даты в формате DD.MM.YYYY.
    """
    # Извлекаем часть с датой из строки даты и времени
    date_part = datetime_str.split("T")[0]
    # Разделяем дату на год, месяц и день
    year, month, day = date_part.split("-")
    # Форматируем дату в формат DD.MM.YYYY
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date


print(format_datetime_to_date("2018-07-11T02:26:18.671407"))

# Примеры для тестирования
test_inputs = [
    "Visa Platinum 7000 7922 8960 6361",
    "Maestro 1596 8378 6870 5199",
    "Счет 73654108430135874305",
    "MasterCard 7158 3007 3472 6758",
    "Счет 35383033474447895560",
    "Visa Classic 6831 9824 7673 7658",
]

for test_input in test_inputs:
    print(universal_masking(test_input))
