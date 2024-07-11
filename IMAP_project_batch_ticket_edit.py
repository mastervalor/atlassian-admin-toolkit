import requests
import json
import os
import csv

jira_base_url = "https://jira.robot.car/rest/api/2/"
jira_dev_url = "https://jira-dev.robot.car/rest/api/2/"
# fill in first string with username, and second string with token.
auth_token = ('', '')
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
        }
    }
}
edit_ticket(ticket, payload)
