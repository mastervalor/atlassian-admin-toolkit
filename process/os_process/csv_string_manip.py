import csv
import os

file = 'JSM Usage - Sheet3'

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), file), mode='r+') as new_csv:
    reader = csv.DictReader(new_csv)
    writer = csv.DictWriter(new_csv, fieldnames=reader.fieldnames)
    rows = []

    for i in reader:
        login_details = i['Login details']
        if login_details == 'Never logged in':
            rows.append(i)
        else:
            date_start_index = login_details.index(':') + 2
            date_string = login_details[date_start_index:]
            i['Login details'] = date_string
            rows.append(i)

    new_csv.seek(0)
    writer.writeheader()
    writer.writerows(rows)
    new_csv.flush()
