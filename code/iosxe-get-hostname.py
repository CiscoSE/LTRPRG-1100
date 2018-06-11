#!/usr/bin/env python
#
from ncclient import manager
import sys
import xml.dom.minidom as DOM

# the variables below assume the user is leveraging a
# Vagrant Image running IOS-XE 16.6
HOST = '198.18.134.11'
# use the NETCONF port for your IOS-XE
PORT = 830
# use the user credentials for your IOS-XE
USER = 'netconf'
PASS = 'C1sco12345'


def main():
    """
    Main method that retrieves the hostname from config via NETCONF.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        # XML filter to issue with the get operation
        hostname_filter = """
                        <filter>
                            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                            </native>
                        </filter>
                        """

        result = m.get_config('running', hostname_filter)
        xml_doc = DOM.parseString(result.xml)
        hostname_obj = xml_doc.getElementsByTagName("hostname")
        hostname = hostname_obj[0].firstChild.nodeValue
        print(hostname)


if __name__ == '__main__':
    sys.exit(main())
