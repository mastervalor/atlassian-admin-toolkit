import csv
import os
from call import call, Okta

sys_admins = ['con-coyote-creek', 'app-jira-system-admin', 'system-administrators']
admins = ['app-jira-admin', 'app-jira-tpm-admin', 'jira-service-accounts-limited-admin', 'jira-administrators']
site = 'site-admins'
newFile = 'UAR-admins'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), newFile), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Email', 'Group', 'Global Permissions', 'Manager'])
    for j in admins:
        response = call(f'group/member?groupname={j}', 'get')

        for i in response['values']:
            manager = Okta.okta_call(i['emailAddress'])
            if manager != 'No Manager' and manager != 'Nothing for this one':
                writer.writerow([i['emailAddress'], j, 'Jira Administrator', manager])
            print(i['displayName'], i['emailAddress'], j, 'jira admin', manager)

    for j in sys_admins:
        response = call(f'group/member?groupname={j}', 'get')

        for i in response['values']:
            manager = Okta.okta_call(i['emailAddress'])
            if manager != 'No Manager' and manager != 'Nothing for this one':
                writer.writerow([i['emailAddress'], j, 'System Administrator', manager])
            print(i['displayName'], i['emailAddress'], j, 'System Administrator', manager)

    response = call(f'group/member?groupname={site}', 'get')

    for i in response['values']:
        manager = Okta.okta_call(i['emailAddress'])
        if manager != 'No Manager' and manager != 'Nothing for this one':
            writer.writerow([i['emailAddress'], site, 'Jira Administrator', manager])
        print(i['displayName'], i['emailAddress'], site, 'Jira Administrator', manager)

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
#site-admins