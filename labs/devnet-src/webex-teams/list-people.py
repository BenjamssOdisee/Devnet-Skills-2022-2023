import requests
import json
access_token = 'NDg1MWJlN2YtNGRkOC00YmI0LWJhNDAtYjc2MWRmYzkzYjlhZGEzMDg3MGItMmJk_PE93_715b0668-72c8-44da-be57-2e5ab1929d3a'
url = 'https://webexapis.com/v1/people'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {
 'email': 'benjamin.ghosez@student.odisee.be'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS83YTIxMDRmOS01MGEyLTRhNjgtOGJmMy04M2NjMzlkZDg4MTg'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

