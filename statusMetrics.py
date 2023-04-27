import csv
import os
import json
from call import status_metrics

statuses = status_metrics()

print(json.dumps(statuses, sort_keys=True, indent=4, separators=(",", ": ")))