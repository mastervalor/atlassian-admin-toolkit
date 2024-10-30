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

    def test_get_dashboard_by_id(self):
        # Replace 'dashboard_id' with a valid dashboard ID in the staging environment
        dashboard_id = "1"  # Example ID for testing

        # Call the get_dashboard_by_id method
        response = self.looker_dashboard.get_dashboard_by_id(dashboard_id)

        # Check if the response status code is 200 (success) after handling potential token expiration
        self.assertEqual(response.status_code, 200, "Expected status code 200 for fetching dashboard by ID")

        # Verify the response contains the dashboard ID and other key details
        dashboard_data = response.json()
        self.assertIn("id", dashboard_data, "Response should contain 'id' field")
        self.assertIn("title", dashboard_data, "Response should contain 'title' field")
        self.assertEqual(str(dashboard_data["id"]), dashboard_id, "Dashboard ID in response should match requested ID")

    def test_search_dashboards_for_explore(self):
        # Replace 'explore_name' with a valid explore name for testing
        explore_name = "order_items"  # Example explore name in staging

        # Call the search_dashboards_for_explore method
        response = self.looker_dashboard.search_dashboards_for_explore(explore_name)

        # Check if the response is a list
        self.assertIsInstance(response, list, "Expected response to be a list of dashboards")

        # Optionally, check if the first result contains expected fields
        if response:
            dashboard = response[0]
            self.assertIn("id", dashboard, "Each dashboard result should contain an 'id' field")
            self.assertIn("title", dashboard, "Each dashboard result should contain a 'title' field")
            