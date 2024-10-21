from calls.looker_api_calls.looker_dashboard_api import LookerDashboard
from calls.looker_api_calls.looker_explores_api import LookerExplores
from logic.looker_logic.looker_dashboards_logic import LookerDashboardLogic
from logic.looker_logic.looker_explorers_logic import LookerExplorersLogic
from logic.okta_logic.okta_user_logic import OktaUsers
from dataformating.json_formating import JSONFormating
import json

okta_logic = OktaUsers()
looker_dashboard = LookerDashboard()
looker_explorer = LookerExplores()
explorer = LookerExplorersLogic()
dashboard_logic = LookerDashboardLogic()
dashboard_ids = ['1']
dashboard_id = 'ra-db::ra_db_ra_bugs'
model_name = 'metrics'
# response = looker_dashboard.get_dashboard_by_id(dashboard_id).json()
response = looker_dashboard.get_dashboard_by_id(dashboard_id).json()
# response = looker_dashboard.search_dashboards_for_explore('jira_issues')
# response2 = dashboard.get_dashboards_models(dashboard_id, 'metrics')
# response = looker_explorer.get_all_explores_by_model('jira')
# response = looker_explorer.get_all_explores().json()
# response = json.loads(response.text)
# response = okta_logic.get_user_second_email('tars.svc@getcruise.com')
# response = looker_explorer.get_query_history('jira', 'Stability_Buckets_SLA')
# response = looker_dashboard.get_all_dashboards().json
JSONFormating.pretty_json(response)
# print(response2)
