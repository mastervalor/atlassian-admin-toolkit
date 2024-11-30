import re
from file_manip.json_file_manip import JSONManip


class JSONLogic:
    def __init__(self, open_file=None, write_file=None, append_file=None, base_dir=None):
        self.json_file_manip = JSONManip(open_file, write_file, append_file, base_dir)

    def count_occurrences(self, data, search_term):
        """
        Recursively counts the total number of times 'search_term' appears in keys and string values,
        including multiple occurrences within the same string.

        :param data: The JSON data to search.
        :param search_term: The string to search for in keys and string values.
        :return: The total count of occurrences of 'search_term'.
        """
        count = 0
        pattern = re.escape(search_term)

        if isinstance(data, dict):
            for key, value in data.items():
                # Count occurrences in the key
                count += len(re.findall(pattern, key))

                # Count occurrences in the value if it's a string
                if isinstance(value, str):
                    count += len(re.findall(pattern, value))

                # Recursively search in the value if it's a dict or list
                elif isinstance(value, (dict, list)):
                    count += self.count_occurrences(value, search_term)
                # Other data types are ignored
        elif isinstance(data, list):
            for item in data:
                count += self.count_occurrences(item, search_term)
        elif isinstance(data, str):
            count += len(re.findall(pattern, data))
        # Other data types are ignored

        return count