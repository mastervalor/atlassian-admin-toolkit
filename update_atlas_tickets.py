from auth import auth
import json
import requests
import csv
import os
import concurrent.futures
from tabulate import tabulate


def put(pref, project):
    url = f"https://lucidmotors.atlassian.net/rest/api/3/issue/" + pref

    payload = json.dumps({
        "fields": {
            "customfield_14052": {
                "key": project
            },
            "customfield_14116": {
                "value": "Jira"
            }
        }
    })
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.request(
        "PUT",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    print(response)
    print(f'Edited {pref} to value of {project}')


def call(pref):
    url = f"https://lucidmotors.atlassian.net/rest/api/3/issue/" + pref
    headers = {
        "Accept": "application/json"
    }

    response = json.loads(requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    ).text)

    return response


def fill_in(ticket):
    try:
        response = call(ticket)
    except ConnectionError:
        print(f"failed call on {ticket}")
    try:
        response['fields']['summary']
        for (project, name) in zip(projects, names):
            if project in response['fields']['summary']:
                put(ticket, project)
                break
            elif name in response['fields']['summary']:
                put(ticket, project)
                break
        else:
            print(f'Nothing was changed in {ticket}')
    except KeyError:
        print(f"This isn't there on {ticket}")
    except AttributeError:
        print(f"This ticket is attribute none {ticket}")
    except TypeError:
        print(f"This ticket is type none {ticket}")


mainFile = 'tickets3'

url_p = "https://lucidmotors.atlassian.net/rest/api/3/project"

headers = {
    "Accept": "application/json"
}

response = json.loads(requests.request(
    "GET",
    url_p,
    headers=headers,
    auth=auth
).text)

projects = []
names = []
tickets = []

for i in response:
    projects.append(i['key'])
    names.append(i['name'])

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), mainFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        tickets.append(i['Ticket Key'])

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(fill_in, tickets)
