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

    def get_dashboards_by_ids(self, dashboard_ids, model_names):
        """
        Retrieves and counts occurrences of specified models in each dashboard by their IDs.

        :param dashboard_ids: List of dashboard IDs to retrieve.
        :param model_names: List of model names to search for in the dashboard elements.
        :return: A list of dictionaries containing dashboard ID, title, and model counts.
        """
        dashboards_info = []

        for dashboard_id in dashboard_ids:
            response = self.looker_dashboard.get_dashboard_by_id(dashboard_id)

            if response.status_code == 200:
                dashboard = response.json()
                model_counts, dashboard_title = self.get_dashboards_models(dashboard, model_names)
                dashboards_info.append({
                    'dashboard_id': dashboard_id,
                    'title': dashboard_title,
                    'model_counts': model_counts  # Dictionary of model counts
                })
            else:
                raise Exception(f'Failed to retrieve dashboard {dashboard_id}: {response.content}')

        return dashboards_info

    def recursive_model_search(self, data, model_names):
        """
        Recursively searches through nested dictionaries and lists for the specified models.

        :param data: The data (dictionary or list) to search through.
        :param model_names: A list of model names to search for.
        :return: A dictionary with model counts for each model.
        """
        model_counts = {model: 0 for model in model_names}  # Initialize count for each model

        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'model':
                    # Handle both dictionary and string representations of the model
                    for model in model_names:
                        if isinstance(value, dict) and value.get('id') == model:
                            model_counts[model] += 1
                        elif isinstance(value, str) and value == model:
                            model_counts[model] += 1
                # Recursively search in nested dictionaries
                nested_model_counts = self.recursive_model_search(value, model_names)
                for model, count in nested_model_counts.items():
                    model_counts[model] += count

        elif isinstance(data, list):
            for item in data:
                nested_model_counts = self.recursive_model_search(item, model_names)
                for model, count in nested_model_counts.items():
                    model_counts[model] += count

        return model_counts

    def get_dashboards_models(self, dashboard, model_names):
        """
        Extracts model details from the dashboard elements and counts occurrences of the specified models.

        :param dashboard: The dashboard object to process.
        :param model_names: The list of models to search for in the dashboard elements.
        :return: A tuple with (model_counts, dashboard_title), where model_counts is a dictionary of model counts.
        """
        dashboard_title = dashboard.get('title', 'No Title')
        dashboard_elements = dashboard.get('dashboard_elements', [])

        # Use recursive search to count occurrences of the models
        model_counts = self.recursive_model_search(dashboard_elements, model_names)

        for model, count in model_counts.items():
            if count > 0:
                print(f"Dashboard ID {dashboard['id']} (Title: {dashboard_title}) uses model '{model}' {count} times.")
            else:
                print(f"Dashboard ID {dashboard['id']} (Title: {dashboard_title}) does not use model '{model}'.")

        return model_counts, dashboard_title

    def get_dashboard_metadata(self, dashboard_ids, model_names):
        """
        Retrieves metadata for each dashboard including creation details, model counts, and access details.

        :param dashboard_ids: List of dashboard IDs to retrieve.
        :param model_names: List of model names to search for in the dashboard elements.
        :return: A list of dictionaries with dashboard metadata.
        """
        dashboards_info = []

        for dashboard_id in dashboard_ids:
            response = self.looker_dashboard.get_dashboard_by_id(dashboard_id)

            if response.status_code == 200:
                dashboard = response.json()

                # Call the get_dashboards_models function to get model counts and title
                model_counts, dashboard_title = self.get_dashboards_models(dashboard, model_names)

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
                    'model_counts': model_counts,  # Add model counts to metadata
                    'main_model': dashboard.get('model')
                }
                for model, count in model_counts.items():
                    dashboard_metadata[f'{model}_count'] = count

                dashboards_info.append(dashboard_metadata)
                print(f'All data found for {dashboard_title}')

            else:
                raise Exception(f'Failed to retrieve dashboard {dashboard_id}: {response.content}')

        return dashboards_info
    