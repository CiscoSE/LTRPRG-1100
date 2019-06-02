#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""


import requests
import urllib3
import json
from requests.auth import HTTPBasicAuth

# Silence the insecure snake oil SSL certificate warning.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = "devnetuser"
password = "Cisco123!"

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

response = requests.request("POST",
                            url,
                            auth=HTTPBasicAuth(username, password),
                            # Ignore insecure snake oil SSL certificate
                            verify=False)

token = response.json()["Token"]

print(response.text)

headers = {
    'X-Auth-Token': token
}


url = "https://sandboxdnac.cisco.com/api/v1/host"

response = requests.request("GET",
                            url,
                            headers=headers,
                            # Ignore insecure snake oil SSL certificate
                            verify=False)

print(response.text)
