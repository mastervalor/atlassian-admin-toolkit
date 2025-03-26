# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from datetime import date
from requests.auth import HTTPBasicAuth
import json
import operator

url = "https://lucidmotors.atlassian.net/rest/api/2/project/DR/properties"
#url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/2/project/DR/properties"

auth = HTTPBasicAuth("mouradmarzouk@lucidmotors.com", "10U1uDLf8VHUU6EYb8m3CE0E")

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


json_data = response.json()
#json=json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

# ===== All properties =====

for key in json_data.keys():
    #print(key)
    values=json_data.values()

# ===== All values in property =====

    for value in values:
        for inner in value:
            #print(inner['key'])
            url = "https://lucidmotors.atlassian.net/rest/api/2/project/DR/properties"
            #url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/2/project/DR/properties"
            DRProperty = inner['key']
            #print(DRProperty)
            urlP = "https://lucidmotors.atlassian.net/rest/api/2/project/DR/properties"
            #urlP = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/2/project/DR/properties"
            urlP = urlP + "/" + DRProperty
            responseP = requests.request(
               "GET",
               urlP,
               headers=headers,
               auth=auth
            )
            json_dataP = responseP.json()
            #print(json_dataP)

            if 'engineeringapproverprimary' in json_dataP['value'].keys():
                eap = (json_dataP['value']['engineeringapproverprimary'])
                eas = (json_dataP['value']['engineeringapproversecondary'])
                bap = (json_dataP['value']['buildapproverprimary'])
                bas = (json_dataP['value']['buildapproversecondary'])

# ===== EAP =====

                url = "https://lucidmotors.atlassian.net/rest/api/2/user?accountId=" + eap
                #url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/2/user?accountId=" + eap
                responseEAP = requests.request(
                   "GET",
                   url,
                   headers=headers,
                   auth=auth
                )
                json_dataEAP = responseEAP.json()
                if 'displayName' in json_dataEAP.keys():
                    eapDisplayName = (json_dataEAP['displayName'])
                #print(eapDisplayName)

# ===== EAS =====

                url = "https://lucidmotors.atlassian.net/rest/api/2/user?accountId=" + eas
                #url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/2/user?accountId=" + eas
                responseEAS = requests.request(
                   "GET",
                   url,
                   headers=headers,
                   auth=auth
                )
                json_dataEAS = responseEAS.json()
                if 'displayName' in json_dataEAS.keys():
                    easDisplayName = (json_dataEAS['displayName'])
                    #print(epsDisplayName)

# ===== BAP =====

                url = "https://lucidmotors.atlassian.net/rest/api/2/user?accountId=" + bap
                #url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/2/user?accountId=" + bap
                responseBAP = requests.request(
                   "GET",
                   url,
                   headers=headers,
                   auth=auth
                )
                json_dataBAP = responseBAP.json()
                if 'displayName' in json_dataBAP.keys():
                    bapDisplayName = (json_dataBAP['displayName'])
                    #print(bapDisplayName)

# ===== BAS =====

                url = "https://lucidmotors.atlassian.net/rest/api/2/user?accountId=" + bas
                #url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/2/user?accountId=" + bas
                responseBAS = requests.request(
                   "GET",
                   url,
                   headers=headers,
                   auth=auth
                )
                json_dataBAS = responseBAS.json()
                if 'displayName' in json_dataBAS.keys():
                    basDisplayName = (json_dataBAS['displayName'])
                    #print(basDisplayName)

# ====== updated property =====

                eapn = eapDisplayName
                easn = easDisplayName
                bapn = bapDisplayName
                basn = basDisplayName

                if len(json_dataP['value']['engineeringapproverprimary']) != 0:
                    final_property = dict([
                    ('engineeringapproverprimary',  eap ),
                    ('engineeringapproversecondary',  eas ),
                    ('buildapproverprimary',  bap ),
                    ('buildapproversecondary',  bas ),
                    ('engineeringapproverprimaryname',  eapn ),
                    ('engineeringapproversecondaryname',  easn ),
                    ('buildapproverprimaryname',  bapn ),
                    ('buildapproversecondaryname',  basn ),
                    ('zdateupdated', date.today().strftime("%m/%d/%Y")),
                    ('zdateupdatedname',  'Laurent Bordier')])


                payload = json.dumps(final_property,sort_keys=True)

                response = requests.request(
                "PUT",
                urlP,
                data=payload,
                headers=headers,
                auth=auth
                )

                print(DRProperty, payload)

            else:
                final_property = dict([
                    ('engineeringapproverprimary', " "),
                    ('engineeringapproversecondary', " "),
                    ('buildapproverprimary', " "),
                    ('buildapproversecondary', " "),
                    ('engineeringapproverprimaryname', " "),
                    ('engineeringapproversecondaryname', " "),
                    ('buildapproverprimaryname', " "),
                    ('buildapproversecondaryname', " "),
                    ('zdateupdated', date.today().strftime("%m/%d/%Y")),
                    ('zdateupdatedname', 'Laurent Bordier')])

                payload = json.dumps(final_property,sort_keys=True)

                response = requests.request(
                "PUT",
                urlP,
                data=payload,
                headers=headers,
                auth=auth
                )

                print(DRProperty, payload)