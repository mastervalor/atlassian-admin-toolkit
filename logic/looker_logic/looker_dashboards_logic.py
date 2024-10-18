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

            # Extract model details from each element of the dashboard
            model_names = set()  # Use a set to avoid duplicates
            dashboard_elements = dashboard.get('dashboard_elements', [])

            for element in dashboard_elements:
                query = element.get('query')
                if query and 'model' in query:
                    model = query['model']
                    model_names.add(model)

            if model_names:
                print(f"Dashboard ID {dashboard_id} uses models: {', '.join(model_names)}")
            else:
                print(f"No model information found for dashboard ID {dashboard_id}")

            # Convert set to list before returning
            return list(model_names)
        else:
            raise Exception(f'Failed to retrieve dashboard {dashboard_id}: {response.content}')

    def search_for_jira_model(self, dashboard_elements):
        jira_model_count = 0  # To count, how many times the "Jira" model appears
        for element in dashboard_elements:
            # Check in 'look' for the model
            if 'look' in element:
                look = element['look']
                if 'query' in look and 'model' in look['query']:
                    model_info = look['query']['model']
                    if isinstance(model_info, dict) and model_info.get('id') == 'jira':
                        jira_model_count += 1
                    elif isinstance(model_info, str) and model_info == 'jira':
                        jira_model_count += 1

            # Check in 'result_maker' for the model
            if 'result_maker' in element:
                result_maker = element['result_maker']
                if 'query' in result_maker and 'model' in result_maker['query']:
                    model_info = result_maker['query']['model']
                    if isinstance(model_info, dict) and model_info.get('id') == 'jira':
                        jira_model_count += 1
                    elif isinstance(model_info, str) and model_info == 'jira':
                        jira_model_count += 1

        return jira_model_count
