import requests
import json
import os
import csv

jira_base_url = "https://jira.robot.car/rest/api/2/"
jira_dev_url = "https://jira-dev.robot.car/rest/api/2/"
# fill in first string with username, and second string with token.
auth_token = ('mourad.marzouk', 'nKWvwHYaGgB4nD3Ao1MBwJoIwD138kqqGmiWVe')
# fill in target csv file name in string below
tickets_file = ''


def edit_ticket(key, payload):
    url = jira_dev_url + 'issue/' + key
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.request(
        "PUT",
        url,
        headers=headers,
        json=payload,
        auth=auth_token
    )

    return response


def add_issue_link(inward_issue_key, outward_issue_key, link_type):
    url = jira_dev_url + 'issueLink'
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "type": {
            "name": link_type
        },
        "inwardIssue": {
            "key": inward_issue_key
        },
        "outwardIssue": {
            "key": outward_issue_key
        }
    }
    response = requests.request(
        "POST",
        url,
        headers=headers,
        json=payload,
        auth=auth_token
    )
    return response


#
# with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), tickets_file), mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for ticket in csv_reader:
#         fields = {
#
#         }

ticket = 'IMAP-1517'
payload = {
    "fields": {
        "customfield_30300": {
            "value": "Lane Wandering"
        },
        "customfield_30301": {
            "value": "Not Referenced in Report"
        },
        "customfield_30403": [
            {
            "value": "[Lane Changes] - Handling lane change"
            }
        ],
        "customfield_30404": [
            {
            "value": "Not Referenced in Report"
            }
        ],
        "customfield_30400": {
            "value": "Overtaking"
        },
        "customfield_26200": {
            "value": "Extreme"
        }
    }
}
response = edit_ticket(ticket, payload)
print(response.status_code)
print(response.text)

link_response = add_issue_link(ticket, 'IMAP-109', 'Relates')
print(link_response.status_code)
print(link_response.text)
