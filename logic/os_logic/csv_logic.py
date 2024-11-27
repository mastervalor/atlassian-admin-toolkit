import os
import csv


class CSVLogic:
    def __init__(self, open_file=None, write_file=None, append_file=None, columns=None):
        """
        Initializes the CSVLogic class with optional file names and columns.

        :param open_file: Name of the CSV file to open for reading.
        :param write_file: Name of the CSV file to open for writing.
        :param append_file: Name of the CSV file to open for appending.
        :param columns: List of column headers for the CSV file.
        """
        self.open_file = open_file
        self.write_file = write_file
        self.append_file = append_file
        self.headers_written = False
        self.columns = columns

    def read_file(self):
        """
        Reads a CSV file from the user's desktop and returns its contents as a list of dictionaries.

        :return: List of dictionaries representing the CSV file's rows.
        """
        file_path = '/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), self.open_file)
        try:
            with open(file_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                print(f"File read to '{file_path}' successfully.")
                return list(csv_reader)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return []

    def write_to_file(self, data):
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

    def append_to_file(self, data):
        if self.append_file:
            file_path = '/Users/{}/Desktop/{}.csv'.format(os.environ.get('USER'), self.append_file)
            try:
                with open(file_path, mode='a', newline='') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=self.columns)
                    if not self.headers_written:
                        header_row = {column: column for column in self.columns}
                        writer.writerow(header_row)
                        self.headers_written = True
                    writer.writerow(dict(zip(self.columns, data)))
                print(f"Data appended to '{file_path}' successfully.")
            except Exception as e:
                print(f"Error writing data to file '{file_path}': {e}")
        else:
            print("No file specified for writing.")