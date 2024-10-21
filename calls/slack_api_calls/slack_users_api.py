from slack_api_handling import SlackAPIHandling


class SlackUserAPI:
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def get_user_id(self, user_email):
        endpoint = 'users.lookupByEmail'
        params = {'email': user_email}
        response_data = self.api_handler.get(endpoint, params)
        return response_data['user']['id']


