import os
import requests


class APIHandler:
    def __init__(self, token=None):
        self.base_url = 'https://slack.com/api/'
        self.token = token or os.environ.get('SLACK_BOT_TOKEN')
        if not self.token:
            raise ValueError("Slack Bot User OAuth token is required.")
