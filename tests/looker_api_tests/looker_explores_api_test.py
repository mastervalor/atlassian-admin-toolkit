import unittest
from calls.looker_api_calls.looker_explores_api import LookerExplores


class TestLookerExploresIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.looker_explores = LookerExplores()
