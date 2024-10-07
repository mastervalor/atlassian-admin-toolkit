import unittest
from calls.atlassian_admin_api_calls.user_directory_api_calls import UserDirectory


class TestUserDirectory(unittest.TestCase):
    def setUp(self):
        self.user_directory = UserDirectory()

    def test_restore_user(self):
        user_id = '4785775'
