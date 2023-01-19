import json 

rack_struc = {
 "rack": [
      { "server": { "dev_id": "S1" , "server_name": "svr1" , "domain": "biasc.be", "ip-address": "10.2.3.1" ,
                     "os": "linux"  , "server_type": "vm" ,
                     "services": [   
                       {"service": "ad" , "service_type": "vm", "protocol": "tcp", "port": "389"},
                       {"service": "dns", "service_type": "vm", "protocol": "udp", "port": "53"},
                       {"service": "ntp", "service_type": "vm", "protocol": "tcp", "port": "123"} 
                    ]
                  }
      },
      { "server": { "dev_id": "S2" , "server_name": "svr2" , "domain": "biasc.be", "ip-address": "10.2.3.2" ,
                            "os": "linux"  , "server_type": "vm" ,
                            "services": [   
                            {"service": "flask", "service_type": "vm", "protocol": "tcp", "port": "8089"  }, 
                            {"service": "db"   , "service_type": "vm", "protocol": "tcp", "port": "1521"  } 
                            ]     
                        }
                  },
            { "server": { "dev_id": "S3" , "server_name": "svr3" ,  "domain": "biasc.be" , "ip-address": "10.2.3.3",
                            "os": "linux"  , "server_type": "vm" ,
                            "services": [   
                            {"service": "dns" , "service_type": "vm", "protocol": "tcp", "port": "8089" }, 
                            {"service": "ntp" , "service_type": "vm", "protocol": "tcp", "port": "8089" },
                            {"service": "dhcp", "service_type": "docker", "protocol": "udp", "port": "67" }
                            ] 
                        }
            }
        ]
        }


#YANG leaves are comparable to a Python dict structure; YANG lists are comparable to an array (or list) in Python.

### all servers, services, ip addresses, protocol/ports

for g in rack_struc["rack"]:
    print("Server: " + g["server"]["server_name"])
    print("IP Address: " + g["server"]["ip-address"])
    for p in g["server"]["services"]:
        print(p["service"] + " => " + p["protocol"] + "/" + p["port"])
        
####################################################

print('------1---------')
#print(devices_struc)
#print('------1A--------')
js_groups = json.dumps(rack_struc)
print(js_groups)
print(json.dumps(rack_struc, indent=2))

print('------2---------')
for g in rack_struc["rack"]:
    print('------2A--------')
    print(type(g))
    print(g)
    print(g["server"]["services"])
    for p in g["server"]["services"]:
        print(p)
            
print('------3---------')
print(rack_struc.keys())
print('------3A---------')
print(rack_struc["rack"][0].keys())
print('------3B---------')
print(rack_struc["rack"][0]["server"].keys())
print('------3C---------')
print(rack_struc["rack"][0]["server"]["services"][0].keys())

#Transforming DICT into JSON
js_struc = json.dumps(rack_struc)
print(type(js_struc))
print(js_struc)
print(json.dumps(rack_struc, indent=4))
#Transforming JSON into YAML
import yaml
yaml_data = yaml.dump(rack_struc)
print(yaml_data)
#Transforming JSON into XML
from dicttoxml import dicttoxml
xml_data = dicttoxml(rack_struc)
print(xml_data)


