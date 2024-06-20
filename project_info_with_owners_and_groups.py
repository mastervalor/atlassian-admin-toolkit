from logic.project_logic import Projects
from logic.os_logic import OSLogic
from dataformating.json_formating import JSONFormating

project_logic = Projects()
os_logic = OSLogic(open_file='Archived projects - projects to standerdize', write_file='all projects')
file = os_logic.read_file()
archived_projects = []
projects_table = []

for project in file:
    archived_projects.append(project['project_key'])

def project_info():
    projects_table = []
    projects = project_logic.get_project_owners_and_status()

    for project in projects:
        if project['Key'] not in archived_projects:
            projects_table.append(project_logic.build_project_table(project['Project'], project['Key'], project['Name'],
                                                                    project['Active']))

    return projects_table

