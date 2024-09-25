import requests
from auth import conf_cloud_dev_token
import json
from config import conf_cloud_v1, conf_cloud_v2, conf_cloud_v1_dev, conf_cloud_v2_dev


class ConfluenceSpaceCalls:
    def __init__(self, is_staging=False):
        self.cloud_v1 = conf_cloud_v1_dev if is_staging else conf_cloud_v1
        self.cloud_v2 = conf_cloud_v2_dev if is_staging else conf_cloud_v2
        self.token = conf_cloud_dev_token

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
            auth=self.token
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
                auth=self.token
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

    def fetch_restrictions_for_page(self, page_id):
        url = self.cloud_v1 + f"content/{page_id}/restriction/byOperation"

        headers = {
            "Accept": "application/json"
        }

        response = requests.get(
            url,
            headers=headers,
            auth=self.token
        )

        if response.status_code != 200:
            print(f"Failed to retrieve restrictions for page {page_id}: {response.status_code}")
            return None

        restrictions_data = response.json()

        return restrictions_data

    def add_user_to_page_restriction(self, page_id, operation_key, account_id):
        url = f"{self.cloud_v1}/content/{page_id}/restriction/byOperation/{operation_key}/user?accountId={account_id}"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = {
            "results": [
                {
                    "operation": operation_key,
                    "restrictions": {
                        "user": [
                            {"accountId": account_id},  # The user you're adding
                            {"accountId": '557058:981107ee-1d06-4794-9954-f21c4e7c246a'}  # Yourself to avoid eviction
                        ]
                    }
                }
            ]
        }
        print(f"Adding user {account_id} to page {page_id} with operation {operation_key}.")

        response = requests.put(
            url,
            headers=headers,
            json=payload,
            auth=self.token
        )

        return response

    def add_restrictions_to_page(self, page_id, operation_key, account_id):
        url = f"{self.cloud_v1}/content/{page_id}/restriction"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        # Payload to add the user to the specified operation
        payload = {
            "results": [
                {
                    "operation": operation_key,
                    "restrictions": {
                        "user": [
                            {
                                "type": 'Known',
                                "accountId": account_id,
                            }
                        ]
                    }
                }
            ]
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            auth=self.token
        )

        return response
