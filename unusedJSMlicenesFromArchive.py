from logic.project_logic import Projects
from logic.groups_users_logic import GroupsUsers
import json

projects = Projects()
groups = GroupsUsers()
results = projects.get_archived_projects()
jsm_projects_keys = []

for project in results:
    if project['projectTypeKey'] == 'service_desk':
        jsm_projects_keys.append(project['key'])

project_strings = [f"app-jira-{project}-agent" for project in jsm_projects_keys]

agent_groups_by_user = []

for project_string in project_strings:
    group_members = groups.get_group_members_with_status(project_string)
    for member in group_members:
        other_groups = groups.user_groups(member)
        agent_groups = [group for group in other_groups if group.endswith("-agent")]
        archived_project_groups = []
        non_archived_project_groups = []
        for agent_group in agent_groups:
            if agent_group in project_strings:
                archived_project_groups.append(agent_group)
            else:
                non_archived_project_groups.append(agent_group)
        # Append user dictionary with agent groups categorized by project type
        agent_groups_by_user.append({member: {'archived_projects_agent_groups': archived_project_groups,
                                              'non_archived_projects_agent_groups': non_archived_project_groups}})

print(json.dumps(agent_groups_by_user, sort_keys=True, indent=4, separators=(",", ": ")))