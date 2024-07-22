from calls.jira import Jira
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
                "customfield_16774": [{
                    "value": "RTB"
                }],
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

    def build_values_list(self, values):
        if not values:
            return []
        values_list = []
        for value in values.split(', '):
            values_list.append(
                {
                    "value": value.strip()
                },
            )
        return values_list

    def process_linked_issues(self, ticket_key, linked_issues_str, link_types_str):
        if not linked_issues_str or not link_types_str:
            return

        linked_issues = linked_issues_str.split(', ')
        link_types = link_types_str.split(', ')

        for issue, link_type in zip(linked_issues, link_types):
            link_response = self.jira.add_issue_link(ticket_key, issue, link_type)
            print(
                f"Ticket: {ticket_key}, link response code: {link_response.status_code} and response: {link_response.text}")
