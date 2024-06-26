import os

from src.logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path)


def mask_card_number(card_number):
    if len(card_number) != 16 or not card_number.isdigit():
        logger.error("Card number must be exactly 16 digits long")
        raise ValueError("Card number must be exactly 16 digits long")
    logger.info('маскировки карты')
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number):
    if len(account_number) < 6 or not account_number.isdigit():
        logger.error("Account number must be at least 6 digits long")
        raise ValueError("Account number must be at least 6 digits long")
    logger.info('маскировка счета')
    return f"{'*' * (len(account_number) - 4)}{account_number[-4:]}"
