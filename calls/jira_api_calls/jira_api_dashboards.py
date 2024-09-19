import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging, jira_agile, jira_agile_dev


class DashboardsJiraCalls:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira_agile = jira_agile_dev if is_staging else jira_agile
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

    def get_all_boards(self, start_at=None):
        url = self.jira_agile + "board"

        params = {
            'startAt': start_at
        }

        response = json.loads(requests.request(
            "GET",
            url,
            params=params,
            auth=self.token
        ).text)

        return response

    def delete_board(self, board_id):
        url = self.jira_agile + "board/" + board_id

        response = requests.request(
            "DELETE",
            url,
            auth=self.token
        )

        return response
