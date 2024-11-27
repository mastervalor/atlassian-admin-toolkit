from logic.jira_logic.project_logic import Projects
from logic.os_logic.csv_logic import CSVLogic

project_logic = Projects()
csv_logic = CSVLogic(open_file='Archived Projects final', write_file='all active projects')
file = csv_logic.read_file()

archived_projects = []
projects_table = []


for project in file:
    archived_projects.append(project['Key'])

projects = project_logic.get_project_owners_and_status()

for project in projects:
    if project['Key'] not in archived_projects:
        projects_table.append(project)


csv_logic.write_to_file(projects_table)
