from calls.looker_api_calls.looker_dashboard_api import LookerDashboard


class LookerDashboardLogic:
    def __init__(self):
        self.looker_dashboard = LookerDashboard

    def get_all_dashboards(self):
        response = self.looker_dashboard.get_all_dashboards()

        if response.status_code == 200:
            dashboards = response.json()
            print("Dashboards and their details:")
            for dashboard in dashboards:
                print(
                    f"ID: {dashboard['id']}, Title: {dashboard['title']}, Description: "
                    f"{dashboard.get('description', 'No Description')}")
            return dashboards
        else:
            print(f'Failed to retrieve dashboards: {response.content}')
            return []
