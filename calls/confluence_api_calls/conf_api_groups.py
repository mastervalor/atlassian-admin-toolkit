import requests
from auth import conf_cloud_dev_token
import json
from config import conf_cloud_v1, conf_cloud_v2, conf_cloud_v1_dev, conf_cloud_v2_dev


class ConfluenceGroupsCalls:
    def __init__(self, is_staging=False):
        self.cloud_v1 = conf_cloud_v1_dev if is_staging else conf_cloud_v1
        self.cloud_v2 = conf_cloud_v2_dev if is_staging else conf_cloud_v2
        self.token = conf_cloud_dev_token

    def group_members(self, name, expanded=False):
        url = self.cloud_v1 + f'group/{name}/member/?expand={expanded}' if expanded else f'group/{name}/member'
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)

        return response

    def get_group(self, pref, group):
        url = self.cloud_v1 + 'group/member' + pref

        headers = {
            "Accept": "application/json"
        }
        query = {
            'groupname': group
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response
