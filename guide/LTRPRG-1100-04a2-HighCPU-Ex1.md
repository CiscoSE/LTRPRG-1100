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
    
    Transfer the example script with the `wget https://raw.githubusercontent.com/curtissmith/LTRPRG-1100/master/code/iosxe-highcpu.py` command, for example:
        
    ```
    [guestshell@guestshell scripts]$ wget https://raw.githubusercontent.com/curtissmith/LTRPRG-1100/master/code/iosxe-highcpu.py
    --2019-05-31 19:48:17--  https://raw.githubusercontent.com/curtissmith/LTRPRG-1100/master/code/iosxe-highcpu.py
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.0.133, 151.101.64.133, 151.101.128.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.0.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 656 [text/plain]
    Saving to: 'iosxe-highcpu.py'
    
    100%[======================================>] 656         --.-K/s   in 0s
    
    2019-05-31 19:48:17 (72.9 MB/s) - 'iosxe-highcpu.py' saved [656/656]
    
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
    this lab's GitHub repository at `https://github.com/CiscoSE/LTRPRG-1100/blob/clus19/code/iosxe-porttrack.py`.
    
    TODO: Update URL to this file.
    
5. Exit out of the Guest Shell Bash CLI session with the `exit` command:
    
    ```
    [guestshell@guestshell scripts]$ exit
    csr1#
    ```

#### Step 2: Using IOS XE Embedded Event Manager to Trigger the High CPU Troubleshooting Python Script

Now that the Python script is on our network device, it must be launched at the appropriate time. IOS XE can utilize a 
feature called Embedded Event Manager (EEM) to trigger actions based on certain events. One such event that can 
trigger an EEM action is a change in an SNMP value, such as the SNMP OID that corresponds to current CPU utilization.
EEM can execute a Python script out of the Guest Shell environment as an action. Therefore, EEM can be used as the 
tool to ensure that the Python script can run any time there is a high CPU condition, regardless of whether an 
administrator is logged in to the network device or not.

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

3. Enter global configuration mode, which will be indicated by the `csr1(config)#` prompt, with the
`configure terminal` command, for example:
   
    ```
    csr1#configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    csr1(config)#
    ```

4. Run the following IOS XE commands in config mode to configure an EEM applet to create a trigger to run our high 
CPU troubleshooting script automatically:
    
    ```
    event manager applet highcpu authorization bypass
    event snmp oid 1.3.6.1.4.1.9.2.1.56.0 get-type exact entry-op gt entry-val "40" poll-interval 1 maxrun 180 ratelimit 300
    action 0.01 syslog msg "High CPU detected."
    action 0.02 cli command "enable"
    action 0.03 cli command "guestshell run python /bootflash/scripts/iosxe-highcpu.py"
    ```
    
    For example:

    ```
    csr1(config)#event manager applet highcpu authorization bypass
    csr1(config-applet)#event snmp oid 1.3.6.1.4.1.9.2.1.56.0 get-type exact entry-op gt entry-val "40" poll-interval 1 maxrun 180 ratelimit 300
    csr1(config-applet)#action 0.01 syslog msg "High CPU detected."
    csr1(config-applet)#action 0.02 cli command "enable"
    csr1(config-applet)#action 0.03 cli command "guestshell run python /bootflash/scripts/iosxe-highcpu.py"
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

In order to complete the lab, it is important to ensure that the CPU monitoring put in place actually works as expected.
However, in a lab environment, it can be difficult to spike the CPU of a router without any peers. As noted previously,
we have set the high CPU threshold at a low level of 40% for demonstration purposes. Now, we must take the steps to 
bring the CPU to this level to simulate a real-world scenario in the lab.

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

3. From the IOS XE device CLI, run the `show proc cpu | include CPU` command to see the current utilization, for 
example:
    
    ```
    csr1#show proc cpu | include CPU
    CPU utilization for five seconds: 0%/0%; one minute: 0%; five minutes: 0%
    csr1#
    ```
    
    It is likely to be steady at or less than 5% utilization under normal conditions in this lab.

4. Enter a Guest Shell interactive session with the IOS XE command `guestshell run bash`, for example:
    
    ```
    csr1#guestshell run bash
    [guestshell@guestshell ~]$
    ```

5. There is an example BASH shell script `cpuspike.sh` in this lab's Git repository.  Let's create a directory
on the network device `bootflash:` and transfer the file to the network device file system to be used in the next 
steps.
    
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
    
    Transfer the example script with the `wget https://raw.githubusercontent.com/curtissmith/LTRPRG-1100/master/code/cpuspike.sh` command, for example:
    
    TODO: Update URL to raw file.
    
    ```
    [guestshell@guestshell scripts]$ wget https://raw.githubusercontent.com/curtissmith/LTRPRG-1100/master/code/cpuspike.sh
    --2019-05-31 19:49:44--  https://raw.githubusercontent.com/curtissmith/LTRPRG-1100/master/code/cpuspike.sh
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.192.133, 151.101.0.133, 151.101.64.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.192.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 113 [text/plain]
    Saving to: 'cpuspike.sh'
    
    100%[======================================>] 113         --.-K/s   in 0s
    
    2019-05-31 19:49:44 (16.4 MB/s) - 'cpuspike.sh' saved [113/113]
    
    [guestshell@guestshell scripts]$
    ```
    
    This script will generate a lot of ICMP traffic in a very short period of time for demonstration purposes.

