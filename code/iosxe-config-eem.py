#!/usr/bin/env python

from ncclient import manager

HOST = '198.18.134.11'
PORT = 830
USER = 'netconf'
PASS = 'C1sco12345'

# NETCONF Config Template to use
netconf_payload = open("iosxe-config-eem.xml").read()

if __name__ == '__main__':

    print("Configuration Payload:\n")
    print(netconf_payload)

    with manager.connect(host=HOST, port=PORT,
                         username=USER,
                         password=PASS,
                         hostkey_verify=False) as m:

        # Send NETCONF <edit-config> command with payload
        netconf_reply = m.edit_config(netconf_payload, target="running")

        # Print the NETCONF reply
        print(netconf_reply)
