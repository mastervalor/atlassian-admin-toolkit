import unittest
from calls.jira_api_calls.jira_api_user_calls import UserJiraCalls


class TestUserJiraCalls(unittest.TestCase):
    def setUp(self):
        self.jira_user_calls = UserJiraCalls(is_staging=True)

    def test_get_user(self):
        query = {
            'username': 'mourad.marzouk',
        }
        response = self.jira_user_calls.get_user(query)
        self.assertEqual(response['emailAddress'], 'mourad.marzouk@getcruise.com')

    def test_delete_user(self):
        user = 'test.user'
        response = self.jira_user_calls.delete_user(user)
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_key(self):
        user = 'JIRAUSER73627'
        response = self.jira_user_calls.get_user_by_key(user)
        self.assertEqual(response['name'], 'swaroop.vimalkumar')


if __name__ == "__main__":
    unittest.main()
