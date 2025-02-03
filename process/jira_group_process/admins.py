import csv
import os
from logic.jira_logic.group_logic import Groups
from calls.okta_api_calls.okta_users_api import OktaUsersCalls


sys_admins = ['con-coyote-creek', 'app-jira-system-admin', 'system-administrators']
admins = ['app-jira-admin', 'app-jira-tpm-admin', 'jira-service-accounts-limited-admin', 'jira-administrators']
site = 'site-admins'
newFile = 'UAR-admins'
group_logic = Groups()

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Email', 'Group', 'Global Permissions', 'Manager'])
    for j in admins:
        response = group_logic.group_members(j)

        for i in response['values']:
            manager = OktaUsersCalls.get_user_manager(i['emailAddress'])
            if manager != 'No Manager' and manager != 'Nothing for this one':
                writer.writerow([i['emailAddress'], j, 'Jira Administrator', manager])
            print(i['displayName'], i['emailAddress'], j, 'jira admin', manager)

    for j in sys_admins:
        response = group_logic.group_members(j)

        for i in response['values']:
            manager = OktaUsersCalls.get_user_manager(i['emailAddress'])
            if manager != 'No Manager' and manager != 'Nothing for this one':
                writer.writerow([i['emailAddress'], j, 'System Administrator', manager])
            print(i['displayName'], i['emailAddress'], j, 'System Administrator', manager)

    response = group_logic.group_members(site)

    for i in response['values']:
        manager = OktaUsersCalls.get_user_manager(i['emailAddress'])
        if manager != 'No Manager' and manager != 'Nothing for this one':
            writer.writerow([i['emailAddress'], site, 'Jira Administrator', manager])
        print(i['displayName'], i['emailAddress'], site, 'Jira Administrator', manager)
