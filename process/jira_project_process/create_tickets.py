from calls.jira_api_calls.jira_api_tickets import TicketsJiraCalls
from calls.jira_api_calls.jira_api_projects import ProjectJiraCalls
import csv
import os

tickets = TicketsJiraCalls()
projects = ProjectJiraCalls()

openFile = 'Projects - projects to archive'
assingees = {"mourad.marzouk": 0, "patricia.pattin": 0, "ron.erlandson": 0}


with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), openFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        name, status = projects.project_owner(row['key'])
        if not status:
            assignee = 'mourad.marzouk'
            assingees['mourad.marzouk'] += 1
            approver = ''
        else:
            lowest_assignee = min(assingees, key=assingees.get)
            assignee = lowest_assignee
            assingees[lowest_assignee] += 1
            approver = name

        owner = name.replace('.', ' ')
        payload = {
            'fields': {
                'project': {
                    'key': 'ITAPP',
                },
                'summary': f"This project: {row['Name']} does not meet the new requirements, and will be targeted for "
                           f"archiving",
                "issuetype": {
                    "id": "3"
                },
                "reporter": {
                    "name": 'mourad.marzouk'
                },
                "assignee": {
                    "name": assignee
                },
                "customfield_13230": [
                    {
                        "name": approver
                    }],
                "customfield_18672": {
                    "value": "Strategic Work"
                },
                "customfield_28001": {
                    'value': "Jira"
                },
                "description": f"Hello {owner} As the owner of {row['Name']} : {row['key']} In our effort to "
                               f"standardize the instance, we have found that your project is not used in some time "
                               f"or doesn't have many tickets. Due to this project will be targeted for archival. "
                               f"We are reaching out to you to inform you about this. If you have any concerns please "
                               f"let us know here. If no response in 5 days the project will be archived"
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
                                "key": "ITAPP-7856"
                            }
                        }
                    }
                ]
            }
        }
        response = tickets.create_ticket(payload)
        print(response, assignee, row['Name'], approver)
