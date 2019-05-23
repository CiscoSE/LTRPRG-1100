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


from ncclient import manager
import sys

m = manager.connect(host="198.18.134.11",
                    port="830",
                    username="netconf",
                    password="C1sco12345",
                    hostkey_verify=False)

print("This remote network device supports the following capabilities:\n")

for capability in m.server_capabilities:
    print(capability.split('?')[0])

m.close_session()
