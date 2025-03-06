from logic.jira_logic.ticket_logic import Tickets

ticket_logic = Tickets()

jql = ('project in (POL,LTSS,FINTECH,CRP,MDG,PROCURETEC,OPSTECH,PTT,CUSTTECH,DCOPS,EAI,EIAM,ENTNET,ITAPP,ITCPE,ITINF,'
       'ITOPS,ITAM,APPSEC,SECOPS,CORPSEC,TRUST,AVSEC,PLATAUTH,SCS1,THREAT,PRIVACY,SECRETS) and ("Business '
       'Justification" is not EMPTY or "Value Proposition" is not EMPTY) AND issuetype = Epic and description is EMPTY')

query = ticket_logic.get_tickets_from_jql(jql)

keys = []
for key in query['issues']:
    keys.append(key['key'])

for key in keys:
    new_description = ''
    ticket = ticket_logic.get_ticket_by_key(key)
    print(key)
    if ticket['fields']['description']:
        new_description += ticket['fields']['description']
    if ticket['fields']['customfield_25110']:
        new_description += ticket['fields']['customfield_25110']
    if 'customfield_20201' in ticket['fields'] and ticket['fields']['customfield_20201'] is not None:
        new_description += ticket['fields']['customfield_20201']
    print(key, new_description)
    payload = {
        "fields": {
            'description': new_description
        }
    }
    edit = ticket_logic.set_fields(key, payload)
    print(edit)
