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