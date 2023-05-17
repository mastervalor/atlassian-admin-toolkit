from call import Confluence
import json

set_up = Confluence(is_staging=True)
response = set_up.move_page('493159641', 4, 493159811)

# "ancestors": [
#                 {
#                     "id": ancestors
#                 }
#             ]

print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
