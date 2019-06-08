Navigation :: [Previous Page](LTRPRG-1100-04b1-PortTrack.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04c1-NetAssist.md)

---

### Example 1: Tracking Switch Port Utilization like a Network Programmability Ninja

#### Objectives

The objectives for this exercise are to:

* Create a Python script on-box in Guest Shell to track when interfaces were last seen in an "up" state
* Leverage Embedded Event Manager to run the script on a regular basis
* Run a script to report the port usage history to an operator

#### Step 1: Creating a Port Tracker Python Script

With a good understanding of the problem to solve and a high-level approach, we can start putting together a script that
can gather and save interface state. While we could make this script more intricate by either triggering from an SNMP
trap on interface state change, or even tracking input packet counts, we can still be very effective simply by 
monitoring the interface state over time. We can write a script running in Guest Shell to utilize basic IOS XE EXEC 
mode `show` commands to provide the data that we need, and then leverage file storage to NVRAM to record and report 
this data over time.

1. Establish an SSH connection to the IOS XE device `csr1` by double clicking the CSR1 PuTTY icon on the desktop:
    
    ![CSR1 PuTTY Icon](assets/CSR1-Icon.png)
    
    ![CSR1 Terminal](assets/CSR1-Term.png)

2. From the IOS XE device CLI, ensure you are in privileged EXEC mode as indicated by the `csr1#` prompt.  If you are
in user EXEC mode as indicated by the `csr1>` prompt, then enter privileged EXEC mode with the `enable` command, for
example:
   
    ```
    csr1>enable
    csr1#
    ```

3. Enter a Guest Shell interactive session with the IOS XE command `guestshell run bash`, for example:
    
    ```
    csr1#guestshell run bash
    [guestshell@guestshell ~]$
    ```

