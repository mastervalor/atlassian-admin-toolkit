from calls.slack_api_calls.slack_users_api import SlackUserAPI
from calls.slack_api_calls.slack_messages_api import SlackMessageAPI


class MessageLogic:
    def __init__(self):
        self.user_handler = SlackUserAPI()
        self.message_handler = SlackMessageAPI()

