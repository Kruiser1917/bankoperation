import pytest


from src.masks import mask_account_number, mask_card_number


def test_mask_card_number():
    assert mask_card_number("1234567812345678") == "1234 56** **** 5678"
    with pytest.raises(ValueError):
        mask_card_number("1234")


def test_mask_account_number():
    assert mask_account_number("12345678") == "**5678"
    with pytest.raises(ValueError):
        mask_account_number("123")
=======
from src.masks import mask_card_number, mask_account_number


def test_mask_card_number():
    assert mask_card_number('1234567812345678') == '1234 56** **** 5678'
    with pytest.raises(ValueError):
        mask_card_number('1234')


def test_mask_account_number():
    assert mask_account_number('12345678') == '**5678'
    with pytest.raises(ValueError):
        mask_account_number('123')

