from logic.project_logic import Projects
import json

projects = Projects()
results = projects.get_archived_projects()
jsms = []

for project in results:
    if project['projectTypeKey'] == 'service_desk':
        jsms.append(project)

print(json.dumps(jsms, sort_keys=True, indent=4, separators=(",", ": ")))