import json
from typing import List, Dict, Any


def read_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Reads transactions from a JSON file and returns a list of dictionaries."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
