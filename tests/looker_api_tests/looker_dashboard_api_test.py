import unittest
from calls.looker_api_calls.looker_dashboard_api import LookerDashboard


class TestLookerDashboardIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize LookerDashboard instance
        cls.looker_dashboard = LookerDashboard()

    def test_get_all_dashboards(self):
        # Call the get_all_dashboards method
        response = self.looker_dashboard.get_all_dashboards()

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for fetching all dashboards")

        # Check if the response is a list
        dashboards = response.json()
        self.assertIsInstance(dashboards, list, "Expected response to be a list of dashboards")

        # Optionally check for specific fields in the first dashboard
        if dashboards:
            dashboard = dashboards[0]
            self.assertIn("id", dashboard, "Each dashboard should contain an 'id' field")
            self.assertIn("title", dashboard, "Each dashboard should contain a 'title' field")