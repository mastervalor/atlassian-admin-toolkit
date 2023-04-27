from call import call


response = call('permissionscheme', 'get')


for i in response['permissionSchemes']:
    print(i['name'])

# print(json.dumps(response, sort_keys=True, indent=4, separators=(",", ": ")))