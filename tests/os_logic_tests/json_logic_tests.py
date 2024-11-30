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
