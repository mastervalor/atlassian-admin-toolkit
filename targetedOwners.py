from logic.jira_logic.project_logic import Projects
from calls.jira_api_calls.jira_api_projects import ProjectJiraCalls
from calls.jira_api_calls.jira_api_tickets import TicketsJiraCalls

project_logic = Projects()
ticket_calls = TicketsJiraCalls()
archive_list = []

jql = ('project = "Corporate Engineering" and summary ~ "does not meet the new requirements, and will be targeted for '
       'archiving" and status in ("Waiting for Response", Backlog, "In Progress")')

tickets = ticket_calls.jql('?startAt=0&maxResults=100', jql)

for ticket in tickets['issues']:
    description = ticket['fields']['description']
    part = description.split(": ")[1]
    part = part.split(" ")[0]
    archive_list.append(part)

projects = project_logic.get_active_projects()

for project in projects:
    if project['key'] not in archive_list:
        owner, status = project_logic.get_project_owner_with_status(project['key'])
        print(status)

# print(json.dumps(projects, sort_keys=True, indent=4, separators=(",", ": ")))
