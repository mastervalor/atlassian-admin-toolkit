from call import call, Jira
import csv
import os

jira = Jira()


newFile = "owners of done tickets"
newFile2 = "owners of open tickets"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Project Key', 'Project lead'])
    keys = jira.tickets('updatedDate <= startOfDay(-730d) and statusCategory = Done')
    owners = jira.project_owners(keys)
    for owner in owners:
        writer.writerow([owner[0], owner[1]])
        print(owner[0], owner[1])

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile2), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Project Key', 'Project lead'])
    keys = jira.tickets('updatedDate <= startOfDay(-730d) and statusCategory != Done')
    owners = jira.project_owners(keys)
    for owner in owners:
        writer.writerow([owner[0], owner[1]])
        print(owner[0], owner[1])