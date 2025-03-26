import json
import getpass

fileName = "app-jira-group-memberships-20230712"
newfile = "okta jira groups"
username = getpass.getuser()

file_path = '/Users/{}/Desktop/{}.json'.format(username, fileName)
new = '/Users/{}/Desktop/{}.json'.format(username, fileName)

with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

converted_data = {}
for group, members in json_data.items():
    converted_members = []
    for member in members:
        username = member.split('@')[0]
        converted_members.append(username)
    print(group)
    converted_data[group] = converted_members

with open(new, 'w') as newFile:
    json.dump(converted_data, newFile, indent=4)

