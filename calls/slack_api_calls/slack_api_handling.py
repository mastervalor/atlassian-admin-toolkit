import requests
from auth import slack_token


class SlackAPIHandling:
    def __init__(self):
        self.base_url = 'https://slack.com/api/'
        self.token = slack_token
        if not self.token:
            raise ValueError("Slack Bot User OAuth token is required.")

    def post(self, endpoint, data):
        url = self.base_url + endpoint
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        if not response_data.get('ok'):
            error = response_data.get('error', 'Unknown error')
            raise Exception(f"Slack API error on {endpoint}: {error}")
        return response_data

    def get(self, endpoint, params):
        url = self.base_url + endpoint
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()
        if not response_data.get('ok'):
            error = response_data.get('error', 'Unknown error')
            raise Exception(f"Slack API error on {endpoint}: {error}")
        return response_data
