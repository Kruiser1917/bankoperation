from collections import Counter
import re

def filter_transactions_by_keyword(transactions, keyword):
    """
    Filter transactions by keyword in description.

    Args:
        transactions (list): List of transaction dictionaries.
        keyword (str): Keyword to search in transaction descriptions.

    Returns:
        list: List of filtered transactions.
    """
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]

def categorize_transactions(transactions, categories):
    category_counts = Counter()
    for transaction in transactions:
        description = transaction.get('description', '').lower()
        for category in categories:
            if re.search(re.escape(category), description):
                category_counts[category] += 1
                break
    return category_counts
