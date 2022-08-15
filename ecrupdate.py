import requests
from auth import auth
import concurrent.futures
import json
import time


def buildPhase(i):
    url = "https://lucidmotors.atlassian.net/rest/api/3/issue/ECR-" + i

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    ).text

    response = json.loads(response)
    value = response['fields']['customfield_11601'][0]['value']
    if value == 'Alpha':
        id = ''
    elif value == 'Beta1':
        id = ''
    elif value == 'RC':
        id = ''
    elif value == 'SOP':
        id = ''
    elif value == 'Post SOP':
        id = ''



t1 = time.perf_counter()

tickets = list(range(1, 25000))
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(buildPhase, tickets)

t2 = time.perf_counter()

print(f'Finished in {t2 - t1} seconds')
