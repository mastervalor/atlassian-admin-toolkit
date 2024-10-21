import os
import requests


class APIHandler:
    def __init__(self, token=None):
        self.base_url = 'https://slack.com/api/'
        self.token = token or os.environ.get('SLACK_BOT_TOKEN')
        if not self.token:
            raise ValueError("Slack Bot User OAuth token is required.")

    def _post(self, endpoint, data):
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
