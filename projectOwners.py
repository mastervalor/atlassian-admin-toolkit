from call import Jira
import json
import csv
import os

jira = Jira()
newFile = 'Projects and Owners'
projects = jira.get_projects_with_owners()

# with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
#     writer = csv.writer(new_csv)
#     writer.writerow(['Name', 'Key', 'Project Archived?', 'Owner', 'Owner Status'])
#     for project in projects:
#         writer.writerow([project['name'], project['key'], project['archived'], project['lead']['displayName'],
#                          project['lead']['active']])
#         print(project['name'])

print(json.dumps(projects, sort_keys=True, indent=4, separators=(",", ": ")))