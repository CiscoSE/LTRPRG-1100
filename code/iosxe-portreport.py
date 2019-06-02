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


import json

# Attempt to open the JSON data file as source of report. Load file into a Python dict.
# If file does not exist, exit, as we have nothing to report.
try:
    fp = open('/home/guestshell/porthistory.json','r')
    filebuffer = fp.read()
    portstatus = json.loads(filebuffer)
    fp.close()
except IOError:
    quit("""Sorry, no report found. 
    
    Add iosxe-porttrack.py to EEM cron applet or run manually on a regular basis first.""")

# Create an empty list to populate with results
report = []

# Print header on screen
print("Open Interface Report\n\n")

# Iterate through interfaces in JSON, only adding details for ones that are down
for intfname,intfdetails in portstatus.items():
    if(intfdetails['status'] == 'down'):
        report.append(intfname+" is down. It was last seen up "+intfdetails['lastup'])

# Primitively sort interfaces in our report list, then print to screen it line by line.
report.sort()

for line in report:
    print(line)
