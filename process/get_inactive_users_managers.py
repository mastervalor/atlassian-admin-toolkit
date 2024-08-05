from logic.okta_logic.okta_user_logic import OktaUsers
from logic.jira_logic.ticket_logic import Tickets
from logic.os_logic.os_logic import OSLogic

tickets = Tickets()
os_logic = OSLogic(write_file="inactive and their managers in capa")

assignee_jql = 'project = "Enterprise CAPA" and assignee in inactiveUsers() and statusCategory != Done'
reporter_jql = 'project = "Enterprise CAPA" and reporter in inactiveUsers() and statusCategory != Done'

assignee_results = tickets.get_assignee_from_jql(assignee_jql)
reporter_results = tickets.get_reporter_from_jql(reporter_jql)

inactive_employees = []

for assignee in assignee_results:
    manager, manager_title, manager_status = OktaUsers.get_manager_info(assignee)
    print(f"User: {assignee}, manager: {manager}, manager status: {manager_status}, manager title: {manager_title}")
    inactive_employees.append({
        'Employee Email': assignee,
        'Assingee/reporter': 'Assignee',
        'Manager': manager,
        "Manager status": manager_status,
        "Manager title": manager_title
    })


for reporter in reporter_results:
    manager, manager_title, manager_status = OktaUsers.get_manager_info(reporter)
    print(f"User: {reporter}, manager: {manager}, manager status: {manager_status}, manager title: {manager_title}")
    inactive_employees.append({
        'Employee Email': reporter,
        'Assingee/reporter': 'Reporter',
        'Manager': manager,
        "Manager status": manager_status,
        "Manager title": manager_title
    })




