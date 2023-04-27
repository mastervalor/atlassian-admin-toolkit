import json
from call import call

response = call('users', 'get')

print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
