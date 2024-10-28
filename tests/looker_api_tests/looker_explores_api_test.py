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
        # Replace 'model_name' with a valid model name for staging
        model_name = "ecommerce"  # Example model name in staging

        # Call the get_all_explores_by_model method
        response = self.looker_explores.get_all_explores_by_model(model_name)

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for fetching explores by model")

        # Optionally parse the response and check structure
        explores_data = response.json()
        self.assertIsInstance(explores_data, list, "Expected explores data to be a list")
        if explores_data:
            explore = explores_data[0]
            self.assertIn("name", explore, "Each explore should have a 'name' field")
            self.assertIn("description", explore, "Each explore should have a 'description' field")
            
