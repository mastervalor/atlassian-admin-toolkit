from logic.looker_logic.looker_dashboards_logic import LookerDashboardLogic
from file_manip.csv_file_manip import CSVLogic


csv_logic = CSVLogic(open_file='looker dashboards', write_file='looker dashboards creators')
dashboard_logic = LookerDashboardLogic()
dashboards = csv_logic.read_file()
dashboards_ids = []

for dash in dashboards:
    dashboards_ids.append(dash['dashboard_id'])

dashboards_info = dashboard_logic.get_dashboard_creators(dashboards_ids)
csv_logic.write_to_file(dashboards_info)
