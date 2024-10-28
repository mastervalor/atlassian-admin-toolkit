import unittest
from calls.looker_api_calls.looker_user_api import LookerUsers


class TestLookerUsersIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize LookerUsers instance
        cls.looker_users = LookerUsers()

    def test_deactivate_user(self):
        # Replace 'user_id' with a real user ID for the integration test
        user_id = 123  # Example user ID in staging

        # Call the deactivate_user method
        response = self.looker_users.deactivate_user(user_id)

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for successful deactivation")

        # Optionally check the response content for expected structure
        response_data = response.json()
        self.assertIn('is_disabled', response_data, "Response JSON should contain 'is_disabled' key")
        self.assertTrue(response_data['is_disabled'], "User should be marked as disabled in response")


if __name__ == "__main__":
    unittest.main()
