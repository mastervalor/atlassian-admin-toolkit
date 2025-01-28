import csv
import os
from calls.okta_api_calls.okta_users_api import OktaUsersCalls
from call import conf_call

admins = ['administrators', 'app-confluence-admin', 'con-coyote-creek', 'con-coyote-creek-confluence', 'system-administrators']
newFile = 'Conf-admins'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Email', 'Group', 'Global Permissions', 'Manager'])
    for j in admins:
        response = conf_call(f'group/{j}/member')

        for i in response['results']:
            email = f'{i["username"]}@getcruise.com'
            manager = OktaUsersCalls.get_user_manager(email)
            writer.writerow([email, j, 'Jira Administrator', manager])
            print(i['username'], email, j, 'jira admin', manager)