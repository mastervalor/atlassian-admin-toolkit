import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging


class DashboardsJiraCalls:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira

    def delete_dashboard(self, dashboard_id):
        url = self.jira + f'dashboard/{dashboard_id}'

        response = requests.request(
            "DELETE",
            url,
            auth=self.token
        )

        return response

    def get_all_dashboards(self, pref):
        url = self.jira + 'dashboard' + pref

        response = json.loads(requests.request(
            "GET",
            url,
            auth=self.token
        ).text)

        return response
