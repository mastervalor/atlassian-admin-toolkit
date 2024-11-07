from calls.slack_api_calls.slack_api_handling import SlackAPIHandling
from calls.slack_api_calls.slack_users_api import SlackUserAPI


class SlackMessageAPI:
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

    def send_message(self, channel_id, text=None, blocks=None):
        endpoint = 'chat.postMessage'
        data = {'channel': channel_id}
        if text:
            data['text'] = text
        if blocks:
            data['blocks'] = blocks
        response_data = self.api_handler.post(endpoint, data)
        return response_data

    def get_existing_group_channel(self, user_ids):
        """Checks for an existing group chat with the specified user IDs."""
        endpoint = 'conversations.list'
        params = {'types': 'private_channel', 'limit': 1000}  # Adjust limit as needed

        response_data = self.api_handler.get(endpoint, params)
        for channel in response_data.get('channels', []):
            if set(channel.get('members', [])) == set(user_ids):
                return channel['id']

        # No existing group found with these users
        return None