4. There is an example Python script `iosxe-porttrack.py` in this lab's Git repository.  Let's create a directory on 
the network device `bootflash:`, transfer the file to the network device file system, and run the script.
    
    To create a new directory to hold scripts on-box if one does not already exist, use the `mkdir -p /bootflash/scripts` 
    command from the Guest Shell `[guestshell@guestshell ~]$` prompt, for example:
    
    ```
    [guestshell@guestshell ~]$ mkdir -p /bootflash/scripts
    [guestshell@guestshell ~]$
    ```
    
    Change to that directory with the `cd /bootflash/scripts` command, for example:
    
    ```
    [guestshell@guestshell ~]$ cd /bootflash/scripts
    [guestshell@guestshell scripts]$
    ```
    
    Transfer the example script with the `wget https://raw.githubusercontent.com/CiscoSE/LTRPRG-1100/master/code/iosxe-porttrack.py` command, for example:
        
    ```
    [guestshell@guestshell scripts]$ wget https://raw.githubusercontent.com/CiscoSE/LTRPRG-1100/master/code/iosxe-porttrack.py
    --2019-05-31 19:51:49--  https://raw.githubusercontent.com/CiscoSE/LTRPRG-1100/master/code/iosxe-porttrack.py
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.0.133, 151.101.64.133, 151.101.128.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.0.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 1615 (1.6K) [text/plain]
    Saving to: 'iosxe-porttrack.py'
    
    100%[======================================>] 1,615       --.-K/s   in 0s
    
    2019-05-31 19:51:50 (76.3 MB/s) - 'iosxe-porttrack.py' saved [1615/1615]
    
    [guestshell@guestshell scripts]$
    ```
    
    This Python script uses the IOS XE Python CLI module `cli.execute` function to run IOS XE EXEC mode commands from
    Guest Shell.  This is how we gather interface state.  The information collected is being organized and written to
    the Guest Shell filesystem, so it can be easily referenced by this script to maintain a port utilization history 
    over time.  Additionally, we will develop a script that uses this file to create a user-friendly report.
    
    While you are not expected to be fluent in Python scripting, please read through the comments (signified by a `#`
    in the Python code) and the subsequent lines of code to understand the basics of how this script operates.  You 
    can view [this Python script](https://github.com/CiscoSE/LTRPRG-1100/blob/clus19/code/iosxe-porttrack.py) in 
    this lab's GitHub repository at `https://github.com/CiscoSE/LTRPRG-1100/blob/clus19/code/iosxe-porttrack.py`.
    
    TODO: Update URL to this file.
    
5. Exit out of the Guest Shell Bash CLI session with the `exit` command:
    
    ```
    [guestshell@guestshell scripts]$ exit
    csr1#
    ```

#### Step 2: Using IOS XE Embedded Event Manager to Run the Port Tracker Python Script

Now that the Python script is on our network device, it must be run regularly to be useful. IOS XE can utilize a feature
called Embedded Event Manager (EEM) to schedule scripts to be run on a regular basis.

1. From the IOS XE device CLI, ensure you are in privileged EXEC mode as indicated by the `csr1#` prompt.  If you are
in user EXEC mode as indicated by the `csr1>` prompt, then enter privileged EXEC mode with the `enable` command, for
example:
   
    ```
    csr1>enable
    csr1#
    ```

2. Enter global configuration mode, which will be indicated by the `csr1(config)#` prompt, with the
`configure terminal` command, for example:
    
    ```
    csr1#configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    csr1(config)#
    ```

3. Run the following IOS XE commands in config mode to configure an EEM applet to create a cron entry to run our port 
tracker script automatically:
    
    ```
    event manager applet porttrack authorization bypass
    event timer cron cron-entry "* * * * *"
    action 0.01 cli command "enable"
    action 0.02 cli command "guestshell run python /bootflash/scripts/iosxe-porttrack.py"
    ```
    
    For example:
    
    ```
    csr1(config)#event manager applet porttrack authorization bypass
    csr1(config-applet)#event timer cron cron-entry "* * * * *"
    csr1(config-applet)#action 0.01 cli command "enable"
    csr1(config-applet)#action 0.02 cli command "guestshell run python /bootflash/scripts/iosxe-porttrack.py"
    ```
    
    End the global configuration mode session with the `end` command or typing `CTRL-Z`, for example:
    
    ```
    csr1(config)#end
    csr1#
    ```
    
    cron is a time-based job scheduler.  In this lab, the cron entry is set to run every minute, of every hour, of 
    every day of the month, on every month of the year, on every day of the week (each `*` is respective of the 
    aforementioned list). In a production network, it may be sufficient to run this only once per five minutes (for 
    example, `*/5 * * * *`) or only once per hour, 10 minutes after the hour (for example, `10 * * * *`). This format
    is standard cron format commonly found in Unix or Linux operating systems.

#### Step 3: Scripting a Report of Historical Port Usage  

The Python script running on a regular basis is reading interface states and saving historical data to a file in
JSON format. While this, on its own, would be sufficient in a pinch to find a port, raw unformatted JSON can be 
somewhat difficult to read. As such, it is best to provide an easy-to-run and easy-to-read report of which ports are 
down and how long it has been since they've been up.

1. From the IOS XE device CLI, ensure you are in privileged EXEC mode as indicated by the `csr1#` prompt.  If you are
in user EXEC mode as indicated by the `csr1>` prompt, then enter privileged EXEC mode with the `enable` command, for
example:
   
    ```
    csr1>enable
    csr1#
    ```

2. Enter a Guest Shell interactive session with the IOS XE command `guestshell run bash`, for example:
    
    ```
    csr1#guestshell run bash
    [guestshell@guestshell ~]$
    ```

3. There is an example Python script `iosxe-portreport.py` in this lab's Git repository.  Let's transfer the file to 
the network device file system in the directory `/bootflash/scripts` created earlier in this lab.
    
    Transfer the example script with the `wget https://raw.githubusercontent.com/CiscoSE/LTRPRG-1100/master/code/iosxe-portreport.py` command, for example:
        
    ```
    [guestshell@guestshell scripts]$ wget https://raw.githubusercontent.com/CiscoSE/LTRPRG-1100/master/code/iosxe-portreport.py
    --2019-05-31 19:53:10--  https://raw.githubusercontent.com/CiscoSE/LTRPRG-1100/master/code/iosxe-portreport.py
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.128.133, 151.101.192.133, 151.101.0.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.128.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 1001 [text/plain]
    Saving to: 'iosxe-portreport.py'
    
    100%[======================================>] 1,001       --.-K/s   in 0s
    
    2019-05-31 19:53:10 (57.9 MB/s) - 'iosxe-portreport.py' saved [1001/1001]
    
    [guestshell@guestshell scripts]$
    ```

4. Run the Python report script with the `python iosxe-portreport.py` command from the Guest Shell 
`[guestshell@guestshell ~]$` prompt, for example:
    
    ```
    [guestshell@guestshell scripts]$ python iosxe-portreport.py
    Open Interface Report
    
    
    [guestshell@guestshell scripts]$
    ```

5. Exit out of the Guest Shell Bash CLI session with the `exit` command:
    
    ```
    [guestshell@guestshell scripts]$ exit
    csr1#
    ```

6. This lab is utilizing a CSR 1000V, which is somewhat lacking of dozens of interfaces that dynamically change state
as end users move around. We can still see the effectiveness of this script by simulating this behavior through
Loopback interfaces. Let's create a couple of Loopback interfaces that we can administratively shut down and enable
at-will. This way we can simulate the behavior of periodic interface usage.
    
    Enter global configuration mode, which will be indicated by the `csr1(config)#` prompt, with the
    `configure terminal` command, for example:
   
    ```
    csr1#configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    csr1(config)#
    ```
    
    Run the following IOS XE commands in config mode to create and configure two test interfaces:
    
    ```
    interface Loopback2
      ip address 10.129.129.129 255.255.255.255
      shutdown
      exit
    interface Loopback3
      ip address 10.129.129.130 255.255.255.255
      no shutdown
      exit
    end
    ```
    
    For example:
    
    ```
    csr1(config)#interface Loopback2
    csr1(config-if)#ip address 10.129.129.129 255.255.255.255
    csr1(config-if)#shutdown
    csr1(config-if)#exit
    csr1(config)#interface Loopback3
    csr1(config-if)#ip address 10.129.129.130 255.255.255.255
    csr1(config-if)#no shutdown
    csr1(config-if)#exit
    csr1(config)#end
    csr1#
    ```

7. Make sure to wait a minute or two for the scheduled port tracking script to run. We can check the report to ensure
that the Loopback2 interface is now reported in the list of "down" interfaces.
    
    We can run the Python report script in Guest Shell from the IOS XE device privileged EXEC mode with the 
    `guestshell run python /bootflash/scripts/iosxe-portreport.py` command, for example:
    
    ```
    csr1#guestshell run python /bootflash/scripts/iosxe-portreport.py
    Open Interface Report
    
    
    Loopback2 is down. It was last seen up never
    
    csr1#
    ```

8. Once enough time has passed, simulate a port usage change by manually configuring the newly-created Loopback3 
interface to a down state.
    
    Enter global configuration mode, which will be indicated by the `csr1(config)#` prompt, with the
    `configure terminal` command, for example:
    
    ```
    csr1#configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    csr1(config)#
    ```
    
    Run the following IOS XE commands in config mode to simulate a change in port usage:
    ```
    interface Loopback3
      shutdown
      exit
    end
    ```
    
    For example:
    
    ```
    csr1(config)#interface Loopback3
    csr1(config-if)#shutdown
    csr1(config-if)#exit
    csr1(config)#end
    csr1#
    ```

9. After waiting a minute or two, we should now see the Loopback3 interface in the list of down interfaces, with a 
"last up" time within the last minute or two. 

    We can run the Python report script in Guest Shell from the IOS XE device privileged EXEC mode with the 
    `guestshell run python /bootflash/scripts/iosxe-portreport.py` command, for example:
    
    ```
    csr1#guestshell run python /bootflash/scripts/iosxe-portreport.py
    Open Interface Report
    
    
    Loopback2 is down. It was last seen up never
    Loopback3 is down. It was last seen up 2019-05-31 05:37:01.874953
    
    csr1#
    ```

While the interface state tracking may be less than useful on a small virtual router, hopefully this example shows the 
practicality of such a concept when applied in larger environments, such as in a campus switch network.  Take this 
example and extend it with the tools and skills of the Ninja.

---

Navigation :: [Previous Page](LTRPRG-1100-04b1-PortTrack.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04c1-NetAssist.md)
