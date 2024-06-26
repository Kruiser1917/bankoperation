import pytest

from src.generators import filter_by_currency, generate_card_number, generate_transaction


@pytest.fixture
def transactions():
    return [
        generate_transaction() for _ in range(10)
    ]


def test_generate_transaction():
    transaction = generate_transaction()
    assert 'id' in transaction
    assert 'amount' in transaction
    assert 'currency' in transaction
    assert 'date' in transaction


def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, 'USD')
    for transaction in usd_transactions:
        assert transaction['currency'] == 'USD'


def test_card_number_generator():
    card_number = generate_card_number()
    assert len(card_number) == 16
    assert card_number.isdigit()
