from logic.jira_logic.project_logic import Projects


project = Projects()
projects = project.get_project_owners_and_status()

for project in projects:
    if not project['Active']: