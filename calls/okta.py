


class Okta:
    def __init__(self, name, email, id, user_id, group_id):
        self.name = name
        self.email = email
        self.id = id
        self.users_id = user_id
        self.group_id = group_id

    @classmethod
    def users_id(cls, email):
        url = 'https://cruise.okta.com/api/v1/users'
        email = email
        params = {'filter': 'profile.email eq "{0}"'.format(email)}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }

        response = requests.get(url, headers=headers, params=params)
        try:
            return json.loads(response.text)[0]
        except IndexError:
            return False

    # @classmethod
    # def users_manager(cls, email):
    @classmethod
    def get_user_groups(cls, id):
        groups_url = f'https://cruise.okta.com/api/v1/users/{id}/groups'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }
        response = requests.get(groups_url, headers=headers, timeout=9000)
        groups_json = response.json()
        groups = [group['profile']['name'] for group in groups_json]
        return groups

    @classmethod
    def okta_call(cls, email):
        url = 'https://cruise.okta.com/api/v1/users'
        email = email
        params = {'filter': 'profile.email eq "{0}"'.format(email)}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }

        response = requests.get(url, headers=headers, params=params)
        try:
            manager = json.loads(response.text)[0]['profile']['manager']
            if not manager:
                return 'empty'
            else:
                return manager
        except KeyError:
            return 'No Manager'
        except IndexError:
            return 'Nothing for this one'

    @classmethod
    def okta_groups(cls, name):
        url = f'https://cruise.okta.com/api/v1/groups?q={name}'

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }

        response = requests.get(url, headers=headers)

        id = json.loads(response.text)[0]['id']

        url = f'https://cruise.okta.com/api/v1/groups/{id}/users'

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': okta_token
        }

        response = requests.get(url, headers=headers)

        return json.loads(response.text)

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
            response = json.loads(response.text)
        for i in response:
            if i['profile']['name'] == name:
                return i['id']
        else:
            return f"Failed to retrieve group ID. Status code: {response.status_code}"

        return None

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
