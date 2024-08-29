from logic.jira_logic.project_logic import Projects
from logic.okta_logic.okta_user_logic import OktaUsers
from logic.jira_logic.ticket_logic import Tickets

tickets = Tickets()
project = Projects()
projects = project.get_project_owners_and_status()

for project in projects:
    if not project['Active']:
        manager, manager_title, manager_status  = OktaUsers.get_manager_info(project['Username'])
        ticket_info = {
            'summary': f"project: {project['project']}, Key: {project['Key']} no longer has and active owner.",
            'assignee': 'mourad.marzouk',
            'description': f"project: {project['project']}, Key: {project['Key']} no longer has and active owner."
                           f"Last owner is {project['Name']} and we need to find a replacement."
                           f"Their listed manager is {manager}, Title{manager_title}, Status{manager_status}",
            'parent ticket': "CORPENG-12665"
        }

        tickets.build_ticket_payload(ticket_info)
        