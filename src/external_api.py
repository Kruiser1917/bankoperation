import os
from typing import Dict

import requests


def get_exchange_rate(currency: str) -> float:
    """Gets the exchange rate from the API."""
    api_key = os.getenv('EXCHANGE_API_KEY')
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={currency}&base=RUB"
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200 and currency in data["rates"]:
        return data["rates"][currency]
    else:
        return 1.0  # Default to 1 if API call fails


def convert_to_rub(transaction: Dict) -> float:
    """Converts transaction amount to RUB."""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(amount)
    else:
        exchange_rate = get_exchange_rate(currency)
        return float(amount) * exchange_rate
