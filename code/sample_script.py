#!/usr/bin/env python

import sys
import cli

intf= sys.argv[1:]
intf = ''.join(intf[0])

print "\n\n *** Configuring interface %s with 'configurep' function *** \n\n" %intf

cli.configurep(["interface loopback55","ip address 10.55.55.55 255.255.255.0","no shut","end"])

print "\n\n *** Configuring interface %s with 'configure' function *** \n\n"

cmd='interface %s,logging event link-status ,end' % intf

cli.configure(cmd.split(','))

print "\n\n *** Printing show cmd with 'executep' function *** \n\n"

cli.executep('show ip interface brief')

print "\n\n *** Printing show cmd with 'execute' function *** \n\n"

output= cli.execute('show run interface %s' %intf)

print (output)

print "\n\n *** Configuring interface %s with 'cli' function *** \n\n"

cli.cli('config terminal; interface %s; spanning-tree portfast edge default' %intf)

print "\n\n *** Printing show cmd with 'clip' function *** \n\n"

cli.clip('show run interface %s' %intf)