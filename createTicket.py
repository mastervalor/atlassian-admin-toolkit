import json
import requests
import csv
import os
from auth import auth


def create(summary):
    url = "https://lucidmotors.atlassian.net/rest/api/3/issue"
    description = 'Dear space owner,\n' \
                  'Due to recent incidents that allowed many users to access internal and/or at-risk information, our team' \
                  'has decided to audit all Confluence spaces that grant access to everyone in the company. Your respective' \
                  'space(s) either has an all-encompassing group or allows permission for anyone to view the content. \n' \
                  'Action Required > Carefully review this link: '
    description2 = ' and select the appropriate cost center groups that would require access to your space. ' \
                   'The deadline to receive this information from you is due no later than Wednesday, ' \
                   'May 25th We will effectively remove any large groups from all spaces on Thursday, May 26th'

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "update": {},
        "fields": {
            "summary": summary,
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": description,
                                "type": "text"
                            },
                            {
                                "marks": [
                                    {
                                        "attrs": {
                                            "href": "https://lucidmotors.atlassian.net/wiki/spaces/HELP/pages/2752119079/Cost+Center+Groups"
                                        },
                                        "type": "link"
                                    }
                                ],
                                "text": "link",
                                "type": "text"
                            },
                            {
                                "text": description2,
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "issuetype": {
                "id": "11205"
            },
            "parent": {
                "key": "ATLAS-12207"
            },
            "project": {
                "id": "13981"
            }
        }
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )


mainFile = "confluence groups "

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), mainFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        summary = i['Space'] + " has " + i['Group']
        create(summary)
