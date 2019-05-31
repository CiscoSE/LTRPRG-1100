Navigation :: [Previous Page](LTRPRG-1100-04a1-HighCPU.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04b1-PortTrack.md)

---

### Example 1: Troubleshooting High CPU like a Network Programmability Ninja

#### Objectives

The objectives for this exercise are to:

* Create a Python script on-box in Guest Shell to evaluate potential causes for high CPU utilzation
* Leverage Embedded Event Manager to trigger Python script when a high CPU event occurs on a router
* Utilize storage space on the router and Syslog capabilities to create a report and alerts

#### Step 1: Creating a High CPU Troubleshooting Python Script

Once you've identified the information to gather when a CPU spike occurs, it is time to write a Python script that
can collect the data on your behalf. This script will exist in IOS XE Guest Shell environment, where it can be run 
directly from the network device.

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

3. Enter a Guest Shell interactive session with the IOS XE command `guestshell run bash`, for example:
    
    ```
    csr1#guestshell run bash
    [guestshell@guestshell ~]$
    ```

4. There is an example Python script `iosxe-highcpu.py` in this lab's Git repository.  Let's create a directory on 
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
    
    Transfer the example script with the `wget foo` command, for example:
    
    TODO: Update URL to raw file.
    
    ```
    [guestshell@guestshell scripts]$ wget https://raw.githubusercontent.com/curtissmith/LTRPRG-1100/clus19/code/iosxe-porttrack.py?token=AAATPLRSE2ZW5EFPFGP5FF247HOTO
    --2019-05-31 04:15:23--  https://raw.githubusercontent.com/curtissmith/LTRPRG-1100/clus19/code/iosxe-porttrack.py?token=AAATPLRSE2ZW5EFPFGP5FF247HOTO
    Reusing existing connection to [raw.githubusercontent.com]:443.
    HTTP request sent, awaiting response... 200 OK
    Length: 1615 (1.6K) [text/plain]
    Saving to: 'iosxe-porttrack.py'
    
    100%[======================================>] 1,615       --.-K/s   in 0s
    
    2019-05-31 04:15:23 (3.97 MB/s) - 'iosxe-porttrack.py' saved [1615/1615]
    
    [guestshell@guestshell scripts]$
    ```
    
    This Python script uses the IOS XE Python CLI module `cli.execute` function to run IOS XE EXEC mode commands from
    Guest Shell.  This is how we gather our information pertinent to troubleshooting the issue.  The information 
    collected is being organized and written to
    the Guest Shell filesystem, so it can be easily referenced over time.  Also, note that the script generates a 
    syslog message with useful details to aid in analysis.
    
        While you are not expected to be fluent in Python scripting, please read through the comments (signified by a `#`
    in the Python code) and the subsequent lines of code to understand the basics of how this script operates.  You 
    can view [this Python script](foo) in 
    this lab's GitHub repository at `https://github.com/curtissmith/LTRPRG-1100/blob/clus19/code/iosxe-porttrack.py`.
    
    TODO: Update URL to this file.
    
5. Exit out of the Guest Shell Bash CLI session with the `exit` command:
    
    ```
    [guestshell@guestshell scripts]$ exit
    csr1#
    ```

#### Step 2: Using IOS XE Embedded Event Manager to Trigger the High CPU Troubleshooting Python Script

Now that the Python script is on our network device, it must be launched at the appropriate time. IOS XE can utilize a 
feature
called Embedded Event Manager (EEM) to trigger actions based on certain events. One such event that can trigger an EEM
action is a change in an SNMP value, such as the SNMP OID that corresponds to current CPU utilization. EEM can execute a
Python script out of the Guest Shell environment as an action. Therefore, EEM can be used as the tool to ensure that the
Python script can run any time there is a high CPU condition, regardless of whether an administrator is logged in to the
network device or not.

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

3. Enter global configuration mode with the `configure terminal` command, which will be indicated by the `csr1 
(config)#` prompt, for example:
   
    ```
    csr1#configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    csr1(config)#
    ```

4. Run the following IOS XE commands in config mode to configure an EEM applet to create a trigger to run our 
high CPU troubleshooting script automatically:
    
    ```
    event manager applet highcpu authorization bypass
    event snmp oid 1.3.6.1.4.1.9.2.1.56.0 get-type exact entry-op gt entry-val "40" poll-interval 1 maxrun 180 ratelimit 300
    action 0.01 syslog msg "High CPU detected."
    action 0.02 cli command "enable"
    action 0.03 cli command "guestshell run python iosxe-highcpu.py"
    ```
    
    For example:

    ```
    csr1(config)#event manager applet highcpu authorization bypass
    csr1(config-applet)#event snmp oid 1.3.6.1.4.1.9.2.1.56.0 get-type exact entry-op gt entry-val "40" poll-interval 1 maxrun 180 ratelimit 300
    csr1(config-applet)#action 0.01 syslog msg "High CPU detected."
    csr1(config-applet)#action 0.02 cli command "enable"
    csr1(config-applet)#action 0.03 cli command "guestshell run python iosxe-highcpu.py"
    ```
   
    End the global configuration mode session with the `end` command or typing `CTRL-Z`, for example:
    
    ```
    csr1(config)#end
    csr1#
    ```
    
    Note that the `entry-val` parameter specifies the percentage at which to trigger the Python script. In normal
    conditions, 40% may be lower than desired to track a high CPU issue. However, this value is set lower for this lab
    to ensure we can repeatedly generate a high CPU event to test the script for demonstration purposes.

