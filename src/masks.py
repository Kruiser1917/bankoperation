import logging

# Настройка логирования для модуля masks
logger = logging.getLogger(__name__)
handler = logging.FileHandler('logs/masks.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.ERROR)

def mask_card_number(card_number):
    """
    Маскирует номер карты, оставляя первые 4 и последние 4 цифры открытыми.
    Если номер карты не состоит из 16 цифр, возвращается сообщение об ошибке.

    :param card_number: Номер карты
    :return: Маскированный номер карты или сообщение об ошибке
    """
    if len(card_number) != 16:
        logger.error("Card number must be exactly 16 digits long")
        return "Invalid card number"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

def mask_account_number(account_number):
    """
    Маскирует номер счета, оставляя последние 4 цифры открытыми.
    Если номер счета не состоит из нужного количества цифр, возвращается сообщение об ошибке.

    :param account_number: Номер счета
    :return: Маскированный номер счета или сообщение об ошибке
    """
    if len(account_number) < 8:
        logger.error("Account number must be at least 8 digits long")
        return "Invalid account number"
    return f"{account_number[:-4]}**{account_number[-4:]}"

# Добавьте другие функции модуля masks, если они есть, с соответствующей настройкой логирования
