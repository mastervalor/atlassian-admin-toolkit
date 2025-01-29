import requests
from auth import conf_cloud_dev_token
import json
from config import conf_cloud_v1, conf_cloud_v2, conf_cloud_v1_dev, conf_cloud_v2_dev


class ConfluenceUsersCalls:
    def __init__(self, is_staging=False):
        self.cloud_v1 = conf_cloud_v1_dev if is_staging else conf_cloud_v1
        self.cloud_v2 = conf_cloud_v2_dev if is_staging else conf_cloud_v2
        self.token = conf_cloud_dev_token

    def get_user(self, username):
        url = self.cloud_v1 + f'user?username={username}'
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}
        print(url)
        print(headers)
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)

        return response

    def user_groups(self, pref):
        url = self.cloud_v1 + f"user/memberof?username={pref}"

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)

        return response
