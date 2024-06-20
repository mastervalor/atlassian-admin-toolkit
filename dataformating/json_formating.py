import json


class JSONFormating:
    def __init__(self, file):
        self.file = file

    def pretty_json(self):
        print(json.dumps(self.file, sort_keys=True, indent=4, separators=(",", ": ")))
