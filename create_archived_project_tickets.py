from logic.os_logic import OSLogic
from logic.ticket_logic import Tickets

os_logic = OSLogic(open_file='Archived projects')
file = os_logic.read_file()
