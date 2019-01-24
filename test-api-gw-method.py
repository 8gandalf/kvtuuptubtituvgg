import requests
import zipfile
import json
import io
import os.path
import astroid           
import asyncio           
import awscli            
import rsa               
import s3transfer        

# api gateway testing
url = 'https://i0hs6b0gn5.execute-api.us-west-2.amazonaws.com/test/cmd?param1='
cmds = ['ls',
        'echo%20hello',
        'history',
        'quota',
        'touch%20test_file',
        'rm%20test_file',
        'cat%20lambda_function.py'
        ]

# Extract the endpoint resource name
file_name = url.split("/")[-1].replace('.zip', '')        

for cmd in cmds:
    test = url + cmd
req = requests.get(test)
    print("Status Code: {}\nResponse Body: {}".format(req.status_code, req.text))