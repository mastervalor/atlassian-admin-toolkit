import json
import os
import csv
import getpass
from logic.confluence_logic.user_logic import ConfUserLogic

newFile = "Jira Group Match"
openFile = "app-jira members"
fileName = "app-jira-group-memberships-20230712"

# Get the current username
username = getpass.getuser()
conf_user = ConfUserLogic()

# Specify the file path
file_path = '/Users/{}/Desktop/{}.json'.format(username, fileName)

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Username', 'groups not in okta'])
    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
        for user in csv_reader:
            response = conf_user.get_users_groups(user['username'])
            # Extract group names from the API response and create a dict
            try:
                api_groups = {group['name'] for group in response['results']}
                # Extract group names from the JSON file keys and create a set
                json_groups = set(json_data.keys())
                # Find groups in the API response but not in the JSON file
                groups_not_in_json = api_groups - json_groups
                # Filter the groups to only include those starting with 'app-confluence'
                filtered_groups = [group for group in groups_not_in_json if group.startswith('app-confluence')]
                writer.writerow([user['username'], filtered_groups])
                print([user['username'], filtered_groups])
            except KeyError:
                writer.writerow([user['username'], "couldn't find user"])
                print([user['username'], "couldn't find user"])
