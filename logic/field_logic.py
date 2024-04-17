from call import Jira
import json


class Fields:
    def __init__(self):
        self.jira = Jira()

    def field_metrics(self):
        fields = self.jira.all_fields()
        for i in fields['values']:
            print(i)