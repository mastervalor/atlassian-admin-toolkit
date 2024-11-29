from logic.jira_logic.project_logic import Projects
from file_manip.csv_file_manip import CSVLogic
import json

projects = Projects()
csv_logic = CSVLogic(open_file='Archived projects')
file = csv_logic.read_file()
project_list = []

for project in file:
    project_list.append(project['project_key'])


responses = projects.archive_projects_list(project_list)

responses_json = json.dumps(responses, indent=4)

print(responses_json)
