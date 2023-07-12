from call import Jira, Okta
import csv
import os

jira = Jira()
openFile = 'Inactive project leads'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        user = Okta.users_id((row['username'] + '@getcruise.com'))
        if user is False:
            print("couldn't find ")
        manager = Okta.users_id(user['profile']['manager'] + '@getcruise.com')
        status = True
        while status:
            if manager['status'] == 'DEPROVISIONED':
                print(manager['profile']['email'] + manager['status'])
                manager = Okta.users_id(manager['profile']['manager'] + '@getcruise.com')
            else:
                status = False
        print(row['username'] + "'s manager:" + manager['profile']['manager'] + manager['status'] + manager['profile']['title'])
        if "VP," in manager['profile']['title'] or "vice president" in manager['profile']['title'] or "chief" in manager['profile']['title']:
            print(f"{row['username']}'s manger is the vp of {manager['profile']['title']}")
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

            response = jira.create_ticket(payload)
            print(response)
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
                        "name": user['profile']['manager']
                     },
                    "customfield_28001": {
                        'value': "Jira"
                    },
                    "customfield_13230": [
                        {
                            "name": user['profile']['manager']
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

            response = jira.create_ticket(payload)
            print(response)