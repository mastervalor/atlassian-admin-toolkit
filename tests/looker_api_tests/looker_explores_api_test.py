import unittest
from calls.looker_api_calls.looker_explores_api import LookerExplores


class TestLookerExploresIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.looker_explores = LookerExplores()

    def test_get_all_models(self):
        response = self.looker_explores.get_all_models()

        self.assertIsInstance(response, list, "Expected response to be a list of models")

        if response:
            model = response[0]
            self.assertIn("name", model, "Each model should have a 'name' field")
            self.assertIn("explores", model, "Each model should contain 'explores'")
