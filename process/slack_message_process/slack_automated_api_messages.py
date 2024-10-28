from logic.slack_logic.slack_messages_logic import MessageLogic
from process.slack_message_process.slack_message_templates import api_message_block, looker_message_block
from logic.os_logic.os_logic import OSLogic

os_logic = OSLogic(open_file='Jira API Integration Tokens Inventory')

file = os_logic.read_file()
message_logic = MessageLogic()

for i in file:
    user_emails = ['parag.hardas@getcruise.com', 'david.cooke@getcruise.com',
                   'mourad.marzouk@getcruise.com']

    if i['Critical - needed on sunday'] != 'No':
        if ',' in i['Owner']:
            user_emails.extend(i['Owner'].split(','))
            print(user_emails)
        else:
            user_emails.append(i['Owner'])
            print(user_emails)