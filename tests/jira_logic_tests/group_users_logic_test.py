import unittest
from unittest.mock import MagicMock, patch
from logic.jira_logic.group_logic import GroupsUsers
from calls.jira import Jira


class TestGroupsUsers(unittest.TestCase):
    def setUp(self):
        # Set up the mock Jira instance
        self.mock_jira = MagicMock(spec=Jira)
        # Initialize the GroupsUsers instance with the mocked Jira
        self.groups_users = GroupsUsers()
        self.groups_users.jira = self.mock_jira

    def test_remove_default_admins(self):
        # Arrange
        admins = ['user1', 'user2.svc', 'admin1', 'user3.car']
        self.mock_jira.group_members.return_value = ['admin1', 'admin2']

        # Act
        result = self.groups_users.remove_default_admins(admins)

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

    def test_get_group_members_with_status_key_error(self):
        # Arrange
        group = 'test-group'
        self.mock_jira.get_group.return_value = {}

        # Act
        result = self.groups_users.get_group_members_with_status(group, inactive=False)

        # Assert
        self.assertEqual(result, [])
        self.mock_jira.get_group.assert_called()

    def test_remove_all_group_members(self):
        # Arrange
        group = 'test-group'
        self.groups_users.get_group_members_with_status = MagicMock(return_value=['user1', 'user2'])
        mock_response = MagicMock()
        mock_response.text = "Removed"
        self.mock_jira.remove_group_member.return_value = mock_response

        # Act
        self.groups_users.remove_all_group_members(group)

        # Assert
        self.groups_users.get_group_members_with_status.assert_called_once_with(group, True)
        self.mock_jira.remove_group_member.assert_any_call(group, 'user1')
        self.mock_jira.remove_group_member.assert_any_call(group, 'user2')

    def test_compare_groups(self):
        # Arrange
        group1 = 'group1'
        group2 = 'group2'
        self.mock_jira.group_members.side_effect = [
            ['user1', 'user2'],
            ['user2', 'user3']
        ]

        # Act
        result = self.groups_users.compare_groups(group1, group2)

        # Assert
        self.assertEqual(result, ['user3'])
        self.mock_jira.group_members.assert_any_call(group1)
        self.mock_jira.group_members.assert_any_call(group2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
