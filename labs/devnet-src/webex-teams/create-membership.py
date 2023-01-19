import requests
access_token = 'NDg1MWJlN2YtNGRkOC00YmI0LWJhNDAtYjc2MWRmYzkzYjlhZGEzMDg3MGItMmJk_PE93_715b0668-72c8-44da-be57-2e5ab1929d3a'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNzZmZGQ0MzAtOGViMy0xMWVkLTg5NDUtMjUxYmU1YzY2ZDll'
person_email = 'maximilien.diallo@student.odisee.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())

