from logic.project_logic import Projects
from logic.os_logic import OSLogic

projects = Projects()
os_logic = OSLogic(open_file='Archived projects')
file = os_logic.read_file()
project_list = []
for project in file:
    project_list.append(project['project_key'])

responses = projects.unarchive_projects_list(project_list)

print(responses)