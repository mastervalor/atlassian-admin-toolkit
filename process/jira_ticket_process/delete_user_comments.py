from logic.jira_logic.ticket_logic import Tickets

ticket_logic = Tickets()

tickets = ['ORACLE-3318', 'ORACLE-3324', 'ORACLE-3362', 'ORACLE-3383', 'ORACLE-3390', 'ORACLE-3423', 'ORACLE-3426',
          'ORACLE-3427', 'ORACLE-3440', 'ORACLE-3452', 'ORACLE-3453', 'ORACLE-3456', 'ORACLE-3460', 'ORACLE-3462',
          'ORACLE-3465']
username = 'user-e5e03'

for ticket in tickets:
    comments_ids = ticket_logic.get_users_comment_ids(username, ticket)
    if comments_ids:
        delete_ticket = ticket_logic.delete_user_comments(ticket, comments_ids)
        print(f'ticket number {ticket} had: {comments_ids} and deleted. {delete_ticket}')
    else:
        print(f'ticket number {ticket} had no comments from {username}')


# print(json.dumps(comments, sort_keys=True, indent=4, separators=(",", ": ")))
#3650988, 3650983
