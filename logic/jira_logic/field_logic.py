from calls.jira_api_calls.jira_api_custom_fields import CustomFieldsJiraCalls
import urllib.parse
import json


class Fields:
    def __init__(self):
        self.custom_fields = CustomFieldsJiraCalls()

    def field_metrics(self):
        field_metrics = []
        fields = self.jira.all_fields()
        for field in fields['values']:
            if 'issuesWithValue' not in field or field['issuesWithValue'] == 0:
                jql = f"'{field['name']}' is not EMPTY"
                try:
                    results = self.jira.jql("", jql)
                    field['issuesWithValue'] = results['total']
                except KeyError:
                    print(field['name'], results['errorMessages'])
                    field['notes'] = results['errorMessages']
            field_metrics.append(field)
            print(field)
        return field_metrics

    def field_options(self, field_id, context_id):
        field_options = self.custom_fields.get_custom_field_context(field_id, context_id)

        return field_options
