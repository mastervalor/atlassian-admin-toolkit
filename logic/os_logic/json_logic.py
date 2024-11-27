import os
import csv
import json


class JSONLogic:
    def __init__(self, open_file=None, write_file=None, append_file=None):
        """
        Initializes the JSONLogic class with optional file names.

        :param open_file: Name of the JSON file to open for reading.
        :param write_file: Name of the JSON file to open for writing.
        :param append_file: Name of the JSON file to open for appending.
        """
        self.open_file = open_file
        self.write_file = write_file
        self.append_file = append_file

    def read_file(self):
        """
        Reads a JSON file from the user's desktop and returns its contents.

        :return: Parsed JSON data from the file.
        """
        file_path = '/Users/{}/Desktop/{}.json'.format(os.environ.get('USER'), self.open_file)
        try:
            with open(file_path, mode='r') as json_file:
                data = json.load(json_file)
                print(f"File read from '{file_path}' successfully.")
                return data
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{file_path}'.")
            return None
