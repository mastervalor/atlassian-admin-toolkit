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