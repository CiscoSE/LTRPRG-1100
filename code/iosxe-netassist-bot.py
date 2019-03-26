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


import requests


def msgToPersonEmail(botkey, toEmail, msg):
    myheaders = {
        "content-type": "application/json",
        "Authorization": "Bearer {}".format(botkey)
    }

    url = "https://api.ciscospark.com/v1/messages/"

    payload = '''{{ 
        "toPersonEmail": "{}",
        "markdown": "{}"
    }}'''.format(toEmail, msg)

    response = requests.post(url, headers=myheaders, data=payload)
    response.raise_for_status()

    return True


if __name__ == '__main__':
    # Use ArgParse to retrieve command line parameters
    from argparse import ArgumentParser

    parser = ArgumentParser("IOS XE Network Assistant Webex Teams Bot Script")

    # Retrieve the Webex Teams Bot Access Token and destination email
    parser.add_argument(
        "-t", "--token", help="Webex Teams Bot Access Token", required=True
    )

    parser.add_argument(
        "-e", "--email", help="Email to Send Message to", required=True
    )

    args = parser.parse_args()
    token = args.token
    email = args.email
    message = "**Alert!** Configuration change detected on network device."

    msgToPersonEmail(token, email, message)
