import requests
from requests.auth import HTTPBasicAuth
from auth import conf_cloud_dev_token, email
import json
from config import conf_cloud_v1, conf_cloud_v2, conf_cloud_v1_dev, conf_cloud_v2_dev


class ConfluenceSpaceCalls:
    def __init__(self, is_staging=False):
        self.cloud_v1 = conf_cloud_v1_dev if is_staging else conf_cloud_v1
        self.cloud_v2 = conf_cloud_v2_dev if is_staging else conf_cloud_v2
        self.token = conf_cloud_dev_token
        self.auth = HTTPBasicAuth(email, self.token)

    def get_spaces(self, limit=250, cursor=None):
        url = self.cloud_v2 + 'spaces'

        headers = {
            "Accept": "application/json"
        }

        params = {
            "limit": limit,
            "status": 'current',
        }

        if cursor:
            params["cursor"] = cursor

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=params,
            auth=self.auth
        ).text)

        return response

    def fetch_pages_in_space(self, space_id, cursor=None):
        url = self.cloud_v2 + f"spaces/{space_id}/pages"

        headers = {
            "Accept": "application/json"
        }

        params = {
        }

        if cursor:
            params["cursor"] = cursor

        try:
            response = requests.get(
                url,
                headers=headers,
                params=params,
                auth=self.auth
            )

            # Check if the request was successful (status code 200)
            if response.status_code != 200:
                print(f"Failed to retrieve pages for space {space_id}. Status Code: {response.status_code}")
                print(f"Response Text: {response.text}")
                return None

            # Try to parse the JSON response
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            print(f"Response Text: {response.text}")
            return None

    def set_space_permissions(self, key, payload):
        url = self.cloud_v2 + f'space/{key}/permission'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = json.loads(requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def get_space_permissions(self, key, expand=False):
        url = self.cloud_v2 + f'space/{key}/permission?expand={expand}' if expand else f'space/{key}/permission'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def get_space_groups(self, key, role_id):
        url = self.cloud_v2 + 'space/' + key + '/role/' + role_id

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.auth
        ).text)

        return response
