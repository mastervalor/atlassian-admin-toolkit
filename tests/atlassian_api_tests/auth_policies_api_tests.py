import unittest
from calls.atlassian_admin_api_calls.auth_policies_api import AtlassianAuthPolicies


class TestAuthPolicies(unittest.TestCase):
    def setUp(self):
        self.auth_policies = AtlassianAuthPolicies()

        