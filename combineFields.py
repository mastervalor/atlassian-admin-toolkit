import json
from calls.jira_api_calls.jira_api_tickets import TicketsJiraCalls

tickets = TicketsJiraCalls()

jql = ('project in (POL,LTSS,FINTECH,CRP,MDG,PROCURETEC,OPSTECH,PTT,CUSTTECH,DCOPS,EAI,EIAM,ENTNET,ITAPP,ITCPE,ITINF,'
       'ITOPS,ITAM,APPSEC,SECOPS,CORPSEC,TRUST,AVSEC,PLATAUTH,SCS1,THREAT,PRIVACY,SECRETS) and ("Business '
       'Justification" is not EMPTY or "Value Proposition" is not EMPTY) AND issuetype = Epic and description is EMPTY')

query = tickets.jql('?startAt=0&maxResults=1000', jql)

keys = []
for key in query['issues']:
    keys.append(key['key'])

for key in keys:
    new_description = ''
    ticket = tickets.get_ticket(key)
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
    edit = tickets.edit_ticket(key, payload)
    print(edit)


#print(json.dumps(query, sort_keys=True, indent=4, separators=(",", ": ")))