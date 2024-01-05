import csv
import os

mainFile = 'Inactive project leads'
final = 'unowned projects'

keys = []

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), final), mode='r') as edit_file:
    csv_reader2 = csv.DictReader(edit_file)
    for i in csv_reader2:
        keys.append(i['Key'])

    with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), mainFile), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            if i['key'] not in keys:
                print(i['key'])