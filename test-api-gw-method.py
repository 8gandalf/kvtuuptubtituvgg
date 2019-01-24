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
url = '<URL>'
cmds = ['ls',
        'echo%20hello',
        'history',
        'quota',
        'touch%20test_file',
        'rm%20test_file',
        'cat%20lambda_function.py'
        ]

for cmd in cmds:
    test = url + cmd
req = requests.get(test)
    print("Status Code: {}\nResponse Body: {}".format(req.status_code, req.text))