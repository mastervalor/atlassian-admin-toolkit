from call import Confluence
import json

set_up = Confluence()
get_groups = set_up.conf_call('group')

print(json.dumps(get_groups, sort_keys=True, indent=4, separators=(",", ": ")))