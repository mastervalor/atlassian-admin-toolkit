import unittest
from calls.jira_api_calls.jira_api_group_calls import GroupJiraCalls


class TestGroupJiraCalls(unittest.TestCase):
    def setUp(self):
        self.jira_group_calls = GroupJiraCalls(is_staging=True)

    def test_get_group(self):
        pref = ""
        group = "test-group"
        response = self.jira_group_calls.get_group(pref, group)
        self.assertIn("values", response)
        self.assertIn("name", response['values'][0])

    def test_remove_group_member(self):
        group = "test-group"
        user = "mourad.marzouk"
        response = self.jira_group_calls.remove_group_member(group, user)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
