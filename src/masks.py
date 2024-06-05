# маскировки номеров карт и счетов


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, показывая только первые 6 и последние 4 цифры.

    Args:
    card_number (str): Номер кредитной карты для маскировки.

    Returns:
    str: Замаскированный номер кредитной карты в формате 'XXXX XX** **** XXXX'.
    """
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        raise ValueError("Invalid card number. Card number must have exactly 16 digits.")


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры.

    Аргументы:
    account_number (str): Номер счета, который будет замаскирован.

    Возвращает:
    str: Замаскированный номер счета в формате '**XXXX'.
    """
    # номер счета состоит только из цифр и имеет длину не менее 4 цифр
    if len(account_number) >= 4 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        raise ValueError("Неверный номер счета. Номер счета должен содержать минимум 4 цифры.")
