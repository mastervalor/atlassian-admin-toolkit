from calls.confluence_api_calls.conf_api_pages import ConfluencePageCalls
import json

set_up = ConfluencePageCalls(is_staging=True)
response = set_up.move_page('493159641', 4, 493159811)

# "ancestors": [
#                 {
#                     "id": ancestors
#                 }
#             ]

print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))
