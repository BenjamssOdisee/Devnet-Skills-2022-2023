import json

groups_struc = {
 "groups": [
      { "group": { "group_id": "G-A" 
                 , "group_name": "DEVASC_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Noel", "person_lastname": "VanPoppen", "email": "noel@odisee.be"},
                     {"person_id": "P-2" , "person_name": "Mary", "person_lastname": "Roeremans", "email": "mary@odisee.be"},
                     {"person_id": "P-3" , "person_name": "Jens", "person_lastname": "VDB", "email": "jens@odisee.be"} 
                   ]
                 }
      },
      { "group": { "group_id": "G-B" 
                 , "group_name": "DEVASC_B" ,    
                   "members": [   
                     {"person_id": "P-4" ,"person_name": "Ives", "person_lastname": "VanDePutte",  "email": "ives@odisee.be"}, 
                     {"person_id": "P-5" ,"person_name": "John", "person_lastname": "VanBerg",  "email": "john@odisee.be"}, 
                     {"person_id": "P-6" ,"person_name": "Alec", "person_lastname": "Hermans",  "email": "alec@odisee.be"} 
                   ]     
                 }
      },
      { "group": { "group_id": "G-C" , 
                   "group_name": "DEVASC_C" ,    
                   "members": [   
                     {"person_id": "P-7" ,"person_name": "Matt", "person_lastname": "VKL", "email": "matt@odisee.be"}, 
                     {"person_id": "P-8" ,"person_name": "Paul", "person_lastname": "Colruyt", "email": "paul@odisee.be"}, 
                     {"person_id": "P-9" ,"person_name": "Elvi", "person_lastname": "De Croo", "email": "elvi@odisee.be"} 
                   ] 
                 }
      }
   ]
}

# ### Select first group, first person
# resp_a1 = groups_struc["groups"][0]["group"]["DEVASC_A"]
# resp_a2 = groups_struc["groups"][0]["group"]["members"][0]["person_name"]

# ### Select second group; first person
# resp_b1 = groups_struc["groups"][1]["group"]["DEVASC_B"]
# resp_b2 = groups_struc["groups"][1]["group"]["members"][0]["person_name"]

# for g in groups_struc["groups"]:
#     print(g["group"]["group_name"])
#     for p in g["group"]["members"]:
#         print(p["person_name"]  + " " + p["person_lastname"]+ ", email: " + p["email"] + " => id: " + p["person_id"])

     
print('------1---------')
print(type(groups_struc))
print(groups_struc)
print('------1A--------')
# convert dict into json string
js_groups = json.dumps(groups_struc)
print(type(js_groups))
print(js_groups)
#print(json.dumps(groups_struc, indent=2))

print('------2---------')
for grp in groups_struc["groups"]:
    print('------2A--------')
    print(type(grp))
    print(grp)
    print('------2B--------')
    print(grp["group"]["group_name"])
    print('------2C--------')
    for per in grp["group"]["members"]:
        print(per["person_name"] + " => " + per["email"])
            
print('------3---------')
print(groups_struc.keys())
print('------3A---------')
print(groups_struc["groups"][0].keys())
print('------3B---------')
print(groups_struc["groups"][0]["group"].keys())
print('------3C---------')
print(groups_struc["groups"][0]["group"]["members"][0].keys())


#Transforming DICT into JSON
import json
js_groups = json.dumps(groups_struc)
print(json.dumps(groups_struc, indent=2))

#Transforming JSON into YAML
import yaml
yaml_data = yaml.dump(groups_struc)
print(yaml_data)

#Transforming JSON into XML
from dicttoxml import dicttoxml
xml_data = dicttoxml(groups_struc)
print(xml_data)