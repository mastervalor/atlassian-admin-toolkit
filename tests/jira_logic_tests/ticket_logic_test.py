from logic.jira_logic.ticket_logic import Tickets
from dataformating.json_formating import JSONFormating
import unittest
from unittest.mock import MagicMock, patch


tickets = Tickets()
formating = JSONFormating()


class TestTickets(unittest.TestCase):
    def setUp(self):
        # Set up the mock Jira instance
        self.mock_jira = MagicMock(spec=Jira)
        # Initialize the Tickets instance with the mocked Jira
        self.tickets = Tickets()
        self.tickets.jira = self.mock_jira

        def test_build_ticket_payload(self):
            # Arrange
            ticket_info = {
                'summary': 'Test Summary',
                'assignee': 'test.assignee',
                'description': 'Test Description',
                'parent ticket': 'TEST-123'
            }

            # Act
            self.tickets.build_ticket_payload(ticket_info)

            # Assert
            self.mock_jira.create_ticket.assert_called_once()
            payload_arg = self.mock_jira.create_ticket.call_args[0][0]
            self.assertEqual(payload_arg['fields']['summary'], 'Test Summary')
            self.assertEqual(payload_arg['fields']['assignee']['name'], 'test.assignee')
            self.assertEqual(payload_arg['update']['issuelinks'][0]['add']['outwardIssue']['key'], 'TEST-123')

        def test_build_values_list(self):
            # Arrange
            values = "Value1, Value2, Value3"

            # Act
            result = self.tickets.build_values_list(values)

            # Assert
            self.assertEqual(result, [{"value": "Value1"}, {"value": "Value2"}, {"value": "Value3"}])

            # Test empty values
            result = self.tickets.build_values_list("")
            self.assertEqual(result, [])

        def test_process_linked_issues(self):
            # Arrange
            ticket_key = 'TEST-123'
            linked_issues_str = 'ISSUE-1, ISSUE-2'
            link_types_str = 'Blocks, Clones'

            # Act
            self.tickets.process_linked_issues(ticket_key, linked_issues_str, link_types_str)

            # Assert
            self.assertEqual(self.mock_jira.add_issue_link.call_count, 2)
            self.mock_jira.add_issue_link.assert_any_call('TEST-123', 'ISSUE-1', 'Blocks')
            self.mock_jira.add_issue_link.assert_any_call('TEST-123', 'ISSUE-2', 'Clones')

        def test_get_ticket_keys_from_jql(self):
            # Arrange
            query = 'project = TEST'
            self.mock_jira.jql.return_value = {
                'issues': [{'key': 'TEST-1'}, {'key': 'TEST-2'}],
                'total': 2
            }

            # Act
            result = self.tickets.get_ticket_keys_from_jql(query)

            # Assert
            self.assertEqual(result, ['TEST-1', 'TEST-2'])
            self.mock_jira.jql.assert_called()
