from logic.project_logic import Projects
from logic.os_logic import OSLogic
from dataformating.json_formating import JSONFormating

project_logic = Projects()
os_logic = OSLogic(write_file='all projects')

projects_table = []


projects = project_logic.get_project_owners_and_status()

# project = project.get_project_admins_group('CORPENG')
# project = project.get_project_developer_group('CORPENG')

for project in projects:
    projects_table.append({
        'Name': project['Project'],
        'Key': project['Key'],
        'Approver': project['Name'],
        'Approver status': project['Active'],
        'Admin group': project_logic.get_project_admins_group(project['Key']),
        'Developer group': project_logic.get_project_developer_group(project['Key']),
        'User group': project_logic.get_project_users_group(project['Key']),
        'Agent group':project_logic.get_project_agents_group(project['Key']),
        'Project type': project_logic.get_project_type(project['Key'])
    })

JSONFormating.pretty_json(projects)

