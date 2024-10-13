import requests
from config import looker_base_url
from calls.looker_api_calls.looker_token_api import LookerToken


class LookerExplores:
    def __init__(self):
        self.looker_url = looker_base_url
        self.looker_token = LookerToken()
        self.token = self.looker_token.get_access_token()