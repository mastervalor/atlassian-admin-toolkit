from pprint import pprint

from calls.jira_api_calls.jira_api_dashboards import DashboardsJiraCalls
from logic.jira_logic.dashboard_logic import Dashboards

# dashboards = Dashboards()
#
# pprint(dashboards.get_board_ids('C5 EV Builds'))
boards = [1224, 1225, 1226]

dashboards = DashboardsJiraCalls()

pprint(dashboards.delete_board(str(1224)))
