import os
import json
import logging


class JSONManip:
    def __init__(self, open_file=None, write_file=None, append_file=None, base_dir=None):
        """
        Initializes the JSONManip class with optional file names and base directory.

        :param open_file: Name of the JSON file to open for reading.
        :param write_file: Name of the JSON file to open for writing.
        :param append_file: Name of the JSON file to open for appending.
        :param base_dir: Base directory for file operations.
        """
        self.base_dir = base_dir or os.path.expanduser("~/Desktop")
        self.open_file = self._get_file_path(open_file)
        self.write_file_path = self._get_file_path(write_file)
        self.append_file = self._get_file_path(append_file)

    def _get_file_path(self, filename):
        if filename:
            return os.path.join(self.base_dir, f"{filename}.json")
        return None

    def read_file(self):
        """
        Reads a JSON file and returns its contents.

        :return: Parsed JSON data from the file or None if an error occurs.
        """
        file_path = self.open_file
        try:
            with open(file_path, mode='r') as json_file:
                data = json.load(json_file)
                logging.info(f"File read from '{file_path}' successfully.")
                return data
        except FileNotFoundError:
            logging.error(f"File '{file_path}' not found.")
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from file '{file_path}': {e}")
        return None

    # ... (other methods)

    def write_file(self, data, output_file=None):
        """
        Writes the JSON data to a file on the user's desktop or specified path.

        :param data: The JSON data to write.
        :param output_file: The name of the output JSON file (without `.json` extension).
        """
        # Determine the file path to write to
        if output_file:
            file_path = os.path.join(self.base_dir, f"{output_file}.json")
        elif self.write_file_path:
            file_path = self.write_file_path
        else:
            raise ValueError("No valid file path specified for writing.")

        try:
            with open(file_path, mode='w') as json_file:
                json.dump(data, json_file, indent=4)
                print(f"File written to '{file_path}' successfully.")
        except Exception as e:
            print(f"Error writing to file '{file_path}': {e}")

    def write_spaceless_file(self, data, output_file=None):
        """
        Writes the JSON data to a file on the user's desktop or specified path.

        :param data: The JSON data to write.
        :param output_file: The name of the output JSON file (without `.json` extension).
        """
        # Determine the file path to write to
        if output_file:
            file_path = os.path.join(self.base_dir, f"{output_file}.json")
        elif self.write_file_path:
            file_path = self.write_file_path
        elif self.open_file:
            file_path = self.open_file
        else:
            raise ValueError("No valid file path specified for writing.")

        try:
            with open(file_path, mode='w') as json_file:
                # Write JSON data without pretty printing to minimize file size
                json.dump(data, json_file, separators=(',', ':'))  # Compact JSON
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
