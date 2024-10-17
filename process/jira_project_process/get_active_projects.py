from logic.jira_logic.project_logic import Projects
from logic.os_logic.os_logic import OSLogic

project_logic = Projects()
os_logic = OSLogic(open_file='Archived Projects final', write_file='all active projects')
file = os_logic.read_file()

archived_projects = []
projects_table = []


for project in file:
    archived_projects.append(project['Key'])

projects = project_logic.get_project_owners_and_status()

for project in projects:
