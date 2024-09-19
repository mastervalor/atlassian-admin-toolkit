from logic.jira_logic.dashboard_logic import Dashboards

dashboards = Dashboards()

boards = dashboards.get_board_ids('ES: Vehicle Connectivity Products')

print(dashboards.delete_boards(boards))
