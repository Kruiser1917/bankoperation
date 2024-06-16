def filter_by_state(records, state="EXECUTED"):
    return [record for record in records if record["state"] == state]


def sort_by_date(records, descending=True):
    return sorted(records, key=lambda x: x['date'], reverse=descending)
