import json
import os
import getpass
import requests
from call import Confluence, Okta
from calls.jira import Jira
from logic.project_logic import Projects
from auth import auth
import re
#
# fileName = "okta groups"
#
# # Get the current username
# username = getpass.getuser()
#
# # Specify the file path
# file_path = '/Users/{}/Desktop/{}.json'.format(username, fileName)
#
# response = Confluence.user_groups("probirsikdar")
#
#
# # Open the JSON file
# with open(file_path, 'r') as json_file:
#     json_data = json.load(json_file)
#
# # Extract group names from the API response and create a set
# api_groups = {group['name'] for group in response['results']}
#
# # Extract group names from the JSON file keys and create a set
# json_groups = set(json_data.keys())
#
# # Find groups in the API response but not in the JSON file
# groups_not_in_json = api_groups - json_groups
#
# # Filter the groups to only include those starting with 'app-confluence'
# filtered_groups = [group for group in groups_not_in_json if group.startswith('app-confluence')]
#
# print("Groups in API response starting with 'app-confluence' but not in JSON file:")
# for group in filtered_groups:
#     print(group)
project = Projects()
jira = Jira()

# user = jira.user_groups('mourad.marzouk')
# plugin = jira.plugins()
#
# print(json.dumps(plugin, sort_keys=True, indent=4, separators=(",", ": ")))

# name, statues = jira.project_owner('EMSTOP')
# print(statues)
# ticket = jira.get_ticket('ITAPP-6255')
# corrected_summary = ticket['fields']['summary'].replace("requirments", "requirements", 1)
# corrected_description = ticket['fields']['description'].replace("Do to this this", "Due to this", 1)
# payload = {
#     "fields": {
#         'summary': corrected_summary,
#         'description': corrected_description
#     }
# }
# correct = jira.edit_ticket(ticket['key'], payload)
# print(ticket['key'])

# query = jira.get_project('ATP')
# print(query['archived'])
# print(query['lead']['displayName'])
# print(query['lead']['name'])
# print(query['lead']['active'])
# user = jira.get_user('brian.derr', '?expand=groups')
# project = jira.get_project_permissionscheme('ITAPP')
# for group in user['groups']['items']:
#     if 'user' in group['name'] or 'developer' in group['name']:
#         split_parts = group['name'].split('-')
#         project = split_parts[2]
#         print(project)
# print(user['active'])
# user = Okta.users_id('mourad.marzouk@getcruise.com')['status']
# print(json.dumps(user, sort_keys=True, indent=4, separators=(",", ": ")))

# def extract_section(input_string):
#     match = re.search(r':\s(\w+)', input_string)
#     if match:
#         return match.group(1)
#     else:
#         return None
#
# tickets = jira.jql('?maxResults=200', 'project = "IT Apps" and "Level of Effort" = "Strategic Work" and '
#                                       'summary ~ "does not meet the new requirements,"')
#
# for i in tickets['issues']:
#     ticket = i['key']
#     key = extract_section(i['fields']['description'])
#     status = i['fields']['status']['name']
#     try:
#         res = i['fields']['resolution']['name']
#     except TypeError:
#         res = None
#     print(ticket, key, status, res)
#
# owner, status = jira.project_owner('ITPROJREQ')
# print(owner, status)
#
# conf = Confluence()
# user = conf.get_user('justin.che')

projects_list = project.get_project_owners_and_status()

for owner in projects_list:
    if not owner['Active']:
        print(owner)

# print(json.dumps(projects_list, sort_keys=True, indent=4, separators=(",", ": ")))