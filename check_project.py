import csv
import os
from call import project_metric

mainFile = 'missing'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), mainFile), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        print(i['key'], project_metric(i['key']))