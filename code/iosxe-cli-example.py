#!/usr/bin/env python

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
