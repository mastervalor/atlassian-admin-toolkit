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
            if 'issuesWithValue' in field or 'issuesWithValue' == 0:
                field_metrics[field['name']] = field
            else:
                jql = '"' + field['name'] + '" is not EMPTY'
                encoded = urllib.parse.quote(jql)