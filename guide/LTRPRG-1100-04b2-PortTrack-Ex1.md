Navigation :: [Previous Page](LTRPRG-1100-04b1-PortTrack.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04c1-NetAssist.md)

---

### Example 1: Tracking Switch Port Utilization like a Network Programmability Ninja

#### Objectives

The objectives for this exercise are to:

* Create a Python script on-box in Guest Shell to track when interfaces were last seen in an "up" state
* Leverage Embedded Event Manager to run the script on a regular basis
* Develop an ad-hoc reporting script to present the port usage history to an operator

#### Step 1: Identify the problem to solve

In large campus networks, often times network interfaces or ports are patched to a wall jack, whether or not they are
being used. Over time, the access switch may have all of its physical interfaces filled, creating a problem when a new
network drop needs to be added. When this scenario happens, often times the question will be asked, "What port can we
disconnect so that we can install a new network patch"?

While this may seem like a straightforward answer of looking for interfaces that are in the "down" state, this may not
necessarily be accurate enough. There are plenty of times that this may lead to a false positive, if an endpoint just
happened to be powered off, disconnected, or temporarily moved when the administrator checked the interface status. For
instance, consider a laptop that is 'docked' at a desk for portions of the day, but the end user takes it to meetings
throughout the day as well. If the network administrator were to check the interface status while that user was
attending a meeting, it may look like a valid port to reclaim. Unfortunately, if this happens, the user will come back
to find that the wired jack at the desk no longer works.

In order to prevent these false positives, more information about when the interface was last up is necessary. While
this information is not inherently tracked in a switch, there are several ways it can be collected. This example will
work through a method of collecting this information on a regular basis, so that if a port needs to be reclaimed, the
network administrator has a much better idea of which ports have been in an 'offline' state for a long period of time.

The high-level solution requires the following steps:

1. Gather and save the state of each interface on the switch or router, storing it in nonvolatile memory for later
access.

2. Continue to record these interface states on a regular interval, for instance, once every five minutes.

3. Provide a method that a user can request a report to see which ports have been unused for the longest period of time,
as they will be top choices for reclaiming to support a new network patch.

While there are other ways this problem can be solved, this shows one example of a simplistic, automated approach to
provide administrators better information to make a decision at the time of action. In this lab, we will have a few
additional steps to create additional interfaces that can be used to change state, so that the effectiveness of this
solution can be observed.

#### Step 2: Create Python script to collect data

With a good understanding of the problem to solve and a high-level approach, we can start putting together a script that
can gather and save these interface states. While we could make this script more intricate by either triggering from an
SNMP trap on interface state change, or even tracking input packet counts, we can still be very effective simply by monitoring
the interface state over time. We can write a script running in Guest Shell to utilize basic 'show' commands to provide
the data that we need, and then leverage file storage to record this data over time.

1. From the command line interface of the router, launch `bash` from the Guest Shell:
    ```
    csr1#guestshell run bash
    [guestshell@guestshell ~]$
    ```