#### Step 3: Simulating a High CPU Event and Observing the Results

TODO: LEFT OFF HERE

In order to complete the lab, it is important to ensure that the CPU monitoring put in place actually works as expected.
However, in a lab environment, it can be difficult to spike the CPU of a router without any peers. As noted previously,
we have graciously set the high CPU threshold at a low level of 40%. Now, we must take the steps to bring the CPU to
this level.

1. Issue a `show proc cpu | include CPU` to see the current utilization. It is likely hovering less than 5% utilized
under normal conditions in this lab.

2. Enter Guest Shell:
    ```
    csr1#guestshell run bash
    [guestshell@guestshell ~]$
    ```

3. Either use wget to download `cpuspike.sh` or use vi to open `cpuspike.sh` and paste in the following:
    ```
    for i in {0..15}; do for j in {1..254}; do echo 10.128.$i.$j; done; done | xargs -I {} -P5000 ping -c1 -W1 -q {}
    ```

    This script will be used to generate a lot of ICMP traffic in a very short period of time.

4. Set this bash script as executable by issuing the command `chmod +x cpuspike.sh`

5. Type `exit` in the guest shell to return to IOS-XE CLI.

6. In order to ensure that CPU spikes on the router, we will use a time-tested method that often inadvertantly causes
CPU issues on routers: enabling debugs. While we want the debugs to run, we do not want them to overrun the logging
buffer on the router. This way, we can still observe other syslogs that could be used for off-box alerting. Enter the
following commands to not only enable debug, but also remove debugs from the router's log buffer:

    ```
    csr1#debug ip packet
    IP packet debugging is on
    csr1#config t
    csr1(config)#logging buffered informational
    csr1(config)#end
    ```

7. Since we will be generating a significant amount of ICMP traffic, we will want to contain it locally on the router.
The easiest way to do this is to create an interface on the router to handle this traffic. We can utilize a loopback
interface to accomplish this:

    ```
    csr1#config t
    csr1(config)#interface loopback1
    csr1(config-if)#ip address 10.128.0.1 255.255.0.0
    csr1(config-if)#no shut
    csr1(config-if)#end
    ```

8. It is time to run the test. Even though the bash script to generate a CPU spike lives in the Guest Shell, it can be
run without leaving the IOS-XE Exec mode. Make sure to disable debugging afterwards as best practice.

    ```
    csr1#guestshell run ./cpuspike.sh
    [output ommitted]
    csr1#undebug all
    ```

    This bash script will generate a significant amount of output, as it is effectively pinging over 4000 hosts in a
    short period of time. This script, paired with the debug enabled, should push the CPU to where it will trigger our
    troubleshooting script.


#### Step 4: Observe Alerts and Saved Results

The expectation is that the actions taken in Step 3 have forced the router CPU to move beyond the threshold to trigger
our high CPU alert. Based on the script, we should expect to see syslog messages in the logging buffer, as well as a new
file in our bootflash containing details of the high CPU incident. While we are set up to view the details of this file
right on the router, this capability becomes more powerful when considering the ability to copy this file to an off-box
location and subsequently use it to attach to a Cisco TAC service request, archive it for historical baselining, or
some other use.

1. First, confirm that the high CPU event was detected by EEM. Issue a `show logging` and look for a log containing
`%HA_EM-6-LOG: highcpu: High CPU detected.` This syslog message signifies that the EEM applet we created has run.

2. Next, we want to make sure that the Python also ran successfully. The Python script also generated a syslog, so look
for a log that starts with: `*May  3 16:54:18.312: %SYS-3-USERLOG_ERR: Message from tty3(user id: ): High CPU detected.
Check /bootflash/highcpulog.txt : Top process:` Note that this log not only alerts us to the high CPU event, but also
tells us where to find the file with details, and also gives us a glimpse at what the busiest process was at the time of
the event.

3. Lastly, we can observe the full details captured by this script. By looking at the text file created, we will find:
    - The time of the high CPU event
    - The percentage of CPU usage at the time of the event
    - The list of all processes running, sorted by the highest CPU utilization
    - Histograms of the CPU usage over time

    ```
    csr1#more bootflash:highcpulog.txt
    [output ommitted]
    ```

This concludes our first exercise. To summarize, we utilized EEM, Guest Shell, and Python to detect, collect
information, and report on high CPU issues, all on-router without any human interaction.

---

Navigation :: [Previous Page](LTRPRG-1100-04a1-HighCPU.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04b1-PortTrack.md)
