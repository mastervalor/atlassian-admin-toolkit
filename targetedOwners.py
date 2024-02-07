import json

from call import Jira

jira = Jira()

jql = ('project = "Corporate Engineering" and summary ~ "does not meet the new requirements, and will be targeted for '
       'archiving" and status in ("Waiting for Response", Backlog)')

tickets = jira.jql('?startAt=0&maxResults=100', jql)

for ticket in tickets['issues']:
    description = ticket['fields']['description']
    part = description.split(": ")[1]
    part = part.split(" ")[0]

    owner, status = jira.project_owner(part)

    print(status)
# print(json.dumps(tickets, sort_keys=True, indent=4, separators=(",", ": ")))