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

    def test_remove_defult_admins(self):
        # Arrange
        admins = ['user1', 'user2.svc', 'admin1', 'user3.car']
        self.mock_jira.group_members.return_value = ['admin1', 'admin2']

        # Act
        result = self.groups_users.remove_defult_admins(admins)

        # Assert
        self.assertEqual(result, ['user1'])
        self.mock_jira.group_members.assert_called_once_with("administrators")

    def test_get_group_members_with_status_active(self):
        # Arrange
        group = 'test-group'
        self.mock_jira.get_group.return_value = {
            'values': [{'name': 'user1'}, {'name': 'user2'}],
            'total': 2
        }

        # Act
        result = self.groups_users.get_group_members_with_status(group, inactive=False)

        # Assert
        self.assertEqual(result, ['user1', 'user2'])
        self.mock_jira.get_group.assert_called()

    def test_get_group_members_with_status_inactive(self):
        # Arrange
        group = 'test-group'
        self.mock_jira.get_group.return_value = {
            'values': [{'name': 'user1'}, {'name': 'user2'}],
            'total': 2
        }

        # Act
        result = self.groups_users.get_group_members_with_status(group, inactive=True)

        # Assert
        self.assertEqual(result, ['user1', 'user2'])
        self.mock_jira.get_group.assert_called()