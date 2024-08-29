from logic.jira_logic.project_logic import Projects
from logic.okta_logic.okta_user_logic import OktaUsers


project = Projects()
projects = project.get_project_owners_and_status()

for project in projects:
    if not project['Active']:
        manager, manager_title, manager_status  = OktaUsers.get_manager_info(project['Username'])
        payload = {
            'fields': {
                'project': {
                    'key': 'ITAPP',
                },
                'summary': f"project: {project['project']}, Key: {project['Key']} no longer has and active owner.",
                "issuetype": {
                    "id": "3"
                },
                "reporter": {
                    "name": 'mourad.marzouk'
                },
                "customfield_18672": {
                    "value": "Strategic Work"
                },
                "customfield_28001": {
                    'value': "Jira"
                },
                "description": f"project: {project['project']}, Key: {project['Key']} no longer has and active owner."
                               f"Last owner is {project['Name']} and we need to find a replacement."
                               f"Their listed manager is {manager}, Title{manager_title}, Status{manager_status}"
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