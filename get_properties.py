import json
import re
import subprocess

project = 'DR'
prefix = 'approvers-'

env = 'prod'

urlresponse = subprocess.check_output(['acli', env, '-a', 'getServerInfo'])
m = re.search('url: (.+)', urlresponse)
url = m.group(1)

cmdbase = 'acli ' + env + ' --action renderRequest --requestType GET --type application/json --request'
cmdreq = '/rest/api/2/project/' + project + '/properties/'

# print cmdbase + cmdreq

response = subprocess.check_output(cmdbase.split() + [cmdreq])

# Trim the "Rendered data for..." line
response = response.split("\n",1)[1]

properties = json.loads(response)

for prop in properties['keys']:
    propurl = prop['self'].replace(url,'')
    if re.search('properties/approvers-', propurl):
        response = subprocess.check_output(cmdbase.split() + [propurl])
        response = response.split("\n",1)[1]

        property = json.loads(response)

# u'buildapproversecondary': u'5d8317439581710c3032ac97', u'engineeringapproverprimary': u'557058:d5dad836-eb67-42b1-ab5f-2b410679d099', u'buildapproverprimary': u'5cc8aeebcbbec211ec62a0ec', u'engineeringapproversecondary': u'557058:2430e675-3447-4a5d-a063-31d69db53987

        print("{}\t{}\t{}\t{}\t{}".format(property['key'], property['value']['engineeringapproverprimary'], property['value']['engineeringapproversecondary'], property['value']['buildapproverprimary'], property['value']['buildapproversecondary'], ))
