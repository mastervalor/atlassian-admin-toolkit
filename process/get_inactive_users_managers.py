from logic.okta_logic.okta_user_logic import OktaUsers
from logic.jira_logic.ticket_logic import Tickets

tickets = Tickets()

assignee_jql = 'project = "Enterprise CAPA" and assignee in inactiveUsers() and statusCategory != Done'

reporter_jql = 'project = "Enterprise CAPA" and reporter in inactiveUsers() and statusCategory != Done'


print(OktaUsers.get_user_manager('mourad.marzouk@getcruise.com'))
print(OktaUsers.get_user_status('mourad.marzouk@getcruise.com'))