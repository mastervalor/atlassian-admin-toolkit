import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging


class TicketsJiraCalls:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira

    def create_ticket(self, ticket):
        url = self.jira + 'issue'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(ticket)

        response = json.loads(requests.request(
            "POST",
            url,
            headers=headers,
            data=payload,
            auth=self.token
        ).text)

        return response

    def jql(self, pref, payload):
        url = self.jira + 'search' + pref

        headers = {
            "Accept": "application/json"
        }
        query = {
            'jql': payload,
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response

    def edit_ticket(self, key, payload):
        url = self.jira + 'issue/' + key
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.request(
            "PUT",
            url,
            headers=headers,
            json=payload,
            auth=self.token
        )

        return response

    def get_ticket(self, key):
        url = self.jira + 'issue/' + key + '?notifyUsers=false'

        headers = {
            "Accept": "application/json",
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

