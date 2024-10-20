from logic.looker_logic.looker_dashboards_logic import LookerDashboardLogic
from logic.os_logic.os_logic import OSLogic


os_logic = OSLogic(open_file='looker dashboards', write_file='looker dashboards creators')
dashboard_logic = LookerDashboardLogic()
dashboards = os_logic.read_file()
dashboards_ids = []

for dash in dashboards:
    dashboards_ids.append(dash['dashboard_id'])

dashboards_info = dashboard_logic.get_dashboard_creators(dashboards_ids)
os_logic.write_to_file(dashboards_info)
