import requests
import sys
import os
import json
ip_file = sys.argv[1]
if not os.path.isfile(ip_file):
    print("ERROR: File %s does not exist" % ip_file)
    exit(1)
with open(ip_file,'r') as f:
    for ip in f:
        ip = ip.rstrip()

        request_loc = 'http://freegeoip.net/json/' + ip
        location_dat = requests.get(request_loc).content
        
        obfuscated_ip = ip
        
        root = json.loads(location_dat)
        print("%s,%s,%s,%s,%s" % (obfuscated_ip, root["city"], root["region_name"], root["latitude"], root["longitude"]))

        if not ip: continue
