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

timestamp = cli.execute("show clock")
processes = cli.execute("show proc cpu sort")
histogram = cli.execute("show proc cpu hist")
users = cli.execute("show users")

fp = open('/bootflash/highcpulog.txt','w')

fp.write("High CPU at "+timestamp+"\n\n")

processlines = processes.splitlines()

fp.write("CPU and top ten processes:\n\n")

for x in range(0,12):
    fp.write(processlines[x]+"\n")
    fp.write("CPU histogram:\n\n")
    fp.write(histogram+"\n\n")
    fp.write("Active users:\n\n")
    fp.write(users+"\n\n")

fp.close()

topproc = processlines[2][65:]

cli.execute("send log 3 High CPU detected. Check /bootflash/highcpulog.txt : Top process: "+topproc)
