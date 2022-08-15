import csv
import os

from os import path



fileName = "new"
if not path.exists('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName)):
    print("Sorry that file name doesn't exist, try again")
    quit()

list = list(range(1, 3165))
oldString = []
issueid = []
type = []
parent = []
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for t in csv_reader:
        oldString.append(t["oldstring"])
        issueid.append(t["issueid"])
        type.append(t["type"])
        parent.append(t["parentkey"])

    print(parent)