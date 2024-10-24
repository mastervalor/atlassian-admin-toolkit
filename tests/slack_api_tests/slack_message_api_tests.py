import unittest
from calls.slack_api_calls.slack_api_handling import SlackAPIHandling
from calls.slack_api_calls.slack_messages_api import SlackMessageAPI
from calls.slack_api_calls.slack_users_api import SlackUserAPI


class TestMessageHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_handler = SlackAPIHandling()
        cls.message_handler = SlackMessageAPI()
        cls.user_api = SlackUserAPI()
        cls.test_email = 'mourad.marzouk@getcruise.com'
        cls.test_email_group = [
            'mourad.marzouk@getcruise.com',
            'test.user@getcruise.com'
        ]

    def test_open_direct_message(self):
        user_id = self.user_api.get_user_id(self.test_email)
        channel_id = self.message_handler.open_direct_message(user_id)
        self.assertIsNotNone(channel_id)
        print(f"DM Channel ID with {self.test_email}: {channel_id}")

    def test_send_direct_message(self):
        user_id = self.user_api.get_user_id(self.test_email)
        channel_id = self.message_handler.open_direct_message(user_id)
        response = self.message_handler.send_message(channel_id, "Hello from unittest!")
        self.assertTrue(response['ok'])
        print(f"Message sent to {self.test_email}")

    def test_open_group_message(self):
        user_ids = []
        for email in self.test_email_group:
            user_id = self.user_api.get_user_id(email)
            user_ids.append(user_id)
        channel_id = self.message_handler.open_group_message(user_ids)
        self.assertIsNotNone(channel_id)
        print(f"Group DM Channel ID: {channel_id}")

    def test_send_group_message(self):
        user_ids = []
        for email in self.test_email_group:
            user_id = self.user_api.get_user_id(email)
            user_ids.append(user_id)
        channel_id = self.message_handler.open_group_message(user_ids)
        response = self.message_handler.send_message(channel_id, "Hello group from unittest!")
        self.assertTrue(response['ok'])
        print(f"Group message sent to {', '.join(self.test_email_group)}")


if __name__ == '__main__':
    unittest.main()
