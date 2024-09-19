from calls.jira_api_calls.jira_api_dashboards import DashboardsJiraCalls


class Dashboards:
    def __init__(self, is_staging=False):
        self.dashboards = DashboardsJiraCalls()

    def get_dashboard_id(self, name):
        start_at = 0
        max_results = 1000
        total = 1001
        ids = []

        while total >= max_results:
            dashboards = self.dashboards.get_all_dashboards(f'?startAt={start_at}&maxResults={max_results}')
            for dashboard in dashboards['dashboards']:
                if dashboard['name'].lower() == name.lower():
                    ids.append(dashboard['id'])
            else:
                total = dashboards['total']
                start_at += 1000
                max_results += 1000

        return ids

    def get_board_ids(self, name):
        start_at = 0
        max_results = 1000
        total = 1001
        ids = []

        while total >= max_results:
            boards = self.dashboards.get_all_boards(start_at, max_results)
            for dashboard in boards['dashboards']:
                if dashboard['name'].lower() == name.lower():
                    ids.append(dashboard['id'])
            else:
                total = boards['total']
                start_at += 1000
                max_results += 1000

        return ids

