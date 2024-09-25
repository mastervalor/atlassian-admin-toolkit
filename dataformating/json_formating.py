import json


class JSONFormating:
    @staticmethod
    def pretty_json(file):
        print(json.dumps(file, sort_keys=True, indent=4, separators=(",", ": ")))
