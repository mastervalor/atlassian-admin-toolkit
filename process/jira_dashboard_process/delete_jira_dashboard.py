from pprint import pprint

from calls.jira_api_calls.jira_api_dashboards import DashboardsJiraCalls
from logic.jira_logic.dashboard_logic import Dashboards

dashboards = DashboardsJiraCalls()

pprint(dashboards.get_all_boards())
