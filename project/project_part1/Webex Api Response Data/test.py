import requests
import json

access_token = 'ZmRkYWQxYWUtOTg2Yy00ZWZkLWE3ZGItZWVjZGQyYjYyNjVmMGNlM2U5NjYtMzMx_PE93_715b0668-72c8-44da-be57-2e5ab1929d3a'
url = 'https://api.ciscospark.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))


