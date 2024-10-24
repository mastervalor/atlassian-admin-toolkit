import unittest
from calls.slack_api_calls.slack_api_handling import SlackAPIHandling
from calls.slack_api_calls.slack_messages_api import SlackMessageAPI
from calls.slack_api_calls.slack_users_api import SlackUserAPI


class TestMessageHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_handler = SlackAPIHandling()
        cls.message_handler = SlackMessageAPI()
        cls.user_api = SlackUserAPI()
        cls.test_email = 'mourad.marzouk@getcruise.com'
        cls.test_email_group = [
            'mourad.marzouk@getcruise.com',
            'test.user@getcruise.com'
        ]