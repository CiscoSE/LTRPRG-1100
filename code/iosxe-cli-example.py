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


import sys
import cli

intf = sys.argv[1:]
intf = ''.join(intf[0])

print("\nConfiguring interface %s with 'configurep' function...\n") % intf

cli.configurep(["interface " + intf, "ip address 10.55.55.55 255.255.255.0", "no shut", "end"])

print("\nConfiguring interface %s with 'configure' function...\n") % intf

cmd = 'interface %s,logging event link-status,end' % intf
cli.configure(cmd.split(','))

print("Printing show command output with 'executep' function...\n")

cli.executep('show ip interface brief')

print("\nPrinting show command with 'execute' function...\n")

output = cli.execute('show run interface %s' % intf)

print(output)

print("\nConfiguring interface %s with 'cli' function...\n" % intf)

cli.cli('config terminal; interface %s; description Configured with a Python script from Guest Shell' % intf)

print("Printing show command with 'clip' function...")

cli.clip('show run interface %s' % intf)
