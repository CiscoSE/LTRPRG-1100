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

HOST = '198.18.134.11'
PORT = 830
USER = 'netconf'
PASS = 'C1sco12345'

# NETCONF Config Template to use
netconf_payload = open("iosxe-config-eem.xml").read()

if __name__ == '__main__':

    # Print the NETCONF payload
    print("Configuration Payload:\n")
    print(netconf_payload)

    with manager.connect(host=HOST, port=PORT,
                         username=USER,
                         password=PASS,
                         hostkey_verify=False) as m:

        # Send NETCONF <edit-config> command with payload
        netconf_reply = m.edit_config(netconf_payload, target="running")

        # Print the NETCONF reply
        print("Configuration result:\n")
        print(netconf_reply)
