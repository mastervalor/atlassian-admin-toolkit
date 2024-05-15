from logic.project_logic import Projects
from logic.groups_users_logic import GroupsUsers
from logic.user_logic import Users
import csv, os

projects = Projects()
groups = GroupsUsers()
users = Users()
results = projects.get_archived_projects()
jsm_projects_keys = []
newFile = 'former jsm users'

for project in results:
    if project['projectTypeKey'] == 'service_desk':
        jsm_projects_keys.append(project['key'])

project_strings = [f"app-jira-{project}-agent".lower() for project in jsm_projects_keys]

agent_groups_by_user = []

for project_string in project_strings:
    group_members = groups.get_group_members_with_status(project_string)
    for member in group_members:
        other_groups = users.user_groups(member)
        agent_groups = [group for group in other_groups if group.endswith("-agent")]
        archived_project_groups = []
        non_archived_project_groups = []
        for agent_group in agent_groups:
            if agent_group in project_strings:
                archived_project_groups.append(agent_group)
            else:
                non_archived_project_groups.append(agent_group)
        # Append user dictionary with agent groups categorized by project type
        agent_groups_by_user.append({'name': member, 'archived_projects_agent_groups': archived_project_groups,
                                     'non_archived_projects_agent_groups': non_archived_project_groups})

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Name', 'Archived_projects_agent_groups', 'Non_archived_projects_agent_groups'])

    for agent in agent_groups_by_user:
        writer.writerow([agent['name'], agent['archived_projects_agent_groups'],
                         agent['non_archived_projects_agent_groups']])


# print(json.dumps(agent_groups_by_user, sort_keys=True, indent=4, separators=(",", ": ")))