from auth import okta_token
import requests
import json


class Okta:

    @classmethod
    def get_group_id(cls, name):
        url = 'https://cruise.okta.com/api/v1/groups'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            groups = json.loads(response.text)
            for group in groups:
                if group['profile']['name'] == name:
                    return group['id']
            return "Group not found."
        else:
            return f"Failed to retrieve group ID. Status code: {response.status_code}"

    @classmethod
    def add_user_to_group(cls, user_id, group_id):
        url = f"https://cruise.okta.com/api/v1/groups/{group_id}/users/{user_id}"
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }
        response = requests.put(url, headers=headers)
        return response.status_code

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
