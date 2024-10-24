import unittest
from calls.slack_api_calls.slack_api_handling import SlackAPIHandling
from calls.slack_api_calls.slack_users_api import SlackUserAPI


class TestSlackUserAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_handler = SlackAPIHandling()
        cls.user_api = SlackUserAPI()
        cls.test_email = 'mourad.marzouk@getcruise.com'

    def test_get_user_id(self):
        try:
            user_id = self.user_api.get_user_id(self.test_email)
            self.assertIsNotNone(user_id)
            print(f"User ID for {self.test_email}: {user_id}")
        except Exception as e:
            self.fail(f"Exception occurred: {e}")


if __name__ == '__main__':
    unittest.main()
    