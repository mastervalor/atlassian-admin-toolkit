from logic.project_logic import Projects
from logic.groups_users_logic import GroupsUsers
import json

projects = Projects()
groups = GroupsUsers()
results = projects.get_archived_projects()
jsm_projects = []
jsm_users = []
users_groups = []
final_user_groups = []

for project in results:
    if project['projectTypeKey'] == 'service_desk':
        jsm_projects.append(project['key'])

for project in jsm_projects:
    group = f"app-jira-{project}-agent"
    users = groups.get_group_members_with_status(group)

agent_groups_by_user = []

for project_string in project_strings:
    group_members = groups.get_group_members_with_status(project_string)
    for member in group_members:
        other_groups = groups.user_groups(member)
        agent_groups = [group for group in other_groups if group.endswith("-agent") and group != project_string]
        if agent_groups:
            agent_groups_by_user.append({member: agent_groups})

print(agent_groups_by_user)
