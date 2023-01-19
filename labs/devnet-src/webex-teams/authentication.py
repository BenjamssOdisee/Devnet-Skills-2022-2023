import requests
import json
access_token = 'NDg1MWJlN2YtNGRkOC00YmI0LWJhNDAtYjc2MWRmYzkzYjlhZGEzMDg3MGItMmJk_PE93_715b0668-72c8-44da-be57-2e5ab1929d3a'
url = 'https://webexapis.com/v1/people/me'
headers = {
 'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

