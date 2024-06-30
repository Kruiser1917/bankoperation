def filter_by_state(records, state):
    """
    Filter transactions by their state.

    Args:
        records (list): List of transaction records.
        state (str): State to filter by.

    Returns:
        list: Filtered list of transactions.
    """
    state = state.upper()
    filtered_records = [record for record in records if record.get('state', '').upper() == state]
    return filtered_records

def sort_by_date(records, descending=True):
    return sorted(records, key=lambda x: x['date'], reverse=descending)

def filter_by_currency():
    return None
