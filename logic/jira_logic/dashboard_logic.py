from calls.jira_api_calls.jira_api_dashboards import DashboardsJiraCalls


class Dashboards:
    def __init__(self, is_staging=False):
        self.dashboards = DashboardsJiraCalls()

    def get_dashboard_id(self, name):
        start_at = 0
        max_results = 1000
        total = 1001
        ids = []
        dashboards = self.dashboards.get_all_dashboards(f'?startAt={start_at}&maxResults={max_results}')

        while total >= max_results:
            for dashboard in dashboards['dashboards']:
                if dashboard['name'].lower() == name.lower():
                    ids.append(dashboard['id'])
            else:
                total = dashboards['total']
                start_at += 1000
                max_results += 1000

        return ids
