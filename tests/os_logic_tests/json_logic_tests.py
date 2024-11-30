import unittest
from logic.os_logic.json_logic import JSONLogic


class TestJSONLogic(unittest.TestCase):
    def setUp(self):
        # Sample JSON data to use in tests
        self.sample_data = {
            "customfield_1": "value1",
            "field2": {
                "subfield": "customfield_2",
                "customfield_3": "customfield_4"
            },
            "list_field": [
                "customfield_5",
                {"customfield_6": "value2"}
            ],
            "non_matching_field": "some_value"
        }

        # Initialize JSONLogic
        self.json_logic = JSONLogic()

    def test_count_occurrences(self):
        search_term = 'customfield_'
        count = self.json_logic.count_occurrences(self.sample_data, search_term)

        expected_count = 6
        self.assertEqual(count, expected_count)

    def test_count_occurrences_no_match(self):
        search_term = 'nonexistent_term'
        count = self.json_logic.count_occurrences(self.sample_data, search_term)
        self.assertEqual(count, 0)

    def test_count_occurrences_partial_match(self):
        search_term = 'field'
        count = self.json_logic.count_occurrences(self.sample_data, search_term)

        expected_count = 10
        self.assertEqual(count, expected_count)
