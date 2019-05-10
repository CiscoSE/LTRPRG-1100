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
import xml.dom.minidom

m = manager.connect(host="198.18.134.11",
                    port="830",
                    username="netconf",
                    password="C1sco12345",
                    hostkey_verify=False)

config = m.get_config("running")

print(xml.dom.minidom.parseString(config.xml).toprettyxml())

m.close_session()
