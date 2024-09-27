import requests
from auth import conf_cloud_dev_token
import json
from config import conf_cloud_v1, conf_cloud_v2, conf_cloud_v1_dev, conf_cloud_v2_dev


class ConfluencePageCalls:
    def __init__(self, is_staging=False):
        self.cloud_v1 = conf_cloud_v1_dev if is_staging else conf_cloud_v1
        self.cloud_v2 = conf_cloud_v2_dev if is_staging else conf_cloud_v2
        self.token = conf_cloud_dev_token

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

    def add_self_to_page_restriction(self, page_id, operation_key):
        url = f"{self.cloud_v1}/content/{page_id}/restriction/byOperation/{operation_key}/user"

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
                            {"accountId": '557058:981107ee-1d06-4794-9954-f21c4e7c246a'}  # Yourself to avoid eviction
                        ]
                    }
                }
            ]
        }
        print(f"Adding user self to page {page_id} with operation {operation_key}.")

        response = requests.put(
            url,
            headers=headers,
            json=payload,
            auth=self.token
        )

        return response

    def add_user_to_page_restriction(self, page_id, operation_key, account_id):
        url = f"{self.cloud_v1}/content/{page_id}/restriction/byOperation/{operation_key}/user?accountId={account_id}"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        data = {
            "accountId": account_id
        }

        response = requests.put(
            url,
            headers=headers,
            json=data,
            auth=self.token
        )

        return response
