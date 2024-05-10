import os
import csv


class OSLogic:
    def __init__(self, open_file=None, write_file=None):
        self.open_file = open_file
        self.write_file = write_file

    def read_file(self):
        file_path = '/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), self.open_file)
        try:
            with open(file_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                print(f"File read to '{file_path}' successfully.")
                return list(csv_reader)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return []

    def write_file(self, data):
        if self.write_file:
            file_path = '/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), self.write_file)
            try:
                with open(file_path, mode='a', newline='') as csv_file:
                    fieldnames = data[0].keys() if data else []
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    if os.stat(file_path).st_size == 0:
                        writer.writeheader()
                    writer.writerows(data)
                print(f"Data appended to '{file_path}' successfully.")
            except Exception as e:
                print(f"Error writing to file '{file_path}': {e}")
        else:
            print("No file specified for writing.")