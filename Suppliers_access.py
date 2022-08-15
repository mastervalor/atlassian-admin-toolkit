import requests
import urllib.request
from datetime import date
from requests.auth import HTTPBasicAuth
from urllib.error import HTTPError
import json
import operator

# url = "https://lucidmotors.atlassian.net/rest/api/2/"
url = "https://lucidmotors-sandbox-693.atlassian.net/rest/api/2/"

auth = HTTPBasicAuth("mouradmarzouk@lucidmotors.com", "10U1uDLf8VHUU6EYb8m3CE0E")

headers = {
    "Accept": "application/json"
}


def catch(key, type):
    count = 0
    while count < 3:
        print(count)
        if type == "project":
            link = url + "project/" + key
            response = requests.request(
                "GET",
                link,
                headers=headers,
                auth=auth
            )
            print(response)
        elif type == "group":
            link = url + "group/"

            query = {
                'groupname': {key}
            }
            response = requests.request(
                "GET",
                link,
                headers=headers,
                params=query,
                auth=auth
            )
            print(response)

        if response.status_code != 200:
            count += 1
            key = str(input("Please try again, the input you submitted was invalid: "))
            if count == 2:
                print("Pleas try again later")
                quit()
        else:
            count = 0
            return key


project = str(input("What is the project key? "))

project = catch(project, type="project")

supplier = str(input("What is the Name of of the Supplier okta group? "))

supplier = catch(supplier, type="group")

#security_supplier = str(input("What will be the name of the supplier security level? "))

urlP = url + "project/" + project + "/permissionscheme"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps({
    "id": 10548
})

response = requests.request(
    "PUT",
    urlP,
    data=payload,
    headers=headers,
    auth=auth
)

print(response)

urlg = url + "project/" + project + "/role/10425"

payload = json.dumps({
    "group": [
        supplier
    ]
})

response = requests.request(
   "POST",
   urlg,
   data=payload,
   headers=headers,
   auth=auth
)

print(response)
