from calls.looker_api_calls.looker_dashboard_api import LookerDashboard


class LookerDashboardLogic:
    def __init__(self):
        self.looker_dashboard = LookerDashboard()

    def get_all_dashboards(self):
        response = self.looker_dashboard.get_all_dashboards()

        if response.status_code == 200:
            dashboards = response.json()
            for dashboard in dashboards:
                print(f"ID: {dashboard['id']}, Title: {dashboard['title']}, URL: {dashboard['url']}")
            return dashboards
        else:
            raise Exception(f'Failed to retrieve dashboards: {response.content}')

    def get_dashboards_by_id(self, dashboard_ids):
        for dashboard_id in dashboard_ids:
            response = self.looker_dashboard.get_dashboard_by_id(dashboard_id)

            if response.status_code == 200:
                dashboard = response.json()
                print(f"ID: {dashboard['id']}, Title: {dashboard['title']}, URL: {dashboard['url']}")
                return dashboard
            else:
                raise Exception(f'Failed to retrieve dashboard {dashboard_id}: {response.content}')

    def get_dashboards_models(self, dashboard_id):
        response = self.looker_dashboard.get_dashboard_by_id(dashboard_id)
        if response.status_code == 200:
            dashboard = response.json()

            # Assuming model information is stored within `dashboard_elements`
            # Extract model details from each element of the dashboard
            model_names = set()  # Use a set to avoid duplicates
            for element in dashboard.get('dashboard_elements', []):
                model = element.get('query', {}).get('model')
                if model:
                    model_names.add(model)

            if model_names:
                print(f"Dashboard ID {dashboard_id} uses models: {', '.join(model_names)}")
            else:
                print(f"No model information found for dashboard ID {dashboard_id}")

            return model_names
        else:
            raise Exception(f'Failed to retrieve dashboard {dashboard_id}: {response.content}')
