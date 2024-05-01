import os
import csv


class OS_Logic:
    def __init__(self, open_file=None, write_file=None):
        self.open_file = open_file
        self.write_file = write_file

    def read_file(self):
        file_path = '/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), self.open_file)
        try:
            with open(file_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return list(csv_reader)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return []
