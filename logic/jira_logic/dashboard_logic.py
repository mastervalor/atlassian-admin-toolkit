from calls.jira_api_calls.jira_api_dashboards import DashboardsJiraCalls


class Dashboards:
    def __init__(self, is_staging=False):
        self.dashboards = DashboardsJiraCalls()
