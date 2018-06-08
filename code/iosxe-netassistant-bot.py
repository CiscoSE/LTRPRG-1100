#!/usr/bin/env python

#from ciscosparkapi import CiscoSparkAPI
import requests

def msgToPersonEmail(botkey, toEmail, msg):
    myheaders = {
        "content-type":"application/json",
        "Authorization":"Bearer {}".format(botkey)
    }
    url = "https://api.ciscospark.com/v1/messages/"
    payload = '''{{ 
        "toPersonEmail": "{}",
        "text": "{}"
    }}'''.format(toEmail, msg)
    response = requests.post(url, headers=myheaders, data=payload)
    response.raise_for_status()
    return True


if __name__ == '__main__':
    # Use ArgParse to retrieve command line parameters
    from argparse import ArgumentParser

    parser = ArgumentParser("Spark Check In")

    # Retrieve the Webex Teams Bot Access Token and destination email
    parser.add_argument(
        "-t", "--token", help="Webex Teams Bot Access Token", required=True
    )

    parser.add_argument(
        "-e", "--email", help="Email to Send to", required=True
    )

    args = parser.parse_args()
    token = args.token
    email = args.email
    message = "**Alert:** Config Changed"
    #api = CiscoSparkAPI(access_token=token)
    #api.messages.create(toPersonEmail=email, markdown=message)

    msgToPersonEmail(token, email, message)
