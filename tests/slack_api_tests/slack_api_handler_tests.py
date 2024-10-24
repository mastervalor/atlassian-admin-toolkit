import unittest
from calls.slack_api_calls.slack_api_handling import SlackAPIHandling


class TestSlackAPIHandling(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_handler = SlackAPIHandling()

    def test_get(self):
        # Test the 'api.test' endpoint which is safe and doesn't require parameters
        endpoint = 'api.test'
        params = {'foo': 'bar'}
        response = self.api_handler.get(endpoint, params)
        self.assertTrue(response['ok'])
        self.assertEqual(response['args']['foo'], 'bar')

    def test_post(self):
        # Since 'api.test' supports both GET and POST, we can use it safely
        endpoint = 'api.test'
        data = {'foo': 'bar'}
        response = self.api_handler.post(endpoint, data)
        self.assertTrue(response['ok'])
        self.assertEqual(response['args']['foo'], 'bar')


if __name__ == '__main__':
    unittest.main()
