import unittest
import os
import json
from file_manip.json_file_manip import JSONManip


class TestJSONManip(unittest.TestCase):
    def setUp(self):
        # Set up test files and directories
        self.test_dir = 'test_json_files'
        os.makedirs(self.test_dir, exist_ok=True)
