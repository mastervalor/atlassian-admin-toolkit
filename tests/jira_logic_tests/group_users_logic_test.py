import unittest
from unittest.mock import MagicMock, patch
from logic.jira_logic.groups_users_logic import GroupsUsers  # Replace with your actual import path
from calls.jira import Jira

class TestGroupsUsers(unittest.TestCase):
    def setUp(self):
        # Set up the mock Jira instance
        self.mock_jira = MagicMock(spec=Jira)
        # Initialize the GroupsUsers instance with the mocked Jira
        self.groups_users = GroupsUsers()
        self.groups_users.jira = self.mock_jira