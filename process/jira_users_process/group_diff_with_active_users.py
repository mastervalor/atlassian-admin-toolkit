import json
import os
import csv
from logic.os_logic.os_logic import OSLogic
from logic.jira_logic.groups_users_logic import GroupsUsers
from logic.okta_logic.okta_user_logic import OktaUsers
from call import Jira, Okta

group_users = GroupsUsers()

newFile = 'not in app-jira with status'
openFile = 'not in app-jira'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Username', 'access group', 'status', 'in okta'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            status = group_users.get(i['Username'])['active']
            okta = Okta.users_id(f"{i['Username']}@getcruise.com")
            if okta:
                okta = okta['status']
            writer.writerow([i['Username'], i['access group'], status, okta])
            print(f"User {i['Username']} is active: {status} and oka: {okta}")