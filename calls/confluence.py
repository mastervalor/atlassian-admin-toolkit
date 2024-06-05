import requests
from auth import auth, staging_auth, okta_token, conf_token, staging_conf_token
import json
from config import confluence, jira, jira_staging, confluence_staging, conf_base


class Confluence:
    def __init__(self, is_staging=False):
        self.token = staging_conf_token if is_staging else conf_token
        self.conf_url = confluence_staging if is_staging else confluence
        self.conf_base = conf_base

    def get_user(self, username):
        url = self.conf_url + f'user?username={username}'
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
        url = confluence + f"user/memberof?username={pref}"

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)

        return response

    def group_members(self, pref):
        url = self.conf_base + pref
        print(url)
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)

        return response

    def conf_call(self, pref):
        url = self.conf_url + pref

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"}

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
        ).text)
        print(response)
        return response

    def get_child_pages_recursive(self, pref):
        url = f'content/{pref}/child/page?limit=500&expand=version'
        response = self.conf_call(url)

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
        url = self.conf_url + f'content/{pref}'

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
            headers=headers
        ).text)

        return response
