import os
import pytest
from src.utils import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_excel


@pytest.fixture
def json_file_path():
    return os.path.join(os.path.dirname(__file__), 'test_data', 'test_transactions.json')


@pytest.fixture
def csv_file_path():
    return os.path.join(os.path.dirname(__file__), 'test_data', 'test_transactions.csv')


@pytest.fixture
def excel_file_path():
    return os.path.join(os.path.dirname(__file__), 'test_data', 'test_transactions.xlsx')


def test_read_transactions_from_json(json_file_path):
    transactions = read_transactions_from_json(json_file_path)
    assert transactions is not None
    assert len(transactions) > 0
    assert isinstance(transactions, list)


def test_read_transactions_from_csv(csv_file_path):
    transactions = read_transactions_from_csv(csv_file_path)
    assert transactions is not None
    assert len(transactions) > 0
    assert isinstance(transactions, list)


def test_read_transactions_from_excel(excel_file_path):
    transactions = read_transactions_from_excel(excel_file_path)
    assert transactions is not None
    assert len(transactions) > 0
    assert isinstance(transactions, list)
