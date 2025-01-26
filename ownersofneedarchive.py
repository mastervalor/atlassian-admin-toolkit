from calls.jira_api_calls.jira_api_projects import ProjectJiraCalls
from logic.jira_logic.ticket_logic import Tickets
import csv
import os

projects = ProjectJiraCalls()
tickets = Tickets()

newFile = "owners of done tickets"
newFile2 = "owners of open tickets"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Project Key', 'Project lead'])
    keys = tickets.get_ticket_keys_from_jql('updatedDate <= startOfDay(-730d) and statusCategory = Done')
    owners = projects.project_owners(keys)
    for owner in owners:
        writer.writerow([owner[0], owner[1]])
        print(owner[0], owner[1])

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile2), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Project Key', 'Project lead'])
    keys = tickets.get_ticket_keys_from_jql('updatedDate <= startOfDay(-730d) and statusCategory != Done')
    owners = projects.project_owners(keys)
    for owner in owners:
        writer.writerow([owner[0], owner[1]])
        print(owner[0], owner[1])
