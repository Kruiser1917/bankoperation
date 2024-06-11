# tests/test_widget.py

import pytest


from src.widget import format_datetime_to_date, universal_masking



def test_format_datetime_to_date():
    assert format_datetime_to_date("2018-07-11T02:26:18.671407") == "11.07.2018"



def test_universal_masking():
    result = universal_masking("Visa Platinum 1234567812345678")
    print(f"Result: '{result}'")
    assert result == "Visa Platinum 1234 56** **** 5678"

def test_universal_masking():
    result = universal_masking('Visa Platinum 1234567812345678')
    print(f"Result: '{result}'")
    assert result == 'Visa Platinum 1234 56** **** 5678'

