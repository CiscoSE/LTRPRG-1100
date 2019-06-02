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

# NETCONF payload
payload = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <event>
                <manager xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-eem">
                    <applet>
                        <name>GUESTSHELL-CONFIG-CHANGE-NETASSIST-BOT</name>
                        <event>
                            <syslog>
                                <pattern>%SYS-5-CONFIG_I: Configured from</pattern>
                            </syslog>
                        </event>
                        <action>
                            <name>0.0</name>
                            <cli>
                                <command>enable</command>
                            </cli>
                        </action>
                        <action>
                            <name>1.0</name>
                            <cli>
                                <command>guestshell run python /bootflash/scripts/iosxe-netassist-bot.py -t OWIyODVhODEtMDM0MC00NmY5LWFmYjEtOTI1ODJiZWFiNzIyODdlY2FiOGItMTQ3 -e email@example.com</command>
                            </cli>
                        </action>
                    </applet>
                </manager>
            </event>
        </native>
    </config>
    """

m = manager.connect(host="198.18.134.11",
                    port="830",
                    username="netconf",
                    password="C1sco12345",
                    hostkey_verify=False)

response = m.edit_config(payload, target="running")

print(response)

m.close_session()
