import json
import os
import csv
import getpass
from call import Jira

newFile = "Jira Group Match 2"
openFile = "app-jira members"
fileName = "app-jira-group-memberships-20230712"

# Get the current username
username = getpass.getuser()
jira = Jira()

# Specify the file path
file_path = '/Users/{}/Desktop/{}.json'.format(username, fileName)

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Username', 'groups not in okta'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
            json_groups = set(json_data.keys())
        for user in csv_reader:
            response = jira.user_groups(user['username'])
            filtered_groups = []
            try:
                for group in response:
                    if group.startswith('app-jira'):
                        okta_group_users = json_data[group]
                        if (user['username']) not in okta_group_users:
                            filtered_groups.append(group)

                writer.writerow([user['username'], filtered_groups])
                print([user['username'], filtered_groups])
            except KeyError:
                writer.writerow([user['username'], "couldn't find user"])
                print([user['username'], "couldn't find user"])