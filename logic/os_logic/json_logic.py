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

    def find_occurrences(self, data, search_pattern):
        """
        Recursively finds all occurrences of 'search_pattern' in keys and string values,
        and returns a list of full matches.

        :param data: The JSON data to search.
        :param search_pattern: The regex pattern to search for in keys and string values.
        :return: A list of full matches of 'search_pattern'.
        """
        matches = []
        pattern = re.compile(search_pattern)

        if isinstance(data, dict):
            for key, value in data.items():
                # Find matches in the key
                key_matches = pattern.findall(key)
                matches.extend(key_matches)

                # Find matches in the value if it's a string
                if isinstance(value, str):
                    value_matches = pattern.findall(value)
                    matches.extend(value_matches)

                # Recursively search in the value if it's a dict or list
                elif isinstance(value, (dict, list)):
                    matches.extend(self.find_occurrences(value, search_pattern))
                # Other data types are ignored
        elif isinstance(data, list):
            for item in data:
                matches.extend(self.find_occurrences(item, search_pattern))
        elif isinstance(data, str):
            value_matches = pattern.findall(data)
            matches.extend(value_matches)

        return matches

    def replace_values(self, data, value_mapping, search_pattern):
        """
            Recursively traverses the JSON data and replaces occurrences of 'customfield_<ID>'
            with the corresponding 'cloud_id' from fields_mapping.

            :param data: The JSON data to process.
            :param fields_mapping: A dictionary mapping server IDs to cloud IDs.
            :param search_pattern: The regex pattern to search for 'customfield_<ID>'.
            :return: The updated JSON data with replacements.
        """
        pattern = re.compile(search_pattern)
        if isinstance(data, dict):
            # Traverse dictionary
            for key, value in data.items():
                if isinstance(value, str):
                    # Replace in string values
                    matches = pattern.findall(value)
                    for match in matches:
                        field_id = match.split('customfield_')[1]
                        cloud_id = value_mapping.get(field_id)
                        if cloud_id:
                            value = value.replace(match, f"customfield_{cloud_id}")
                    data[key] = value
                elif isinstance(value, (dict, list)):
                    # Recursively process nested structures
                    self.replace_values(value, value_mapping, search_pattern)
                    