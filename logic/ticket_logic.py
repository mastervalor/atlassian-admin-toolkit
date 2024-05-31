from call import Jira
import json


class Tickets:
    def __init__(self):
        self.jira = Jira()

    def build_ticket_payload(self, ticket_info):
        payload = {
            'fields': {
                'project': {
                    'key': 'CORPENG',
                },
                'summary': ticket_info['summary'],
                "issuetype": {
                    "id": "3"
                },
                "reporter": {
                    "name": 'mourad.marzouk'
                },
                "assignee": {
                    "name": ticket_info["assignee"]
                },
                "customfield_18672": {
                    "value": "Strategic Work"
                },
                "customfield_28001": {
                    'value': "Jira",
                    "child": {
                        'value': "Other"
                    }
                },
                "description": ticket_info['description'],
            },
            "update": {
                "issuelinks": [
                    {
                        "add": {
                            "type": {
                                "name": "Problem/Incident",
                                "inward": "is caused by",
                                "outward": "causes"
                            },
                            "outwardIssue": {
                                "key": ticket_info['parent ticket']
                            }
                        }
                    }
                ]
            }
        }

        response = self.jira.create_ticket(payload)
        print(response)
