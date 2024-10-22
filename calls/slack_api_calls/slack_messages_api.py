from calls.slack_api_calls.slack_api_handling import SlackAPIHandling
from calls.slack_api_calls.slack_users_api import SlackUserAPI


class MessageHandler:
    def __init__(self):
        self.api_handler = SlackAPIHandling()
        self.slack_users = SlackUserAPI()

    def open_direct_message(self, user_id):
        endpoint = 'conversations.open'
        data = {'users': user_id}
        response_data = self.api_handler.post(endpoint, data)
        return response_data['channel']['id']

    def open_group_message(self, user_ids):
        if not isinstance(user_ids, list) or len(user_ids) < 2:
            raise ValueError("user_ids must be a list of at least two user IDs.")
        endpoint = 'conversations.open'
        data = {'users': ','.join(user_ids)}
        response_data = self.api_handler.post(endpoint, data)
        return response_data['channel']['id']

