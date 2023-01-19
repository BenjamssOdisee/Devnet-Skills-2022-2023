from test_data import *
def json_search(key,input_object):
    ret_val=[]
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                temp={k:v}
                ret_val.append(temp)
print(json_search("issueSummary",data))
