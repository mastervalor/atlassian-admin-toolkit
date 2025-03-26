from logic.okta_logic.okta_user_logic import OktaUsers
from logic.jira_logic.group_logic import Groups
import csv
import os
import concurrent.futures

okta_users = OktaUsers()
group_logic = Groups()
newfile = "App-jira members 3"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newfile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Email', 'App-jira in'])
    group = group_logic.group_members('app-jira')
    for member in group:
        user = okta_users.get_user_id(member)
        if user is False:
            writer.writerow([f"Failed on {member} because not groups"])
            print(f"Failed on {member} because not groups")
            continue
        groups = OktaUsers.user_groups(user)
        if "app-jira" in groups:
            writer.writerow([member, "Okta"])
            print(member, "Okta")
        else:
            writer.writerow([member, "Jira"])
            print(member, "Jira")
    total = group['total']
