import logging
import os

# Создаем директорию logs, если она не существует
os.makedirs('logs', exist_ok=True)

# Настройка логера
logger = logging.getLogger(__name__)
handler = logging.FileHandler('logs/masks.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def universal_masking(account: str) -> str:
    """Маскирование номера счета или карты."""
    logger.info(f'Маскирование аккаунта: {account}')
    if account.startswith('Счет'):
        masked = f'{account[:5]}**{account[-4:]}'
    elif len(account.split()) == 2 and account.split()[0] in ['Visa', 'MasterCard']:
        masked = f'{account.split()[0]} {account.split()[1][:4]} {account.split()[1][4:6]}** **** {account.split()[1][-4:]}'
    else:
        logger.warning(f'Неверный формат аккаунта: {account}')
        return "Card number must be exactly 16 digits long"
    logger.info(f'Замаскированный аккаунт: {masked}')
    return masked


def mask_card_number(card_number: str) -> str:
    """Маскирование номера карты."""
    logger.info(f'Маскирование номера карты: {card_number}')
    if len(card_number) != 16 or not card_number.isdigit():
        logger.warning(f'Неверный формат номера карты: {card_number}')
        return "Card number must be exactly 16 digits long"
    masked = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
    logger.info(f'Замаскированный номер карты: {masked}')
    return masked


def mask_account_number(account_number: str) -> str:
    """Маскирование номера счета."""
    logger.info(f'Маскирование номера счета: {account_number}')
    masked = f'{account_number[:5]}**{account_number[-4:]}'
    logger.info(f'Замаскированный номер счета: {masked}')
    return masked
