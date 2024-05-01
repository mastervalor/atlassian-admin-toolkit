import os
import csv


class OS_Logic:
    def __init__(self):


    def read_file(self, open_file):
        file_path = '/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), open_file)
        try:
            with open(file_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return list(csv_reader)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return []
