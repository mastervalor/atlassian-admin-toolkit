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

    def get_dashboards_models(self, dashboard_id, model_name):
        """
        Retrieves and counts occurrences of the specified model in the dashboard elements.

        :param dashboard_id: The ID of the dashboard to retrieve.
        :param model_name: The name of the model to search for in the dashboard elements.
        :return: A tuple with (model_count, dashboard_title), where model_count is the number of times the model is found.
        """
        response = self.looker_dashboard.get_dashboard_by_id(dashboard_id)
        if response.status_code == 200:
            dashboard = response.json()
            dashboard_title = dashboard.get('title', 'No Title')

            # Extract model details from each element of the dashboard
            model_count = 0
            dashboard_elements = dashboard.get('dashboard_elements', [])

            for element in dashboard_elements:
                # Check if the model is present in the 'query' of the dashboard element
                query = element.get('query')
                if query and 'model' in query:
                    model_info = query['model']
                    if isinstance(model_info, dict):
                        if model_info.get('id') == model_name:
                            model_count += 1
                    elif isinstance(model_info, str) and model_info == model_name:
                        model_count += 1

                # Check for models within 'result_maker'
                result_maker = element.get('result_maker')
                if result_maker and 'query' in result_maker:
                    query = result_maker['query']
                    model_info = query.get('model')
                    if isinstance(model_info, dict):
                        if model_info.get('id') == model_name:
                            model_count += 1
                    elif isinstance(model_info, str) and model_info == model_name:
                        model_count += 1

            if model_count > 0:
                print(
                    f"Dashboard ID {dashboard_id} (Title: {dashboard_title}) uses model '{model_name}' {model_count} times.")
            else:
                print(f"Dashboard ID {dashboard_id} (Title: {dashboard_title}) does not use model '{model_name}'.")

            return model_count, dashboard_title
        else:
            raise Exception(f'Failed to retrieve dashboard {dashboard_id}: {response.content}')