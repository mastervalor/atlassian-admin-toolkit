import unittest
from calls.looker_api_calls.looker_token_api import LookerToken


class TestLookerTokenApi(unittest.TestCase):
    def setUp(self):
        self.looker_token = LookerToken()

    def test_get_access_token(self):
        token = self.looker_token.get_access_token()
        self.assertIsInstance(token, str)


if __name__ == "__main__":
    unittest.main()