from calls.jira_api_calls.jira_api_tickets import TicketsJiraCalls
import json


class Tickets:
    def __init__(self):
        self.tickets = TicketsJiraCalls()

    def build_ticket_payload(self, ticket_info):
        payload = {
            'fields': {
                'project': {
                    'key': 'CORPENG',
                },
                'summary': ticket_info['summary'],
                "issuetype": {
                    "id": "3"
                },
                "reporter": {
                    "name": 'mourad.marzouk'
                },
                "assignee": {
                    "name": ticket_info["assignee"]
                },
                "customfield_16774": [{
                    "value": "Project"
                }],
                "customfield_28001": {
                    'value': "Jira",
                    "child": {
                        'value': "Other"
                    }
                },
                "description": ticket_info['description'],
            },
            "update": {
                "issuelinks": [
                    {
                        "add": {
                            "type": {
                                "name": "Problem/Incident",
                                "inward": "is caused by",
                                "outward": "causes"
                            },
                            "outwardIssue": {
                                "key": ticket_info['parent ticket']
                            }
                        }
                    }
                ]
            }
        }

        response = self.tickets.create_ticket(payload)
        print(response)

    def build_values_list(self, values):
        if not values:
            return []
        values_list = []
        for value in values.split(', '):
            values_list.append(
                {
                    "value": value.strip()
                },
            )
        return values_list

    def process_linked_issues(self, ticket_key, linked_issues_str, link_types_str):
        if not linked_issues_str or not link_types_str:
            return

        linked_issues = linked_issues_str.split(', ')
        link_types = link_types_str.split(', ')

        for issue, link_type in zip(linked_issues, link_types):
            link_response = self.tickets.add_issue_link(ticket_key, issue, link_type)
            print(
                f"Ticket: {ticket_key}, link response code: {link_response.status_code} and response: {link_response.text}")

    def get_ticket_keys_from_jql(self, query):
        startAt = 0
        maxResults = 1000
        total = 1001
        ticket_list = []

        while total >= maxResults:
            tickets = self.tickets.jql(f'?startAt={startAt}&maxResults={maxResults}', query)

            for ticket in tickets['issues']:
                key = ticket['key']
                if key not in ticket_list:
                    ticket_list.append(key)

            total = tickets['total']
            startAt += 1000
            maxResults += 1000

        return ticket_list

    def get_assignee_from_jql(self, query):
        startAt = 0
        maxResults = 1000
        total = 1001
        assignee_list = []

        while total >= maxResults:
            tickets = self.tickets.jql(f'?startAt={startAt}&maxResults={maxResults}', query)

            for ticket in tickets['issues']:
                key = ticket['fields']['assignee']['emailAddress']
                if key not in assignee_list:
                    assignee_list.append(key)

            total = tickets['total']
            startAt += 1000
            maxResults += 1000

        return assignee_list

    def get_reporter_from_jql(self, query):
        startAt = 0
        maxResults = 1000
        total = 1001
        reporter_list = []

        while total >= maxResults:
            tickets = self.tickets.jql(f'?startAt={startAt}&maxResults={maxResults}', query)

            for ticket in tickets['issues']:
                key = ticket['fields']['reporter']['emailAddress']
                if key not in reporter_list:
                    reporter_list.append(key)

            total = tickets['total']
            startAt += 1000
            maxResults += 1000

        return reporter_list

    def assign_ticket(self, ticket, assignee):
        response = self.tickets.assign_ticket(ticket, assignee)

        if response.status_code == 204:
            print(f"Issue {ticket} successfully assigned to {assignee}.")
        elif response.status_code == 400:
            print("Error: Problem with the received user representation.")
        elif response.status_code == 401:
            print("Error: Calling user does not have permission to assign the issue.")
        elif response.status_code == 404:
            print("Error: Either the issue or the user does not exist.")
        else:
            print(f"Error: Unexpected response code {response.status_code}. Response: {response.text}")

    def assign_reporter_ticket(self, ticket, reporter):
        response = self.tickets.assign_ticket(ticket, reporter)

        if response.status_code == 204:
            print(f"Issue {ticket} successfully assigned to {reporter}.")
        elif response.status_code == 400:
            print("Error: Problem with the received user representation.")
        elif response.status_code == 401:
            print("Error: Calling user does not have permission to assign the issue.")
        elif response.status_code == 404:
            print("Error: Either the issue or the user does not exist.")
        else:
            print(f"Error: Unexpected response code {response.status_code}. Response: {response.text}")

    def clear_field(self, key, field):
        """
            Clears the values from a field of a Jira issue.

            Args:
            - key (str): The key of the Jira issue to update.
            - field (str): The field of the Jira issue to be cleared.

            Returns:
            - response (dict): The response from the Jira API call.
        """
        payload = {
            "fields": {
                field: []
            }
        }

        response = self.tickets.edit_ticket(key, payload)

        return response

    def set_fields(self, issue, fields):
        payload = {
            "fields": {}
        }

        for key, values in fields.items():
            payload["fields"][key] = values

        response = self.tickets.edit_ticket(issue, payload)

        print(response.text)
        return response

    def get_all_users_comments(self, user_name, ticket_key):
        comments = self.tickets.get_ticket_comments(ticket_key)['comments']
        users_comments = []
        for comment in comments:
            if comment['author']['displayName'] == user_name:
                users_comments.append(comment)

        return users_comments

    def get_users_comment_ids(self, user_name, ticket_key):
        users_comments = self.get_all_users_comments(user_name, ticket_key)
        comment_ids = []
        for comment in users_comments:
            comment_ids.append(comment['id'])

        return comment_ids

    def delete_user_comments(self, ticket_key, comment_ids):
        """Deletes multiple comments from a Jira issue and returns results."""
        results = []

        for comment_id in comment_ids:
            response = self.tickets.delete_ticket_comment(ticket_key, comment_id)

            if "error" in response:
                results.append({"comment_id": comment_id, "status": "failed", "details": response["error"]})
            else:
                results.append({"comment_id": comment_id, "status": "deleted"})

        return results

    def get_tickets_from_jql(self, query):
        start_at = 0
        max_results = 1000
        total = 1001
        ticket_list = []

        while total >= max_results:
            tickets = self.tickets.jql(f'?startAt={start_at}&maxResults={max_results}', query)

            for ticket in tickets['issues']:
                ticket_list.append(ticket)

            total = tickets['total']
            start_at += 1000
            max_results += 1000

        return ticket_list

    def get_ticket_by_key(self, key):
        ticket = self.tickets.get_ticket(key)
        return ticket
