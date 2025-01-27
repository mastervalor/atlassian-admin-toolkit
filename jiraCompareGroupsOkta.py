from logic.okta_logic.okta_user_logic import OktaUsers
from calls import call
import csv
import os
import concurrent.futures

okta_users = OktaUsers()
newfile = "App-jira members 3"

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newfile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Email', 'App-jira in'])
    run = 0
    start = 0
    total = 50
    while start <= total:
        group = call(f'group/member?startAt={start}', 'members', 'app-jira')
        for member in group['values']:
            user = okta_users.get_user_id(member['emailAddress'])
            if user is False:
                writer.writerow([f"Failed on {member['emailAddress']} because not groups"])
                print(f"Failed on {member['emailAddress']} because not groups")
                continue
            groups = OktaUsers.user_groups(user)
            if "app-jira" in groups:
                writer.writerow([member['emailAddress'], "Okta"])
                print(member['emailAddress'], "Okta")
            else:
                writer.writerow([member['emailAddress'], "Jira"])
                print(member['emailAddress'], "Jira")
        start += 50
        print("start is currently at: ", start)
        total = group['total']
