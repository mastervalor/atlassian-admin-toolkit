from call import call, conf_call
import json


response = conf_call('space?limit=1000&type=global&status=current&expand=description.plain.value')

print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
