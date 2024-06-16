from src.masks import mask_card_number


def universal_masking(value):
    if len(value) == 16:
        return mask_card_number(value)
    elif len(value) >= 20:
        return '*' * (len(value) - 4) + value[-4:]
    else:
        raise ValueError("Invalid length for masking")


def format_datetime_to_date(datetime_str):
    from datetime import datetime
    date_obj = datetime.fromisoformat(datetime_str)
    return date_obj.strftime("%d.%m.%Y")
