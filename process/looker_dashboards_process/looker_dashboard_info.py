from logic.looker_logic.looker_dashboards_logic import LookerDashboardLogic
from logic.os_logic.csv_logic import CSVLogic


csv_logic = CSVLogic(open_file='looker dashboards', write_file='looker dashboards full')
dashboard_logic = LookerDashboardLogic()
dashboards = csv_logic.read_file()
model_names = ['jira', 'mapping_jira', 'jira_qa']
dashboards_ids = []

for dash in dashboards:
    dashboards_ids.append(dash['dashboard_id'])

dashboards_info = dashboard_logic.get_dashboard_metadata(dashboards_ids, model_names)
csv_logic.write_to_file(dashboards_info)
