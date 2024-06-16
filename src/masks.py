import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('logs/masks.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def mask_card_number(card_number):
    if len(card_number) != 16 or not card_number.isdigit():
        logger.error("Card number must be exactly 16 digits long")
        raise ValueError("Card number must be exactly 16 digits long")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number):
    if len(account_number) < 6 or not account_number.isdigit():
        logger.error("Account number must be at least 6 digits long")
        raise ValueError("Account number must be at least 6 digits long")
    return f"{'*' * (len(account_number) - 4)}{account_number[-4:]}"
