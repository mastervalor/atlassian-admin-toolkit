from calls.jira_api_calls.jira_api_system import SystemJiraCalls


class JiraSystemsLogic:
    def __init__(self):
        self.jira_system = SystemJiraCalls()

    def get_all_issue_types(self):
        issue_types = self.jira_system.issue_types()
        return issue_types

    def get_all_permission_schemes(self):
        permission_schemes = self.jira_system.permission_schemes()
        return permission_schemes
    