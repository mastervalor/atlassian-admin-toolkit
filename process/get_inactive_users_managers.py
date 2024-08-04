from logic.okta_logic.okta_user_logic import OktaUsers
from logic.jira_logic.ticket_logic import Tickets

tickets = Tickets()

assignee_jql = 'project = "Enterprise CAPA" and assignee in inactiveUsers() and statusCategory != Done'

reporter_jql = 'project = "Enterprise CAPA" and reporter in inactiveUsers() and statusCategory != Done'

assignee_results = tickets.get_assignee_from_jql(assignee_jql)
for assignee in assignee_results:
    manger = OktaUsers.get_user_manager(assignee)
    print(manger)


reporter_results = tickets.get_reporter_from_jql(reporter_jql)
for reporter in reporter_results:
    manger = OktaUsers.get_user_manager(reporter)
    print(manger)


