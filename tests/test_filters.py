import pytest
from src.filters import filter_transactions_by_keyword, categorize_transactions

@pytest.fixture
def sample_transactions():
    return [
        {"description": "Оплата услуг", "amount": "1000 руб."},
        {"description": "Перевод на карту", "amount": "2000 руб."},
        {"description": "Оплата товаров", "amount": "3000 руб."},
        {"description": "Пополнение счета", "amount": "4000 руб."}
    ]

def test_filter_transactions_by_keyword(sample_transactions):
    filtered = filter_transactions_by_keyword(sample_transactions, "оплата")
    assert len(filtered) == 2

def test_categorize_transactions(sample_transactions):
    categories = ["услуги", "товаров", "счета"]
    categorized = categorize_transactions(sample_transactions, categories)
    print(f"Categorized: {categorized}")  # Отладочный вывод
    assert categorized["услуги"] == 1
    assert categorized["товаров"] == 1
    assert categorized["счета"] == 1
