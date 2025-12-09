import requests
from requests.auth import HTTPBasicAuth
from auth import conf_cloud_dev_token, email
import json
from config import conf_cloud_v1, conf_cloud_v2, conf_cloud_v1_dev, conf_cloud_v2_dev


class ConfluencePageCalls:
    def __init__(self, is_staging=False):
        self.cloud_v1 = conf_cloud_v1_dev if is_staging else conf_cloud_v1
        self.cloud_v2 = conf_cloud_v2_dev if is_staging else conf_cloud_v2
        self.token = conf_cloud_dev_token
        self.auth = HTTPBasicAuth(email, self.token)

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
            auth=self.auth
        )

        return response

    def add_self_to_page_restriction(self, page_id):
        account_id = '63c996ae6178fcc941d947ad'
        url = f"{self.cloud_v1}/content/{page_id}/restriction/byOperation/update/user?accountId={account_id}"

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
            auth=self.auth
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
            auth=self.auth
        )

        return response

    def fetch_restrictions_for_page(self, page_id):
        url = self.cloud_v1 + f"content/{page_id}/restriction/byOperation"

        headers = {
            "Accept": "application/json"
        }

        response = requests.get(
            url,
            headers=headers,
            auth=self.auth
        )

        if response.status_code != 200:
            print(f"Failed to retrieve restrictions for page {page_id}: {response.status_code}")
            return None

        restrictions_data = response.json()

        return restrictions_data

    def get_child_pages_recursive(self, pref):
        url = self.cloud_v1 + f'content/{pref}/child/page?limit=500&expand=version'

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.auth
        ).text)

        pages = response["results"]
        page_dicts = []

        for page in pages:
            page_dict = {
                "id": page["id"],
                "title": page["title"],
                "children": self.get_child_pages_recursive(page["id"])
            }
            print(page['id'])
            page_dicts.append(page_dict)

        return page_dicts

    def move_page(self, pref, version, ancestors):
        url = self.cloud_v1 + f'content/{pref}'

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        payload = json.dumps({
            "version": {
                "number": version,
            },
            "title": "testing more page",
            "space": {
                "key": "T2"
            },
            "type": "page",
            "ancestors": [
                {
                    "id": ancestors
                }
            ]})

        response = json.loads(requests.request(
            "PUT",
            url,
            data=payload,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def create_content(self, page_type, space_key, title, content, ancestors):
        url = self.cloud_v1 + 'content'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

        payload = json.dumps({
            'type': page_type,
            'title': title,
            'space': {'key': space_key},
            "ancestors": [
                {
                    "id": ancestors
                }
            ],
            'body': {
                'storage': {
                    'value': content,
                    'representation': 'storage'
                }
            }
        })

        response = json.loads(requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=self.auth
        ).text)

        return response

    def update_content(self, page_id, page_type, title, content, version):
        url = self.cloud_v1 + f'content/{page_id}'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

        payload = json.dumps({
            'type': page_type,
            'title': title,
            'version': {
                'number': version + 1
            },
            'body': {
                'storage': {
                    'value': content,
                    'representation': 'storage'
                }
            }
        })

        response = json.loads(requests.request(
            "PUT",
            url,
            data=payload,
            headers=headers,
            auth=self.auth
        ).text)

        if response.status_code == 200:
            print(f"Page '{title}' updated successfully!")
        else:
            print(f"Failed to update page. Status code: {response.status_code}")
            print(response.text)
            return False
        return True

    def get_page(self, page_id):
        url = self.cloud_v1 + f'content/{page_id}?expand=body.storage,version,ancestors'
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.auth
        )

        if response.status_code == 200:
            return json.loads(response.text)

        else:
            print('Failed to retrieve page.')
            print('Response:', response.text)
            return None

    def delete_page(self, page_id):
        url = self.cloud_v1 + f"content/{page_id}"

        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = json.loads(requests.request(
            "DELETE",
            url,
            headers=headers,
            auth=self.auth
        ).text)

        if response.status_code == 200:
            print(f"Page '{page_id}' deleted successfully!")
        else:
            print(f"Failed to delete page. Status code: {response.status_code}")
            print(response.text)
            return False
        return True
