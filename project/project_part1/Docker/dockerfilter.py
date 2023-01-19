import json
import requests


#Example 1#########################################""
print("---------------Example1----------------")


print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict = json.loads(docker_json_file2)
print(docker_dict[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json = json.dumps(docker_dict)
print("---------3--------")
print("Filtering from dict")
print(docker_dict[0]["Created"])
print(docker_dict[0]["Architecture"])
print(docker_dict[0]["Os"])

#Example 2##############################
print("---------------Example2----------------")

import json
print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict2 = json.loads(docker_json_file)
print(docker_dict2[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json2 = json.dumps(docker_dict2)
print("Filtering from dict")
print(docker_dict2[0]["Name"])
print(docker_dict2[0]["Created"])
print(docker_dict2[0]["Containers"]["4e99a64e...bd52826d786db9a3be2811"]["IPv4Address"])

