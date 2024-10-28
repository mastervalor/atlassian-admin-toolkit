from logic.slack_logic.slack_messages_logic import MessageLogic
from process.slack_message_process.slack_message_templates import api_message_block, looker_message_block
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='Jira API Integration Tokens Inventory')

file = os_logic.read_file()

for i in file:
    if i['Critical - needed on sunday'] != 'No':
        if 
        print(i['Owner'])
