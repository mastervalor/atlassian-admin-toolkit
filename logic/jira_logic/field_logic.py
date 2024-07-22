from calls.jira import Jira
import urllib.parse
import json


class Fields:
    def __init__(self):
        self.jira = Jira()

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
        field_options = self.jira.get_custom_field_context(field_id, context_id)

        return field_options
