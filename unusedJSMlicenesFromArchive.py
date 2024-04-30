from logic.project_logic import Projects
from logic.groups_users_logic import GroupsUsers
import json

projects = Projects()
groups = GroupsUsers()
results = projects.get_archived_projects()
jsm_projects = []
jsm_users = []
users_groups = []

for project in results:
    if project['projectTypeKey'] == 'service_desk':
        jsm_projects.append(project['key'])

for project in jsm_projects:
    group = f"app-jira-{project}-agent"
    users = groups.get_group_members_with_status(group)

    for user in users:
        if user not in jsm_users:
            jsm_users.append({user: group})

for user_group in jsm_users:
    for user, group in user_group.items():
        looking_groups = groups.user_groups(user)
        for looking_group in looking_groups:
            if looking_group.endswith("-agent") and looking_group != group:
                print(f"{user}: {group}")
