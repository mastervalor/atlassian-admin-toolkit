import requests
import json
from auth import auth, staging_auth
from config import jira_staging


jql = ('project in (POL,LTSS,FINTECH,CRP,MDG,PROCURETEC,OPSTECH,PTT,CUSTTECH,DCOPS,EAI,EIAM,ENTNET,ITAPP,ITCPE,ITINF,'
       'ITOPS,ITAM,APPSEC,SECOPS,CORPSEC,TRUST,AVSEC,PLATAUTH,SCS1,THREAT,PRIVACY) and ("Business '
       'Justification" is not EMPTY or "Value Proposition" is not EMPTY) AND issuetype = Epic and description is EMPTY')

url = jira_staging + 'search' + '?startAt=0&maxResults=1000'

headers = {
       "Accept": "application/json"
}
query = {
       'jql': jql
}
print(url)
print()

response = json.loads(requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=staging_auth
        ).text)

print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))