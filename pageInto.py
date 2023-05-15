from call import Confluence
import json

set_up = Confluence(is_staging=True)
response = set_up.conf_call('content/493159641?expand=ancestors')


print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))







