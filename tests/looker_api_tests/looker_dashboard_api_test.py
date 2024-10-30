import unittest
from calls.looker_api_calls.looker_dashboard_api import LookerDashboard

class TestLookerDashboardIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize LookerDashboard instance
        cls.looker_dashboard = LookerDashboard()