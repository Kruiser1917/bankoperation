import pytest
from src.widget import universal_masking


def test_universal_masking():
    # Test for card number
    assert universal_masking("1234567812345678") == "1234 56** **** 5678"

    # Test for account number
    assert universal_masking("12345678901234567890") == "****************7890"

    # Test for invalid length
    with pytest.raises(ValueError):
        universal_masking("123")
