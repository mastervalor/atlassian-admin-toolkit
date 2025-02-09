from logic.jira_logic.project_logic import Projects


project_logic = Projects()
group = "administrators"
project_key = ''

print(project_logic.add_group_admins_to_project(group, project_key))
