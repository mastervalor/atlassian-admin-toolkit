import unittest
from calls.jira_api_calls.jira_api_dashboards import DashboardsJiraCalls


class TestDashBoardJiraCalls(unittest.TestCase):
    def setUp(self):
        self.jira_dashboard_calls = DashboardsJiraCalls(is_staging=True)

    def test_delete_dashboard(self):
        dashboard_id = '24918'
        response = self.jira_dashboard_calls.delete_dashboard(dashboard_id)
        self.assertEqual(response.status_code, 200)

    def test_get_all_dashboards(self):
        pref = ''
        response = self.jira_dashboard_calls.get_all_dashboards(pref)
        self.assertIn("total", response)

    def test_get_all_boards(self):
        response = self.jira_dashboard_calls.get_all_boards()
        self.assertIn("total", response)

    def test_delete_board(self):
        board_id = '1428'
        response = self.jira_dashboard_calls.delete_board(board_id)
        self.assertEqual(response.status_code, 200)
