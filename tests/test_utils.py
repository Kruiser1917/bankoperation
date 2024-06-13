import json
from unittest.mock import patch, mock_open

from src.utils import read_transactions_from_json


def test_read_transactions_from_json():
    mock_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "operationAmount": {"amount": "1000", "currency": {"code": "USD"}}
        }
    ]

    mock_file_data = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        result = read_transactions_from_json("dummy_path")
        assert result == mock_data

    with patch("builtins.open", mock_open(read_data="{}")):
        result = read_transactions_from_json("dummy_path")
        assert result == []

    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_transactions_from_json("dummy_path")
        assert result == []
