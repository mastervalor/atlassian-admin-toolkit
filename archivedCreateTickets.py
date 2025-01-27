from calls.jira_api_calls.jira_api_tickets import TicketsJiraCalls
from logic.okta_logic.okta_user_logic import OktaUsers
import csv
import os

tickets = TicketsJiraCalls()
okta_users = OktaUsers()
openFile = 'Projects - projects to archive'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        user = okta_users.get_user_id((row['username'] + '@getcruise.com'))
        if user is False:
            print("couldn't find ")
        manager = okta_users.get_user_id(user['profile']['manager'] + '@getcruise.com')
        status = True
        while status:
            if manager['status'] == 'DEPROVISIONED':
                print(manager['profile']['email'] + ' ' + manager['status'])
                manager = okta_users.get_user_id(manager['profile']['manager'] + '@getcruise.com')
            else:
                status = False
        print(row['username'] + "'s manager:" + manager['profile']['manager'] + manager['status'] + manager['profile']['title'])
        if "Vice President" in manager['profile']['title'] or "VP," in manager['profile']['title'] or\
                "chief" in manager['profile']['title']:
            reports = manager['profile']['directReports']
            name_list = reports.split("; ")
            for report in name_list:
                email = f"{report.lower().replace(' ', '.')}@getcruise.com"
                looking = okta_users.get_user_id(email)
                if 'Executive Assistant' in looking['profile']['title'] or 'Executive Business' in looking['profile']['title']:
                    print(f"{row['username']}'s manger is the vp of {manager['profile']['title']}")
                    username = report.lower().replace(' ', '.')
                    vp = manager['profile']['firstName'] + ' ' + manager['profile']['lastName']
                    payload = {
                        'fields': {
                            'project': {
                                'key': 'ITAPP',
                            },
                            'summary': f"Project key: {row['project']} lead {row['username']} is no longer with the company",
                            "issuetype": {
                                "id": "3"
                            },
                            "reporter": {
                                "name": 'mourad.marzouk'
                            },
                            "customfield_13230": [
                                {
                                    "name": username
                                }],
                            "customfield_18672": {
                                "value": "Strategic Work"
                            },
                            "customfield_28001": {
                                'value': "Jira"
                            },
                            "description": f"Hello {report} Project key: {row['project']} lead {row['username']} is "
                                           f"no longer with the company and we need to find out who would be the new"
                                           f"owner of this project. The next manager in line is the VP {vp} as their "
                                           f"Executive Assistant we are reaching out you for support in finding who "
                                           f"they would like to appoint as new owner for this project. Thank you"
                        },
                        "update": {
                            "issuelinks": [
                                {
                                    "add": {
                                        "type": {
                                            "name": "Problem/Incident",
                                            "inward": "is caused by",
                                            "outward": "causes"
                                        },
                                        "outwardIssue": {
                                            "key": "ITAPP-5040"
                                        }
                                    }
                                }
                            ]
                        }
                    }

                    response = tickets.create_ticket(payload)
                    print(response)
                    break
        else:
            print(f"{row['username']}'s manger is not a vp")
            payload = {
                'fields': {
                    'project': {
                        'key': 'ITAPP',
                    },
                    'summary': f"Project key: {row['project']} lead {row['username']} is no longer with the company",
                    "issuetype": {
                            "id": "3"
                    },
                    "reporter": {
                        "name": 'mourad.marzouk'
                     },
                    "customfield_28001": {
                        'value': "Jira"
                    },
                    "customfield_18672": {
                        "value": "Strategic Work"
                    },
                    "customfield_13230": [
                        {
                            "name": manager['profile']['firstName'] + '.' + manager['profile']['lastName']
                        }],
                    "description": f"Project key: {row['project']} lead {row['username']} is no longer with the company "
                                   f"and we need to find out who would be the new owner of this project",
                },
                "update": {
                    "issuelinks": [
                        {
                            "add": {
                                "type": {
                                    "name": "Problem/Incident",
                                    "inward": "is caused by",
                                    "outward": "causes"
                                },
                                "outwardIssue": {
                                    "key": "ITAPP-5040"
                                }
                            }
                        }
                    ]
                }
            }

            response = tickets.create_ticket(payload)
            print(response)
