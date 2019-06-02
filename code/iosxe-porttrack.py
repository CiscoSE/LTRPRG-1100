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


import cli
import re
import datetime
import json

# Gather interface state from CLI command
intf = cli.execute("show interface | inc line proto")

# Convert single string of all interfaces
# to a Python list with one interface per list entry
intflist = re.split(r"\n(?=[A-Z])",intf)

# Load up existing JSON file of previous interface states, if exists.
# If it doesn't exist, create an empty Python dictionary
try:
    fp = open('/home/guestshell/porthistory.json','r')
    filebuffer = fp.read()
    portstatus = json.loads(filebuffer)
    fp.close()
except IOError:
    portstatus = dict()

# Loop through each interface item
# - If interface is up, record its state and update 'last up' time with current time
#
# - If interface is down, record its state. If first time this interface is being recorded,
#   then set the 'last up' time as 'never'
for interface in intflist:
    if("is up" in interface):
        intfname = interface.split(" ")[0]
        if(intfname not in portstatus):
            portstatus[intfname] = {}
        portstatus[intfname]['status'] = 'up'
        portstatus[intfname]['lastup'] = str(datetime.datetime.now())
    elif("is down" in interface):
        intfname = interface.split(" ")[0]
        if(intfname not in portstatus):
            portstatus[intfname] = {}
            portstatus[intfname]['lastup'] = 'never'
        portstatus[intfname]['status'] = 'down'

# Open a file for writing (overwriting) and then save the results as JSON.
fp = open('/home/guestshell/porthistory.json','w')

fp.write(json.dumps(portstatus))

fp.close()
