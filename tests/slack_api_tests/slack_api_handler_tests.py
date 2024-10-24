import unittest
from calls.slack_api_calls.slack_api_handling import SlackAPIHandling


class TestSlackAPIHandling(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_handler = SlackAPIHandling()

    