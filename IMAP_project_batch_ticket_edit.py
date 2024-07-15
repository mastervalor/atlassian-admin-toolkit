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


def build_values_list(values):
    values_list = []
    for value in values:
        values_list.append(
            {
                "value": value
            },
        )

    return values_list


def build_fields_template(row):
    fields = {}
    if row['Hazardous Behavior']:
        fields["customfield_30300"] = {
            "value": row['Hazardous Behavior']
        }
    if row['Environmental Conditions-related Behaviors']:
        fields["customfield_30301"] = {
            "value": row['Environmental Conditions-related Behaviors']
        }
    if row['Static (Scenery) Elements-related Behaviors']:
        fields["customfield_30403"] = build_values_list(row['Static (Scenery) Elements-related Behaviors'])
    if row['Dynamic Object-related Behaviors']:
        fields["customfield_30404"] = build_values_list(row['Dynamic Object-related Behaviors'])
    if row['Road User Actions']:
        fields["customfield_30400"] = {
            "value": row['Road User Actions']
        }
    if row['ERC Enterprise Risk Level']:
        fields["customfield_26200"] = {
            "value": row['ERC Enterprise Risk Level']
        }

    return {"fields": fields}


def edit_ticket(key, fields_edited):
    url = jira_dev_url + 'issue/' + key
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.request(
        "PUT",
        url,
        headers=headers,
        json=fields_edited,
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


with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), tickets_file), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for ticket in csv_reader:
        fields = build_fields_template(ticket)
        response = edit_ticket(ticket['Key'], fields)
        print(f"Ticket: {ticket['Key']}, edit response code: {response.status_code} and response: {response.text}")
        link_response = add_issue_link(ticket['Key'], ticket['Linked Issue'], ticket['Linked Issue Relation'])
        print(f"Ticket: {ticket['Key']}, edit response code: {link_response.status_code} and response: {link_response.text}")
