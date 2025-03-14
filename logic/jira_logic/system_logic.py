from calls.jira_api_calls.jira_api_system import SystemJiraCalls


class Systems:
    def __init__(self):
        self.jira_system = SystemJiraCalls()

    def get_all_issue_types(self):
        issue_types = self.jira_system.issue_types()
        return issue_types
