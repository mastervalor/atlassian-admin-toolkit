from call import Jira
import urllib.parse
import json


class Fields:
    def __init__(self):
        self.jira = Jira()

    def field_metrics(self):
        field_metrics = {}
        fields = self.jira.all_fields()
        for field in fields['values']:
            if 'issuesWithValue' not in field or 'issuesWithValue' == 0:
                jql = '"' + field['name'] + '" is not EMPTY'
                encoded = urllib.parse.quote(jql)
                try:
                    results = self.jira.jql("?maxResults=20000", encoded)
                    field['issuesWithValue'] = results['total']
                except KeyError:
                    print(field['name'], results['errorMessages'])

            field_metrics[field['name']] = field

        return field_metrics
