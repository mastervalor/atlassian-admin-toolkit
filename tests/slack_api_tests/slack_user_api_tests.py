import unittest
from calls.slack_api_calls.slack_api_handling import SlackAPIHandling
from calls.slack_api_calls.slack_users_api import SlackUserAPI


class TestSlackUserAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_handler = SlackAPIHandling()
        cls.user_api = SlackUserAPI()
        cls.test_email = 'mourad.marzouk@getcruise.com'

