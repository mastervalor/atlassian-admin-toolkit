import json
import os
import getpass
from call import Confluence

fileName = "okta groups"

# Get the current username
username = getpass.getuser()

# Specify the file path
file_path = '/Users/{}/Desktop/{}.json'.format(username, fileName)

response = Confluence.user_groups("probirsikdar")


# Open the JSON file
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Extract group names from the API response and create a set
api_groups = {group['name'] for group in response['results']}

# Extract group names from the JSON file keys and create a set
json_groups = set(json_data.keys())

# Find groups in the API response but not in the JSON file
groups_not_in_json = api_groups - json_groups

# Filter the groups to only include those starting with 'app-confluence'
filtered_groups = [group for group in groups_not_in_json if group.startswith('app-confluence')]

print("Groups in API response starting with 'app-confluence' but not in JSON file:")
for group in filtered_groups:
    print(group)
