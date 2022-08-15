import requests
from auth import auth
import json
import csv
import os

def call(id,value):
    url = "https://lucidmotors.atlassian.net/rest/api/3/issue/" + str(id)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "fields": {
            "customfield_13854": {
                "id": value
            }
        }
    })

    response = requests.request(
        "PUT",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    print(response)


with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), 'assessment'), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rule in csv_reader:
        if rule["Custom field (Assessment)"] == "2 - Hardware Change likely":
            call(rule["Issue id"], '17552')
        if rule["Custom field (Assessment)"] == "0 - Unknown":
            call(rule["Issue id"], '17551')
        if rule["Custom field (Assessment)"] == "1 - Hardware & Software Change likely":
            call(rule["Issue id"], '17553')
        if rule["Custom field (Assessment)"] == "3 - Software Change likely":
            call(rule["Issue id"], '17554')
        if rule["Custom field (Assessment)"] == "4 - No Change to Hardware or Software":
            call(rule["Issue id"], '17556')
        elif rule["Custom field (Assessment)"] == "":
            continue

