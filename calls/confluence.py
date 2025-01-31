import requests
from auth import conf_token, staging_conf_token
import json
from config import confluence, confluence_staging, conf_base


class Confluence:
    def __init__(self, is_staging=False):
        self.token = staging_conf_token if is_staging else conf_token
        self.conf_url = confluence_staging if is_staging else confluence
        self.conf_base = conf_base

    def update_content(self, page_id, page_type, title, content, version):
        url = self.conf_url + f'content/{page_id}'
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
            headers=headers
        ).text)

        if response.status_code == 200:
            print(f"Page '{title}' updated successfully!")
        else:
            print(f"Failed to update page. Status code: {response.status_code}")
            print(response.text)
            return False
        return True

    def get_page(self, page_id):
        url = self.conf_url + f'content/{page_id}?expand=body.storage,version,ancestors'
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request(
            "GET",
            url,
            headers=headers
        )

        if response.status_code == 200:
            return json.loads(response.text)

        else:
            print('Failed to retrieve page.')
            print('Response:', response.text)
            return None

    def delete_page(self, page_id):
        url = self.conf_url + f"content/{page_id}"

        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = json.loads(requests.request(
            "DELETE",
            url,
            headers=headers
        ).text)

        if response.status_code == 200:
            print(f"Page '{page_id}' deleted successfully!")
        else:
            print(f"Failed to delete page. Status code: {response.status_code}")
            print(response.text)
            return False
        return True
