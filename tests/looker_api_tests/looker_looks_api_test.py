import unittest
from calls.looker_api_calls.looker_looks_api import LooksExplores


class TestLooksExploresIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.looks_explores = LooksExplores()

