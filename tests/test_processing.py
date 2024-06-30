import pytest
from src.processing import filter_by_state

@pytest.fixture
def sample_records():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 41428830, 'state': 'PENDING', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-23T13:45:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

def test_filter_by_state(sample_records):
    executed_records = filter_by_state(sample_records, "EXECUTED")
    assert len(executed_records) == 1
    assert executed_records[0]["state"] == "EXECUTED"
