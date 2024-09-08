from logic.jira_logic.ticket_logic import Tickets

tickets = Tickets()
key = 'BRM-3'

clear_label = tickets.clear_field(key, "labels")
