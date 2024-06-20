from logic.project_logic import Projects
from logic.os_logic import OSLogic

project = Projects()
os_logic = OSLogic(write_file='all projects')

projects_table = []


# projects = project.get_project_owners_and_status()

print(project.get_project_admins_group('CORPENG'))