2. wget the python script from github or use vi to open iosxe-porttrack.py and paste in the following contents:
    ```
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
    ```

    Remember that the `cli.execute` function is used to run IOS commands, so this how we gather interface states.
    Also, the information collected is being organized and written to the guest shell fileystem, so it can be easily 
    referenced by this script for updates. Additionally, we will develop a script that uses this file to create a
    user-friendly report. While you are not expected to be fluent in Python scripting, please read through the comments
    (signified by a #) and the subsequent lines of code to understand the basics of how this script operates.

#### Step 3: Setup IOS XE Embedded Event Manager to run script at a regular interval

Now that the Python script is created, it must be run regularly to provide be useful. IOS-XE can utilize a feature
called Embedded Event Manager (EEM) to schedule scripts to be run on a regular basis. While in the previous example we
saw the ability to use EEM based to run a script based on a trigger, this time it will be used to ensure the script is
run regularly.

1. Establish an SSH connection to the IOS XE device `csr1` by double clicking the CSR1 PuTTY icon on the desktop:
    
    ![CSR1 PuTTY Icon](assets/GuestShell-01.png)
    
2. From the IOS XE device CLI, ensure you are in privileged EXEC mode as indicated by the `csr1#` prompt.  If you are
in user EXEC mode as indicated by the `csr1>` prompt, then enter privileged EXEC mode with the `enable` command, for
example:
   
    ```
    csr1>enable
    csr1#
    ```
    
    ![CSR1 Privileged EXEC Mode](assets/GuestShell-02.png)

3. Next, enter the following lines to configure the EEM applet for our highcpu script:

    ```
    csr1(config)#event manager applet porttrack authorization bypass
    csr1(config-applet)#event timer cron cron-entry "* * * * *"
    csr1(config-applet)#action 0.01 cli command "enable"
    csr1(config-applet)#action 0.02 cli command "guestshell run python iosxe-porttrack.py"
    csr1(config-applet)#end

    ```

    In our lab, the cron entry is set to run every minute, of every hour, of every day of the month, on every month of
    the year, on every day of the week (each * is respective of the aforementioned list). In a production network, it
    may be sufficient to run this only once per five minutes ("*/5 * * * *") or only once per hour, 10 minutes after the
    hour ("10 * * * *"). This format is standard cron format commonly found in Unix or Linux operating systems.

#### Step 4: Develop a script that can be run as a report to find a good interface to reclaim  

The script we now have written and running regularly is reading interface states and saving historical data to a file in
JSON format. While this, on its own, would be sufficient in a pinch to find a port, unformatted JSON can be somewhat
difficult to read. As such, it is best to provide an easy-to-run and easy-to-read report of which ports are down and how
long it has been since they've been up.

1. From the router in our lab, enter Guest Shell:
    ```
    csr1#guestshell run bash
    [guestshell@guestshell ~]$
    ```

3. Either use wget to download `iosxe-portreport.py` or use vi to open `iosxe-portreport.py` and paste in the following:
    ```
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
    ```

    Please review this script to gain an understanding of the Python functions used, utilizing the comments to provide
    high-level guidance of the purpose of different segments of code.

4. Run the report from Guest Shell to test it:

    ```
    [guestshell@guestshell ~]$ python iosxe-portreport.py
    Open Interface Report

    [output omitted]
    ```

    Remember that this can be run directly from Exec mode CLI using the `guestshell run` command, which we will review
    later in this lab.

5. Type `exit` in the guest shell to return to IOS-XE CLI.

6. This lab is utilizing a CSR 1000V, which is somewhat lacking of dozens of interfaces that dynamically change state
as end users move around. We can still see the effectiveness of this script by mimicking this behavior through
loopback interfaces. Let's create a couple of loopback interfaces that we can administratively shut down and enable
at-will. This way we can simulate the behavior of an interface going offline. 

    ```
    csr1#config t
    csr1(config)#interface loopback2
    csr1(config-if)#ip address 10.129.129.129 255.255.255.255
    csr1(config-if)#shutdown
    csr1(config-if)#interface loopback3
    csr1(config-if)#ip address 10.129.129.130 255.255.255.255
    csr1(config-if)#no shutdown
    csr1(config-if)#end

    ```

7. Make sure to wait a minute or two for the scheduled port tracking script to run. We can check the report to ensure
that Loopback2 interface is now reported in the list of "down" interfaces. Once enough time has passed, change
the newly-created loopback3 interface to a down state.

    ```
    csr1#guestshell run python iosxe-portreport.py
    [output omitted]
    csr1#config t
    csr1(config)#interface loopback3
    csr1(config-if)#shutdown
    csr1(config-if)#end
    ```

8. After waiting a minute or two, we should now see Loopback3 in the list of down interfaces, with a "last up" time
within the last minute or two. 

    ```
    csr1#guestshell run python iosxe-portreport.py
    [output omitted]
    csr1#
    ```

While the interface state tracking may be less useful on a small router, hopefully this example shows the practicality
of such a concept when applied in larger environments, such as in a campus switch network.


---

Navigation :: [Previous Page](LTRPRG-1100-04b1-PortTrack.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04c1-NetAssist.md)
