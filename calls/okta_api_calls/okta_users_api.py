from auth import okta_token
from config import okta
import requests
import json


class OktaUsers:
    def __init__(self):
        self.token = okta_token
        self.okta_base_url = okta

