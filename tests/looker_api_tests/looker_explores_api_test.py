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

    def test_get_all_explores_by_model(self):
        model_name = "jira"

        response = self.looker_explores.get_all_explores_by_model(model_name)

        self.assertEqual(response.status_code, 200, "Expected status code 200 for fetching explores by model")

        explores_data = response.json()
        self.assertIsInstance(explores_data, list, "Expected explores data to be a list")
        if explores_data:
            explore = explores_data[0]
            self.assertIn("name", explore, "Each explore should have a 'name' field")
            self.assertIn("description", explore, "Each explore should have a 'description' field")

    def test_get_query_history(self):
        model_name = "jira"
        explore_name = "jira"

        response = self.looker_explores.get_query_history(model_name, explore_name)

        self.assertIsInstance(response, dict, "Expected response to be a dictionary")
        self.assertIn("model", response, "Response should contain the 'model' field")
        self.assertIn("explore", response, "Response should contain the 'explore' field")
        self.assertIn("fields", response, "Response should contain the 'fields' field")


if __name__ == "__main__":
    unittest.main()
