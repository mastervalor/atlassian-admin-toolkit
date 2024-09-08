from calls.jira import Jira
import json
import csv
import os

jira = Jira()

tickets = jira.jql('?startAt=0&maxResults=1000', 'project = "IT Apps" and "Level of Effort" = "Strategic Work" and '
                                                 'summary ~ "Project does not meet the new requirments"')
for ticket in tickets['issues']:
    if "requirments" in ticket['fields']['summary']:
        corrected_summary = ticket['fields']['summary'].replace("requirments", "requirements", 1)
        corrected_description = ticket['fields']['description'].replace("Do to this this", "Due to this", 1)
        payload = {
            "fields": {
                'summary': corrected_summary,
                'description': corrected_description
            }
        }
        correct = jira.edit_ticket(ticket['key'], payload)
        print(ticket['key'] + "corrected")
    else:
        print(ticket['key'] + "doesn't need correction")

# print(json.dumps(tickets, sort_keys=True, indent=4, separators=(",", ": ")))
