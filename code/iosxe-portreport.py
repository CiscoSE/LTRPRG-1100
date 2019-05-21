# Import modules necessary
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
