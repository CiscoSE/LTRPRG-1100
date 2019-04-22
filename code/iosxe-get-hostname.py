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
import xml.dom.minidom as dom

HOST = '198.18.134.11'
PORT = 830
USER = 'netconf'
PASS = 'C1sco12345'


def main():
    # Main method that prints hostname of remote device.

    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        # XML filter to issue with the get operation.
        hostname_filter = """
                        <filter>
                            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                            </native>
                        </filter>
                        """

        result = m.get_config('running', hostname_filter)
        xml_doc = dom.parseString(result.xml)
        hostname_obj = xml_doc.getElementsByTagName("hostname")
        hostname = hostname_obj[0].firstChild.nodeValue
        print(hostname)


if __name__ == '__main__':
    sys.exit(main())
