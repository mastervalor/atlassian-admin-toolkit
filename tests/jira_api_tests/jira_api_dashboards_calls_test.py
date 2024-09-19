import unittest
from calls.jira_api_calls.jira_api_dashboards import DashboardsJiraCalls


class TestDashBoardJiraCalls(unittest.TestCase):
    def setUp(self):
        self.jira_dashboard_calls = DashboardsJiraCalls(is_staging=True)

    def test_delete_dashboard(self):
        dashboard_id = '24918'
        response = self.jira_dashboard_calls.delete_dashboard(dashboard_id)
        self.assertEqual(response.status_code, 200)
