from auth import okta_token
import requests
import json


class Okta:

        # example
        # for j in admins:
        #     try:
        #         response = Okta.okta_groups(j)
        #         for name in response:
        #             manager = Okta.okta_call(name['profile']['email'])
        #             if manager != 'No Manager' and manager != 'Nothing for this one':
        #                 writer.writerow([name['profile']['email'], j, 'System Administrator', manager])
        #             print(name['profile']['email'], j, 'System admin', manager)
        #     except IndexError:
        #         response = call(f'group/member?groupname={j}', 'get')
        #         try:
        #             for i in response['values']:
        #                 manager = Okta.okta_call(i['emailAddress'])
        #                 if manager != 'No Manager' and manager != 'Nothing for this one':
        #                     writer.writerow([i['emailAddress'], j, 'Jira Administrator', manager])
        #                 print(i['displayName'], i['emailAddress'], j, 'System Administrator', manager)
        #         except KeyError:
        #             print(j)
