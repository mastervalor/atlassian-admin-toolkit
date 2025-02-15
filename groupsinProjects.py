import requests
from auth import auth
import json
import csv
import os
from logic.confluence_logic.groups_logic import ConfGroupLogic
from logic.confluence_logic.space_logic import Spaces
from logic.jira_logic.project_logic import Projects
from logic.jira_logic.user_logic import Users

project_roles = ['10001', '10002', '10301', '10000', '10300', '10425', '10432']
project_type = ['developers', 'admins', 'agents', 'users', 'customers', 'suppliers', 'read-only']
new_file = 'project role groups and users 3'
conf_groups = ConfGroupLogic()
conf_space_logic = Spaces()
jira_project_logic = Projects()
user_logic = Users()

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), new_file), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['jira', 'Project key', 'Role', 'Cost Center'])
    projects = jira_project_logic.get_active_projects()
    for project in projects:
        for (role, p_type) in zip(project_roles, project_type):
            groupName = jira_project_logic.get_project_users_by_role(project["key"], role)
            if 'actors' in groupName:
                emails = []
                costCenters = []
                users = []
                for x in groupName['actors']:
                    if x['displayName'] != 'administrators':
                        if x['displayName'].startswith('CC-') or x['displayName'].startswith('DEPT-') or \
                                x['displayName'].startswith('grp-') or x['displayName'].startswith('okta_'):
                            costCenters.append(x['displayName'])
                        else:
                            names = conf_groups.get_group_users_email(x['displayName'])
                            if 'errorMessages' in names:
                                user = user_logic.get_user_by_id(x['actorUser']['accountId'])
                                try:
                                    users.append(user['emailAddress'])
                                except KeyError:
                                    print(x['actorUser']['accountId'], x['displayName'], project['key'], role)
                            if 'values' in names:
                                for y in names['values']:
                                    try:
                                        emails.append(y['emailAddress'])
                                    except KeyError:
                                        print(y['accountId'], y['displayName'], project['key'], role)
                if costCenters or emails or users:
                    writer.writerow(['jira', project['key'], p_type, costCenters + emails + users])
