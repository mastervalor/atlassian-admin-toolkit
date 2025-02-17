import csv
import getpass
import json
import os
from datetime import date
from os import path
from logic.jira_logic.user_logic import Users
from logic.jira_logic.project_logic import Projects

import requests
from requests.auth import HTTPBasicAuth

user_logic = Users()
project_logic = Projects()
key = str(input("What is the project key? "))

url = "https://lucidmotors.atlassian.net/rest/api/2/project/" + key + "/properties"
# url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/2/project/DRM/properties"

auth = HTTPBasicAuth("mouradmarzouk@lucidmotors.com", "10U1uDLf8VHUU6EYb8m3CE0E")

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)
if response.status_code != 200:
    print("Sorry that's not an exciting project key, please try again. Good bye")
    quit()

prefix = 'approvers-'

fileName = str(
    input("Please enter the name of the CSV file and make sure the file is on your desktop(do not enter .csv): "))

if not path.exists('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName)):
    print("Sorry that file name doesn't exist, try again")
    quit()


with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rule in csv_reader:
        if rule["Componant"]:
            propertykey = prefix + rule["Build Phase"] + '--' + rule["Build Area"] + '--' + rule["Componant"]
        else:
            propertykey = prefix + rule["Build Phase"] + '--' + rule["Build Area"]
        propertykey = propertykey.lower()
        propertykey = propertykey.replace(' ', '_')

        urlP = url + "/" + propertykey

        propertyKeyLoad = json.dumps(propertykey, sort_keys=True)

        response = requests.request(
            "PUT",
            urlP,
            data=propertyKeyLoad,
            headers=headers,
            auth=auth
        )

        print(propertyKeyLoad)

        eap = user_logic.get_user_by_id(rule["Engenieering approver Primary"])
        eas = user_logic.get_user_by_id(rule["Engenieering approver Secondary"])
        bap = user_logic.get_user_by_id(rule["Build approver Primary"])
        bas = user_logic.get_user_by_id(rule["Build approver Secondary "])

        # ====== updated property =====

        eapn = str(eap['displayName'])
        easn = str(eas['displayName'])
        bapn = str(bap['displayName'])
        basn = str(bas['displayName'])

        final_property = dict([
            ('engineeringapproverprimary', eap),
            ('engineeringapproversecondary', eas),
            ('buildapproverprimary', bap),
            ('buildapproversecondary', bas),
            ('engineeringapproverprimaryname', eapn),
            ('engineeringapproversecondaryname', easn),
            ('buildapproverprimaryname', bapn),
            ('buildapproversecondaryname', basn),
            ('zdateupdated', date.today().strftime("%m/%d/%Y")),
            ('zdateupdatedname', getpass.getuser())])

        payload = json.dumps(final_property, sort_keys=True)

        response = requests.request(
            "PUT",
            urlP,
            data=payload,
            headers=headers,
            auth=auth
        )

        print(payload)
