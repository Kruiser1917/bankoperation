from collections import defaultdict
import re

def filter_transactions_by_keyword(transactions, keyword):
    """
    Filter transactions by keyword in the description.

    Args:
        transactions (list): List of transaction dictionaries.
        keyword (str): Keyword to search for in transaction descriptions.

    Returns:
        list: List of transactions containing the keyword in their description.
    """
    keyword = keyword.lower()
    return [txn for txn in transactions if keyword in txn.get('description', '').lower()]

def categorize_transactions(transactions, categories):
    """
    Categorize transactions based on provided categories.

    Args:
        transactions (list): List of transaction dictionaries.
        categories (list): List of categories to search for in transaction descriptions.

    Returns:
        dict: A dictionary with categories as keys and counts of transactions as values.
    """
    categorized = defaultdict(int)
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        print(f"Description: {description}")  # Отладочный вывод
        for category in categories:
            category_lower = category.lower()
            pattern = r'\b' + re.escape(category_lower) + r'\b'
            print(f"Checking if '{category_lower}' is in '{description}' with pattern '{pattern}'")
            if re.search(pattern, description):
                print(f"Matched category '{category_lower}' in description '{description}'")
                categorized[category] += 1
                break
            else:
                print(f"No match for category '{category_lower}' in description '{description}'")
    return categorized