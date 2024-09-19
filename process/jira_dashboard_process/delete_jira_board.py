from logic.jira_logic.dashboard_logic import Dashboards

dashboards = Dashboards()

boards = dashboards.get_board_ids('C5 EV Builds - Sunny')

print(dashboards.delete_boards(boards))
