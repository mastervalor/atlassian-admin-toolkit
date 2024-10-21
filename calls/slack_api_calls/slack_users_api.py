import requests
from slack_api_handling import APIHandler


class UserAPIClient:
    def __init__(self, slack_api_handling):
        self.api_handler = slack_api_handling

    def get_user_id(self, user_email):
        endpoint = 'users.lookupByEmail'
        params = {'email': user_email}
        response_data = self.api_handler._get(endpoint, params)
        return response_data['user']['id']

