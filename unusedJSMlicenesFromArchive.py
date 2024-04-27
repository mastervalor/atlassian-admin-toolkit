from logic.project_logic import Projects
from logic.groups_users_logic import GroupsUsers
import json

projects = Projects()
groups = GroupsUsers()
results = projects.get_archived_projects()
jsm_projects = []
jsm_users = []
total = 0

for project in results:
    if project['projectTypeKey'] == 'service_desk':
        jsm_projects.append(project['key'])

for project in jsm_projects:
    group = f"app-jira-{project}-agent"
    users = groups.get_group_members_with_status(group)
    #print(f"{group} has: {users}")

    for user in users:
        if not user in jsm_users:
            jsm_users.append(user)

    print(jsm_users)