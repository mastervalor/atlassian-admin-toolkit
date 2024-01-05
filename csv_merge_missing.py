import csv
import os

mainFile = 'Inactive project leads'
final = 'unowned projects'


with open ('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), final), mode='a') as edit_file:
    