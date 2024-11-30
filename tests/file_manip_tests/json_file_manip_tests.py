import unittest
import os
import json
from file_manip.json_file_manip import JSONManip


class TestJSONManip(unittest.TestCase):
    def setUp(self):
        # Set up test files and directories
        self.test_dir = 'test_json_files'
        os.makedirs(self.test_dir, exist_ok=True)
        # Define file names without extensions
        self.open_file_name = 'test_open'
        self.write_file_name = 'test_write'
        self.append_file_name = 'test_append'

        # Full file paths
        self.open_file_path = os.path.join(self.test_dir, f"{self.open_file_name}.json")
        self.write_file_path = os.path.join(self.test_dir, f"{self.write_file_name}.json")
        self.append_file_path = os.path.join(self.test_dir, f"{self.append_file_name}.json")

        # Create a sample JSON file to read
        self.sample_data = {"key1": "value1", "key2": [1, 2, 3]}
        with open(self.open_file_path, 'w') as f:
            json.dump(self.sample_data, f)

        # Create a sample JSON file to append to (a list)
        self.sample_list = [1, 2, 3]
        with open(self.append_file_path, 'w') as f:
            json.dump(self.sample_list, f)

    def tearDown(self):
        # Clean up test files and directories
        for file_path in [self.open_file_path, self.write_file_path, self.append_file_path]:
            if os.path.exists(file_path):
                os.remove(file_path)
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)

    def test_read_file(self):
        # Initialize JSONManip with the test open file
        json_manip = JSONManip(open_file=self.open_file_name, base_dir=self.test_dir)
        data = json_manip.read_file()
        self.assertEqual(data, self.sample_data)

    