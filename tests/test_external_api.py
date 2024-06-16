from unittest.mock import patch

from src.external_api import convert_to_rub, get_exchange_rate


@patch("src.external_api.requests.get")
def test_get_exchange_rate(mock_get):
    mock_response = {
        "rates": {
            "USD": 0.013
        }
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    assert get_exchange_rate("USD") == 0.013

    mock_get.return_value.status_code = 400
    assert get_exchange_rate("USD") == 1.0


def test_convert_to_rub():
    transaction_usd = {
        "operationAmount": {"amount": "1000", "currency": {"code": "USD"}}
    }

    with patch("src.external_api.get_exchange_rate", return_value=0.013):
        assert convert_to_rub(transaction_usd) == 13.0

    transaction_rub = {
        "operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}
    }
    assert convert_to_rub(transaction_rub) == 1000.0
