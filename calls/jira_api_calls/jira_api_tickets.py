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
    