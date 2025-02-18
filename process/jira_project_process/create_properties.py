import csv
import getpass
import os
from datetime import date
from os import path
from logic.jira_logic.user_logic import Users
from logic.jira_logic.project_logic import Projects


user_logic = Users()
project_logic = Projects()
key = str(input("What is the project key? "))

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
            property_key = prefix + rule["Build Phase"] + '--' + rule["Build Area"] + '--' + rule["Componant"]
        else:
            property_key = prefix + rule["Build Phase"] + '--' + rule["Build Area"]
        property_key = property_key.lower()
        property_key = property_key.replace(' ', '_')

        project_logic.set_project_properties(key, property_key)

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

        project_logic.set_project_properties(key, final_property)
