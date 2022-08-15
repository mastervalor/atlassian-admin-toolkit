import requests
import json
import concurrent.futures
from auth import auth
import time

FINAL = []
NAMES = []
TYPES = []
PROJECT = ''


def call(pref, apiAction, payload=''):
    url = "https://lucidmotors.atlassian.net/rest/api/3/" + pref

    if apiAction == 'get':
        headers = {"Accept": "application/json"}
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        ).text

        return json.loads(response)
    elif apiAction == 'put':
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


def setFeilds(final, type, value, i):
    pref = f"issue/{PROJECT}-" + str(i)
    if type == 'string':
        payload = json.dumps({
            "fields": {
                f"customfield_{final}": value
            }
        })
        call(pref, 'put', payload)
    elif type == 'user':
        payload = json.dumps({
            "fields": {
                f"customfield_{final}": {
                    "accountId": value
                }
            }
        })
        call(pref, 'put', payload)


def userProfile(i):
    pref = f"issue/{PROJECT}-" + str(i)
    id = call(pref, 'get')['fields']['reporter']['accountId']
    pref = "user/properties/lucidmotors-userProfile?accountId=" + id
    for (name, type, final) in zip(NAMES, TYPES, FINAL):
        try:
            value = call(pref, 'get')['value'][name]
        except KeyError:
            print(f"Ignoring {PROJECT}-" + str(i) + ", user is no longer active ")
            continue
        if value == "":
            print(f"Ignoring {PROJECT}-" + str(i) + ", user does not have an account profile")
        else:
            print(
                f'The ticket number is {i} and the field id is {final} and the type is {type} and the Value in it is {value}')
            setFeilds(final, type, value, i)


x = 0
while x <= 3:
    PROJECT = input("What is the project KEY? ").upper()
    url = "https://lucidmotors.atlassian.net/rest/api/3/project/" + PROJECT
    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    if response.status_code == 200:
        break
    else:
        x += 1
        print(f"Sorry that's not an exciting project key. {x} out of 4 attempts. Please try again")
else:
    print("Sorry that was 4 attempts, quiting application now.")
    quit()

fields = input("Please enter a list of field IDs you are trying to edit seperated by commas? ").split(",")

for i in fields:
    url = f"https://lucidmotors.atlassian.net/rest/api/3/field/search?id=customfield_{i}"

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    ).text
    if json.loads(response)['total'] == 0:
        fields.append(str(input(f"Looks like {i} is not correct, Please try again: ")))
    else:
        FINAL.append(i)
        NAMES.append(json.loads(response)['values'][0]['name'].lower().split("_", 1)[0].replace(" ", "_"))
        TYPES.append(json.loads(response)['values'][0]['schema']['type'])

t1 = time.perf_counter()

start, end = map(int, input(
    "What ticket number would you like to start with? and what ticket number would you like to end with? ").split())

tickets = list(range(start, end + 1))

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(userProfile, tickets)

t2 = time.perf_counter()

print(f'Finished in {t2 - t1} seconds')
