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


def process_linked_issues(ticket_key, linked_issues_str, link_types_str):
    if not linked_issues_str or not link_types_str:
        return

    linked_issues = linked_issues_str.split(', ')
    link_types = link_types_str.split(', ')

    for issue, link_type in zip(linked_issues, link_types):
        link_response = add_issue_link(ticket_key, issue, link_type)
        print(
            f"Ticket: {ticket_key}, link response code: {link_response.status_code} and response: {link_response.text}")


with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), tickets_file), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for ticket in csv_reader:
        fields = build_fields_template(ticket)
        response = edit_ticket(ticket['Key'], fields)
        print(f"Ticket: {ticket['Key']}, edit response code: {response.status_code} and response: {response.text}")
        if ticket['Linked Issue'] and ticket['Linked Issue Relation']:
            process_linked_issues(ticket['Key'], ticket['Linked Issues'], ticket['Linked Issue Relations'])
