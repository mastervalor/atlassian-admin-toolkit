#!/usr/bin/python

import json, re, subprocess, urllib, csv
from collections import OrderedDict

project = 'DR'
prefix = 'approvers-general_assembly-'

env = 'dev'

with open('text.csv') as csv_file:
    csv_reader = csv.reader(csv.file, delimiter=',')
    line_count = 0
    for rule in csv_reader:
        if rule['projects']:
            if rule['projects'][0]['projectId'] == '13970':
                if re.search('GA', rule['name']):
                    comp1 = rule['components'][1]
                    componentjson = comp1['children'][0]['conditions'][2]['value']['compareValue']['value']

                    component = json.loads(componentjson)[0]

                    for child in comp1['children']:
                        buildphase = child['conditions'][1]['value']['compareValue']['value']

                        propertykey = prefix + component + '-' + buildphase
                        propertykey = propertykey.lower()
                        propertykey = propertykey.replace(' ', '_')
                        propertykey = urllib.quote(propertykey, safe='')

                        propertyval = OrderedDict()

                        for op in child['children'][0]['value']['operations']:
                            approvertype = op['field']['value'].encode('ascii')
                            approvertype = approvertype.replace(' ', '')
                            approvertype = approvertype.lower()
                            approverval = op['value']['value']
                            propertyval[approvertype] = approverval

                        print(propertykey)
                        print(propertyval)

                        cmdbase = 'acli ' + env + ' --action renderRequest --requestType PUT --request'
                        cmdreq = '/rest/api/2/project/' + project + '/properties/' + propertykey
                        cmdreqarg = '--requestParameters'
                        cmdparams = json.dumps(propertyval)

                        cmd = '{} {} {} {}'.format(cmdbase, cmdreq, cmdreqarg, cmdparams)

                        print(cmd)

                        response = subprocess.check_output(cmdbase.split() + [cmdreq, cmdreqarg, cmdparams])
                        print(response)