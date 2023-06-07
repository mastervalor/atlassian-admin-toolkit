from call import Confluence
import json

set_up = Confluence()
response = set_up.conf_call('content/427818468')


print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))