5. Exit out of the Guest Shell Bash CLI session with the `exit` command:
    
    ```
    [guestshell@guestshell scripts]$ exit
    csr1#
    ```

6. In order to ensure that CPU spikes on the router, we will use a time-tested method that often inadvertently causes
CPU issues on routers: enabling debugs. While we want the debugs to run, we do not want them to overrun the logging
buffer on the router. This way, we can still observe other syslog messages that could be used for off-box alerting.
    
    Enter global configuration mode, which will be indicated by the `csr1(config)#` prompt, with the
    `configure terminal` command, for example:
   
    ```
    csr1#configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    csr1(config)#
    ```
    
    Run the `logging buffered informational` command to disable logging debug messages, for example:
    
    ```
    csr1(config)#logging buffered informational
    csr1(config)#
    ```
    
    End the global configuration mode session with the `end` command or typing `CTRL-Z`, for example:
    
    ```
    csr1(config)#end
    csr1#
    ```
    
    Run the `debug ip packet` command to turn on debugging, for example:
    
    ```
    csr1#debug ip packet
    IP packet debugging is on
    csr1#
    ```

7. Since we will be generating a significant amount of ICMP traffic, we will want to contain it locally on the router.
The easiest way to do this is to create an interface on the router to handle this traffic. We can utilize a Loopback
interface to accomplish this.
    
    Enter global configuration mode with the `configure terminal` command, which will be indicated by the `csr1 
    (config)#` prompt, for example:
   
    ```
    csr1#configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    csr1(config)#
    ```
    
    Run the following IOS XE commands in config mode to configure an EEM applet to create a cron entry to run our 
    port tracker script automatically:
    
    ```
    interface Loopback1
      ip address 10.128.0.1 255.255.0.0
      no shutdown
    exit
    ```
    
    For example:
    
    ```
    csr1(config)#interface Loopback1
    csr1(config-if)#ip address 10.128.0.1 255.255.0.0
    csr1(config-if)#no shutdown
    csr1(config-if)#exit
    csr1(config)
    ```
    
    End the global configuration mode session with the `end` command or typing `CTRL-Z`, for example:
    
    ```
    csr1(config)#end
    csr1#
    ```

8. It is time to run the test to simulate high CPU load. We can run the Python test script in Guest Shell from the IOS 
XE device privileged EXEC mode with the `guestshell run bash /bootflash/scripts/cpuspike.sh` command, for 
example (output truncated for brevity):

    ```
    csr1#guestshell run bash /bootflash/scripts/cpuspike.sh
    PING 10.128.0.1 (10.128.0.1) 56(84) bytes of data.
    
    --- 10.128.0.1 ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 0.375/0.375/0.375/0.000 ms
    ```

    This Bash test script will generate a significant amount of output, as it is effectively pinging over 4000 hosts 
    in a short period of time. This script, paired with the debug enabled, should push the CPU to where it will 
    trigger our troubleshooting script.
    
    Don't forget to disable all debugging with the `undebug all` command, for example:
    
    ```
    csr1#undebug all
    All possible debugging has been turned off
    csr1#
    ```

