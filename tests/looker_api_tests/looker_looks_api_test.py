import unittest
from calls.looker_api_calls.looker_looks_api import LooksExplores


class TestLooksExploresIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.looks_explores = LooksExplores()

    def test_search_looks_by_explore(self):
        explore_name = "order_items"
        response = self.looks_explores.search_looks_by_explore(explore_name)

        self.assertIsInstance(response, list, "Expected response to be a list of looks")

        if response:
            look = response[0]
            self.assertIn("id", look, "Each look result should contain an 'id' field")
            self.assertIn("title", look, "Each look result should contain a 'title' field")
            self.assertIn("query_id", look, "Each look result should contain a 'query_id' field")


