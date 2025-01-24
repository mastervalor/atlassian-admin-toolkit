import json
from calls. jira_api_calls.jira_api_projects import ProjectJiraCalls

jira = Jira()
archive_list = []

jql = ('project = "Corporate Engineering" and summary ~ "does not meet the new requirements, and will be targeted for '
       'archiving" and status in ("Waiting for Response", Backlog, "In Progress")')

tickets = jira.jql('?startAt=0&maxResults=100', jql)

for ticket in tickets['issues']:
    description = ticket['fields']['description']
    part = description.split(": ")[1]
    part = part.split(" ")[0]
    archive_list.append(part)

projects = jira.get_active_projects()

for project in projects:
    if project['key'] not in archive_list:
        owner, status = jira.project_owner(project['key'])
        print(status)


# print(json.dumps(projects, sort_keys=True, indent=4, separators=(",", ": ")))