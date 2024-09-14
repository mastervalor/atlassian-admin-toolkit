import unittest
from calls.jira_api_calls.jira_api_group_calls import GroupJiraCalls


class TestGroupJiraCalls(unittest.TestCase):
    def setUp(self):
        self.jira_calls = GroupJiraCalls(is_staging=True)

        def test_remove_group_member(self):
            group = "example-group"
            user = "example-user"
            response = self.jira_calls.remove_group_member(group, user)
            self.assertIn("removed", response.lower())
            print("Response from removing group member:", response)

        def test_get_group(self):
            pref = ""
            group = "example-group"
            response = self.jira_calls.get_group(pref, group)
            self.assertIsInstance(response, dict)
            self.assertIn("users", response)
            print("Response from getting group members:", response)


if __name__ == "__main__":
    unittest.main()
