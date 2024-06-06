import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_records():
    return [

        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},

    ]


def test_filter_by_state(sample_records):
    executed_records = filter_by_state(sample_records)
    assert len(executed_records) == 2
    for record in executed_records:

        assert record["state"] == "EXECUTED"

    canceled_records = filter_by_state(sample_records, "CANCELED")
    assert len(canceled_records) == 2
    for record in canceled_records:
        assert record["state"] == "CANCELED"


@pytest.mark.parametrize("descending, expected_first_id", [(True, 41428829), (False, 939719570)])
def test_sort_by_date(sample_records, descending, expected_first_id):
    sorted_records = sort_by_date(sample_records, descending)
    assert sorted_records[0]["id"] == expected_first_id


@pytest.mark.parametrize("descending, expected_first_id", [
    (True, 41428829),
    (False, 939719570)
])

