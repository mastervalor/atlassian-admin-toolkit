import requests
from auth import conf_token, staging_conf_token
import json
from config import confluence, confluence_staging, conf_base


class Confluence:
    def __init__(self, is_staging=False):
        self.token = staging_conf_token if is_staging else conf_token
        self.conf_url = confluence_staging if is_staging else confluence
        self.conf_base = conf_base

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
