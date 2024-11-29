import os
import json


class JSONManip:
    def __init__(self, open_file=None, write_file=None, append_file=None):
        """
        Initializes the JSONManip class with optional file names.

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

    def write_file(self, data, output_file=None):
        """
        Writes the JSON data to a file on the user's desktop.

        :param data: The JSON data to write.
        :param output_file: The name of the output JSON file.
        """
        if output_file is None:
            output_file = self.write_file or self.open_file

        file_path = '/Users/{}/Desktop/{}.json'.format(os.environ.get('USER'), output_file)
        try:
            with open(file_path, mode='w') as json_file:
                json.dump(data, json_file, indent=4)
                print(f"File written to '{file_path}' successfully.")
        except Exception as e:
            print(f"Error writing to file '{file_path}': {e}")

    def append_to_file(self, data):
        """
        Appends JSON data to an existing JSON file on the user's desktop.

        :param data: The JSON data to append.
        """
        file_path = '/Users/{}/Desktop/{}.json'.format(os.environ.get('USER'), self.append_file)
        try:
            existing_data = []
            if os.path.exists(file_path):
                with open(file_path, mode='r') as json_file:
                    existing_data = json.load(json_file)

            # Assuming the JSON file contains a list
            if not isinstance(existing_data, list):
                raise ValueError("Existing JSON data is not a list; cannot append.")

            if isinstance(data, list):
                existing_data.extend(data)
            else:
                existing_data.append(data)

            with open(file_path, mode='w') as json_file:
                json.dump(existing_data, json_file, indent=4)
                print(f"Data appended to '{file_path}' successfully.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{file_path}'.")
        except Exception as e:
            print(f"Error appending to file '{file_path}': {e}")
