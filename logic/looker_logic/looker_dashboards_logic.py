from calls.looker_api_calls.looker_dashboard_api import LookerDashboard
from dataformating.datetime_formating import DateTimeFormating


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

    def get_dashboards_by_ids(self, dashboard_ids, model_name):
        """
        Retrieves and counts occurrences of a specified model in each dashboard by their IDs.

        :param dashboard_ids: List of dashboard IDs to retrieve.
        :param model_name: The name of the model to search for in the dashboard elements.
        :return: A list of dictionaries containing dashboard ID, title, and model count.
        """
        dashboards_info = []

        for dashboard_id in dashboard_ids:
            response = self.looker_dashboard.get_dashboard_by_id(dashboard_id)

            if response.status_code == 200:
                dashboard = response.json()
                model_count, dashboard_title = self.get_dashboards_models(dashboard, model_name)
                dashboards_info.append({
                    'dashboard_id': dashboard_id,
                    'title': dashboard_title,
                    'model_count': model_count
                })
            else:
                raise Exception(f'Failed to retrieve dashboard {dashboard_id}: {response.content}')

        return dashboards_info

    def recursive_model_search(self, data, model_name):
        """
        Recursively searches through nested dictionaries and lists for the specified model.

        :param data: The data (dictionary or list) to search through.
        :param model_name: The name of the model to search for.
        :return: The count of how many times the model is found.
        """
        model_count = 0

        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'model':
                    # Handle both dictionary and string representations of the model
                    if isinstance(value, dict) and value.get('id') == model_name:
                        model_count += 1
                    elif isinstance(value, str) and value == model_name:
                        model_count += 1
                # Recursively search in nested dictionaries
                model_count += self.recursive_model_search(value, model_name)

        elif isinstance(data, list):
            for item in data:
                # Recursively search in nested lists
                model_count += self.recursive_model_search(item, model_name)

        return model_count

    def get_dashboards_models(self, dashboard, model_name):
        """
        Extracts model details from the dashboard elements and counts occurrences of the specified model.

        :param dashboard: The dashboard object to process.
        :param model_name: The name of the model to search for in the dashboard elements.
        :return: A tuple with (model_count, dashboard_title), where model_count is the number of times the model is found.
        """
        dashboard_title = dashboard.get('title', 'No Title')
        dashboard_elements = dashboard.get('dashboard_elements', [])

        # Use recursive search to count occurrences of the model
        model_count = self.recursive_model_search(dashboard_elements, model_name)

        if model_count > 0:
            print(
                f"Dashboard ID {dashboard['id']} (Title: {dashboard_title}) uses model '{model_name}' {model_count} times.")
        else:
            print(f"Dashboard ID {dashboard['id']} (Title: {dashboard_title}) does not use model '{model_name}'.")

        return model_count, dashboard_title

    def get_dashboard_metadata(self, dashboard_ids, model_name):
        """
        Retrieves metadata for each dashboard including creation details, model count, and access details.

        :param dashboard_ids: List of dashboard IDs to retrieve.
        :param model_name: The name of the model to search for in the dashboard elements.
        :return: A list of dictionaries with dashboard metadata.
        """
        dashboards_info = []

        for dashboard_id in dashboard_ids:
            response = self.looker_dashboard.get_dashboard_by_id(dashboard_id)

            if response.status_code == 200:
                dashboard = response.json()

                # Call the get_dashboards_models function to get model count and title
                model_count, dashboard_title = self.get_dashboards_models(dashboard, model_name)

                # Extract high-level metadata
                dashboard_metadata = {
                    'dashboard_id': dashboard.get('id'),
                    'title': dashboard_title,
                    'created_at': DateTimeFormating.format_datetime(dashboard.get('created_at')),
                    'created_by': dashboard.get('user_name'),  # Assuming this field exists
                    'last_updated_at': DateTimeFormating.format_datetime(dashboard.get('updated_at')),
                    'last_updated_by': dashboard.get('last_updater_id'),
                    'last_viewed': DateTimeFormating.format_datetime(dashboard.get('last_viewed_at')),
                    'view_count': dashboard.get('view_count'),
                    'last_accessed': DateTimeFormating.format_datetime(dashboard.get('last_accessed_at')),
                    'model_name': model_name,
                    'model_count': model_count
                }

                dashboards_info.append(dashboard_metadata)
                print(f'All data found for {dashboard_title}')

            else:
                raise Exception(f'Failed to retrieve dashboard {dashboard_id}: {response.content}')

        return dashboards_info
