import unittest
from calls.atlassian_admin_api_calls.user_directory_api_calls import UserDirectory


class TestUserDirectory(unittest.TestCase):
    def setUp(self):
        self.user_directory = UserDirectory()

    def test_restore_user(self):
        user_id = ['63c996ae6178fcc941d947ad']
        response = self.user_directory.restore_user(user_id)
        self.assertEqual(response.status_code, 200)
