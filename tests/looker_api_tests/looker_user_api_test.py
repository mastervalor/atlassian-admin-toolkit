import unittest
from calls.looker_api_calls.looker_user_api import LookerUsers


class TestLookerUsersIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize LookerUsers instance
        cls.looker_users = LookerUsers()
