# Load modules necessary for this script
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


