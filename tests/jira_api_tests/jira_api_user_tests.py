import unittest
from calls.jira_api_calls.jira_api_user_calls import UserJiraCalls


class TestUserJiraCalls(unittest.TestCase):
    def setUp(self):
        self.jira_user_calls = UserJiraCalls(is_staging=True)

    def test_get_user(self):
        user = 'mourad.marzouk'
        response = self.jira_user_calls.get_user(user)
        self.assertEqual(response['emailAddress'], 'mourad.marzouk@getcruise.com')


# test = UserJiraCalls()
#
# print(test.get_user('mourad.marzouk'))
