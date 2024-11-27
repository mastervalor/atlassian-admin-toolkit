from logic.slack_logic.slack_messages_logic import MessageLogic
from process.slack_message_process.slack_message_templates import api_message_block
from logic.os_logic.csv_logic import CSVLogic

csv_logic = CSVLogic(open_file='Jira API Integration Tokens Inventory')

file = csv_logic.read_file()
message_logic = MessageLogic()

for svc in file:
    user_emails = ['parag.hardas@getcruise.com', 'david.cooke@getcruise.com',
                   'mourad.marzouk@getcruise.com', 'satchidanand.challapalli@getcruise.com',
                   'sumaiah.syed@getcruise.com', 'swaroop.vimalkumar@getcruise.com']

    owner = [email.split('@')[0].replace('.', ' ') for email in svc['Owner'].split(',')]
    if len(owner) == 1:
        owner = owner[0]
    elif len(owner) == 2:
        owner = f"{owner[0]} and {owner[1]}"

    svc_account = svc['API Integration Account']

    if svc['Critical - needed on sunday'] != 'No':
        if ',' in svc['Owner']:
            user_emails.extend(svc['Owner'].split(','))
            print(user_emails)
        else:
            user_emails.append(svc['Owner'])
            print(user_emails)

    blocks = api_message_block(owner, svc_account)
    message_logic.send_group_message(user_emails, blocks=blocks)
