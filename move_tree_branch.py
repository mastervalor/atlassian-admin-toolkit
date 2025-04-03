from calls.confluence_api_calls.conf_api_pages import ConfluencePageCalls
import json

conf_pages = ConfluencePageCalls()
page_tree = conf_pages.get_child_pages_recursive('324733855')
print(json.dumps(page_tree, sort_keys=True, indent=4, separators=(",", ": ")))
