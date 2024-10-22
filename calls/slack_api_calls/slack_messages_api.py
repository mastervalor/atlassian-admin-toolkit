from calls.slack_api_calls.slack_api_handling import SlackAPIHandling
from calls.slack_api_calls.slack_users_api import SlackUserAPI


class MessageHandler:
    def __init__(self):
        self.api_handler = SlackAPIHandling()
        self.slack_users = SlackUserAPI()
