import requests
from auth import atlassian_admin_Bearer_token
import json
from config import atlassian_admin_v1


class AtlassianAuthPolicies:
    def __init__(self):
        self.token = atlassian_admin_Bearer_token
        self.admin_url = atlassian_admin_v1
