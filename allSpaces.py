import csv
import os
from logic.confluence_logic.space_logic import Spaces

main_file = 'spaces_des'
updated_file = 'spaces_des2'
space_logic = Spaces()

with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), updated_file), mode='w') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Space Name', 'Space Key', 'Owners'])
    response = space_logic.get_all_spaces()
    for i in response['results']:
        if i['status'] == 'current':
            with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), main_file), mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for r in csv_reader:
                    if r['Space Name'] == i['name']:
                        writer.writerow([i['name'], i['key'], r['Owners']])
