import csv
import os
from call import Jira

project = 'Projects metrics 2'
names = []
word_counts = {}
jira = Jira()

with open('/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), project), mode='r') as new_file:
    csv_reader = csv.DictReader(new_file)
    for i in csv_reader:
        names.append(i['Name'])

for name in names:
    words = name.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

for word, count in word_counts.items():
    if count > 1:
        print(f"{word} appears in {count} names.")
