from file_manip.json_file_manip import JSONManip


class JSONLogic:
    def __init__(self, open_file=None, write_file=None, append_file=None):
        self.json_file_manip = JSONManip(open_file, write_file, append_file)

    def count_occurrences(self, data, search_term):
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
                    count += self.count_occurrences(value, search_term)

        elif isinstance(data, list):
            for item in data:
                count += self.count_occurrences(item, search_term)

        elif isinstance(data, str):
            if search_term in data:
                count += 1

        return count
