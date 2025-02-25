import json
import re
import subprocess

project = 'DR'
prefix = 'approvers-'

env = 'prod'

url_response = subprocess.check_output(['acli', env, '-a', 'getServerInfo'])
m = re.search('url: (.+)', url_response)
url = m.group(1)

cmdbase = 'acli ' + env + ' --action renderRequest --requestType GET --type application/json --request'
cmdreq = '/rest/api/2/project/' + project + '/properties/'


response = subprocess.check_output(cmdbase.split() + [cmdreq])

# Trim the "Rendered data for..." line
response = response.split("\n",1)[1]

properties = json.loads(response)

for prop in properties['keys']:
    prop_url = prop['self'].replace(url,'')
    if re.search('properties/approvers-', prop_url):
        response = subprocess.check_output(cmdbase.split() + [prop_url])
        response = response.split("\n",1)[1]

        project_property = json.loads(response)

        print("{}\t{}\t{}\t{}\t{}".format(project_property['key'],
                                          project_property['value']['engineeringapproverprimary'],
                                          project_property['value']['engineeringapproversecondary'],
                                          project_property['value']['buildapproverprimary'],
                                          project_property['value']['buildapproversecondary'], ))
