import requests
from auth import auth, staging_auth
import json
from config import jira, jira_staging


class Jira:
    def __init__(self, is_staging=False):
        self.token = staging_auth if is_staging else auth
        self.jira = jira_staging if is_staging else jira

    def get_workflows(self):
        url = self.jira + "workflow"

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_customField_context(self, fieldId, contextId):
        url = self.jira + f'customFields/{fieldId}/context/{contextId}'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_user(self, payload, pref=''):
        url = self.jira + 'user' + pref

        headers = {
            "Accept": "application/json"
        }
        query = {
            'username': payload,
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response

    def get_project(self, key):
        url = self.jira + 'project/' + key

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_project_groups(self, key, role_id):
        url = self.jira + 'project/' + key + '/role/' + role_id

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_active_projects(self):
        url = self.jira + 'project'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_projects_with_archived(self):
        url = self.jira + 'project'

        headers = {
            "Accept": "application/json"
        }

        query = {
            'includeArchived': True,
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response

    def get_project_permissionscheme(self, key):
        url = self.jira + 'project/' + key + '/permissionscheme?expand=permissions'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def assign_permission_scheme(self, key):
        url = self.jira + 'project/' + key + '/permissionscheme'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def restore_project(self, key):
        url = self.jira + 'project/' + key + '/restore'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def create_ticket(self, ticket):
        url = self.jira + 'issue'

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = json.dumps(ticket)

        response = json.loads(requests.request(
            "POST",
            url,
            headers=headers,
            data=payload,
            auth=self.token
        ).text)

        return response

    def jql(self, pref, payload):
        url = self.jira + 'search' + pref

        headers = {
            "Accept": "application/json"
        }
        query = {
            'jql': payload,
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response

    def tickets(self, query):
        startAt = 0
        maxResults = 1000
        total = 1001
        ticket_list = []

        while total >= maxResults:
            tickets = self.jql(f'?startAt={startAt}&maxResults={maxResults}', query)

            for ticket in tickets['issues']:
                key = ticket['key'].split("-")[0]
                if key not in ticket_list:
                    ticket_list.append(key)

            print(ticket_list)
            total = tickets['total']
            startAt += 1000
            maxResults += 1000

        return ticket_list

    def get_group(self, pref, group):
        url = self.jira + 'group/member' + pref

        headers = {
            "Accept": "application/json"
        }
        query = {
            'groupname': group
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=self.token
        ).text)

        return response

    def group_members(self, group):
        startAt = 0
        maxResults = 50
        total = 51
        members_list = []

        while total >= maxResults:
            members = self.get_group(f'?includeInactiveUsers=false&startAt={startAt}&maxResults={maxResults}', group)

            for member in members['values']:
                members_list.append(member['name'])

            total = members['total']
            startAt += 50
            maxResults += 50
            # print(startAt, maxResults)
        return members_list

    def remove_group_member(self, group, user):
        url = self.jira + 'group/user'

        query = {
            'groupname': group,
            'username': user
        }

        response = requests.request(
            "DELETE",
            url,
            params=query,
            auth=self.token
        ).text

        return response

    def project_owners(self, keys):
        project_owners = []

        for key in keys:
            url = self.jira + 'project/' + key

            headers = {"Accept": "application/json"}

            response = json.loads(requests.request(
                "GET",
                url,
                headers=headers,
                auth=self.token
            ).text)

            project_owners.append([key, response['lead']['name']])

        return project_owners

    def project_owner(self, key):

        url = self.jira + 'project/' + key
        headers = {"Accept": "application/json"}
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)
        try:
            owner = response['lead']['name']
            status = response['lead']['active']
        except KeyError:
            owner = None
            status = None

        return owner, status

    def edit_ticket(self, key, payload):
        url = self.jira + 'issue/' + key
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.request(
            "PUT",
            url,
            headers=headers,
            json=payload,
            auth=self.token
        )

        return response

    def get_my_permissions(self):
        url = self.jira + 'mypermissions'

        headers = {
            "Accept": "application/json",
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_ticket(self, key):
        url = self.jira + 'issue/' + key + '?notifyUsers=false'

        headers = {
            "Accept": "application/json",
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def plugins(self):
        url = self.jira + 'plugins/'

        headers = {
            "Accept": "application/json",
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def get_projects_with_owners(self):
        url = self.jira + 'project?expand=lead'

        headers = {
            "Accept": "application/json",
        }
        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def all_fields(self):
        url = self.jira + "customFields?maxResults=2200"

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def set_project_workflow_scheme(self, key):
        url = self.jira + 'project/' + key + '/workflowscheme'

        headers = {
            "Accept": "application/json"
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def post_issue_type_scheme(self, scheme, keys):
        url = self.jira + 'issuetypescheme/' + scheme + '/associations'

        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            'idsOrKeys': keys
        }

        response = json.loads(requests.request(
            "POST",
            url,
            headers=headers,
            json=payload,
            auth=self.token
        ).text)

        return response

    def unarchive_project(self, key):
        url = self.jira + 'project/' + key + '/restore'

        headers = {
            'Content-Type': 'application/json'
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response

    def archive_project(self, key):
        url = self.jira + 'project/' + key + '/archive'

        headers = {
            'Content-Type': 'application/json'
        }

        response = json.loads(requests.request(
            "PUT",
            url,
            headers=headers,
            auth=self.token
        ).text)

        return response
