from logic.os_logic.json_logic import JSONLogic


def count_occurrences(data, search_term):
    """
    Recursively counts the number of times 'search_term' appears in the keys or values of the JSON data.

    :param data: The JSON data to search.
    :param search_term: The string to search for in keys and string values.
    :return: The total count of occurrences of 'search_term'.
    """
    count = 0

    if isinstance(data, dict):
        for key, value in data.items():
            # Check if search_term is in the key
            if search_term in key:
                count += 1

            # Check if search_term is in the value if it's a string
            if isinstance(value, str) and search_term in value:
                count += 1

            # Recursively search in the value
            elif isinstance(value, (dict, list)):
                count += count_occurrences(value, search_term)

    elif isinstance(data, list):
        for item in data:
            count += count_occurrences(item, search_term)

    elif isinstance(data, str):
        if search_term in data:
            count += 1

    return count