#### Step 4: Observe Alerts and Saved Results

The expectation is that the actions taken in Step 3 have forced the router CPU to move beyond the threshold to trigger
our high CPU alert. Based on the script, we should expect to see syslog messages in the logging buffer, as well as a new
file in our bootflash containing details of the high CPU incident. While we are set up to view the details of this file
right on the router, this capability becomes more powerful when considering the ability to copy this file to an off-box
location and subsequently use it to attach to a Cisco TAC service request, archive it for historical baselining, or
some other use.

1. Confirm that the high CPU event was detected by EEM. Run the `show logging | include HA_EM-6-LOG` command and look
for a syslog message containing the message `%HA_EM-6-LOG: highcpu: High CPU detected`, for example:
    
    ```
    csr1#show logging | include HA_EM-6-LOG
    *May 31 18:24:48.968: %HA_EM-6-LOG: highcpu: High CPU detected.
    csr1#
    ```
    
    This syslog message indicates that the EEM applet we created was triggered.

2. Confirm that the Python script was successfully run by EEM. The Python script also generates a syslog message.  
Run the `show logging | include SYS-3-USERLOG_ERR` command look for a syslog message containing text similar to 
`%SYS-3-USERLOG_ERR: Message from tty2(user id: cisco): High CPU detected.`, for example:
    
    ```
    csr1#show logging | include SYS-3-USERLOG_ERR
    *May 31 18:24:53.103: %SYS-3-USERLOG_ERR: Message from tty3(user id: ): High CPU detected. Check /bootflash/highcpulog.txt : Top process: IOSXE-RP Punt Se
    csr1#
    ```
    
    Note that this log not only alerts us to the high CPU event, but it also tells us where to find the file with 
    details and gives us a glimpse at what the busiest process was at the time of the event.

3. Observe the full details captured by this Python script. By looking at the text file created, we will find:
    
    * The time of the high CPU event
    * The percentage of CPU usage at the time of the event
    * The list of all processes running, sorted by the highest CPU utilization
    * Histograms of the CPU usage over time
    
    View the contents of the log file created by the Python script with the `more bootflash:highcpulog.txt` command, 
    for example (output truncated for brevity):

    ```
    csr1#more bootflash:highcpulog.txt
    High CPU at *18:24:50.972 UTC Fri May 31 2019
    
    CPU and top ten processes:
    
    CPU utilization for five seconds: 44%/7%; one minute: 7%; five minutes: 3%
     PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process
     123       16263       73015        222 26.65%  4.07%  1.58%   0 IOSXE-RP Punt Se
     400        5140       31381        163  7.76%  1.34%  0.52%   1 SSH Process    
     489         566       27409         20  1.20%  0.18%  0.04%   0 EEM ED Syslog  
      78        4029       53342         75  0.71%  0.38%  0.18%   0 TTY Background 
      77          80        4423         18  0.15%  0.02%  0.00%   0 Logger         
      41        1020       55667         18  0.07%  0.00%  0.00%   0 ARP Background 
     205       29507     1661790         17  0.07%  0.03%  0.04%   0 IP ARP Retry Age
     419       23838      833514         28  0.07%  0.02%  0.01%   0 MMA DB TIMER   
       8           0           1          0  0.00%  0.00%  0.00%   0 RO Notify Timers
     --More--
    ```
    
    Press the `Space` keyboard button to page through the contents of the file or type `q` to exit and return to the 
    `csr1#` prompt.

This concludes our first exercise. To summarize, we utilized EEM, Guest Shell, and Python to detect, collect
information, and report on high CPU issues, all on-router without any human interaction.  We had to perform a bit of 
configuration to create a test scenario to simulate a real-world use case, but this can be easilly deployed when and 
where necessary to aid in troubleshooting a common issue like a Network Programmability Ninja.

---

Navigation :: [Previous Page](LTRPRG-1100-04a1-HighCPU.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04b1-PortTrack.md)
