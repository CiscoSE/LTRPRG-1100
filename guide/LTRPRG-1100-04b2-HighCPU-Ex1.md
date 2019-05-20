### Example 1: Detect and Report on CPU Spikes

#### Objectives

The objectives for this exercise are to:

* Create a Python script on-box in Guest Shell to evaluate potential causes for high CPU
* Leverage Embedded Event Manager to trigger Python script when a high CPU event occurs on a router
* Utilize storage space on the router and Syslog capabilities to create a report and alert about it

#### Step 1: Determine what to collect

One glaring problem with troubleshooting fleeting high-CPU issues on a router, is that often by the time an
administrator logs in to troubleshoot, the issue has passed. The goal of this exercise is to utilize skills of the
network programmability ninja to react to a CPU spike immediately, without waiting for a person to log in to the router.
The actions taken can be as simple as information collection, to as intricate as executing configuration changes based
on real-time traffic observed. For this exercise, we will be collecting what is often pertinent information to help
identify the culprit of a high-CPU event.

In order to effectively triage an event for high CPU utilization, first it is important to understand what information
is pertinent to triage the situation. 

1. Recording the CPU utilization not only helps to understand the usage in 5 sec, 1 min, 5 min intervals, but also
provides an understanding of whether the CPU has high interrupt usage. This can be gathered from a `# show proc cpu
sorted` output.

2. The same command above also lists the processes and their CPU usage, sorted to start with the heaviest load. This
can be indicative of what is causing high CPU, as it may be tied up under a single process.

3. Visualizing the CPU utilization over a time period can also be helpful to understand if this is an
anomalous spike, or just slightly above normal operating thresholds. It can also help to show if there is a pattern to
when a spike repeats.

3. Sometimes high CPU can be attributed to something a particular user or administrator is doing, so gathering the
active users on the router is also helpful to understand the full picture.

While there are surely other pieces of information that can be helpful, this is a great starting point.

#### Step 2: Create Python script to collect data

Now that you've identified the information to gather when a CPU spike occurs, it is time to write a Python script that
can collect the data on your behalf. This script will exist in the IOS-XE Guest Shell environment, where it can be run
directly from the router.

1. From the command line interface of the router, launch `bash` from the Guest Shell:
    ```
    csr1#guestshell run bash
    [guestshell@guestshell ~]$
    ```

2. wget the python script from github or use vi to open iosxe-highcpu.py and paste in the following contents:
    ```
    import cli
    
    timestamp = cli.execute("show clock")
    processes = cli.execute("show proc cpu sort")
    histogram = cli.execute("show proc cpu hist")
    users = cli.execute("show users")
    
    fp = open('/bootflash/highcpulog.txt','w')
    fp.write("High CPU at "+timestamp+"\n\n")
    
    processlines = processes.splitlines()
    fp.write("CPU and top ten processes:\n\n")
    for x in range(0,12):
        fp.write(processlines[x]+"\n")
    fp.write("CPU histogram:\n\n")
    fp.write(histogram+"\n\n")
    fp.write("Active users:\n\n")
    fp.write(users+"\n\n")
    fp.close()
    
    topproc = processlines[2][65:]
    cli.execute("send log 3 High CPU detected. Check /bootflash/highcpulog.txt : Top process: "+topproc)
    ```

    Note that the `cli.execute` function is used to run IOS commands, so this is the basis of the information gathering.
    Also, the information collected is being organized and written to a file in bootflash, so it can be easily viewed
    later. Also, note that the script generate a syslog message with details.

#### Step 3: Setup IOS XE Embedded Event Manager to Launch Python Script

Now that the Python script is created, it must be launched at the appropriate time. IOS-XE can utilize a feature
called Embedded Event Manager (EEM) to initiate actions based on certain events. One such event that can trigger an EEM
action is changing on an SNMP value, such as the OID that corresponds to current CPU utilization. EEM can execute a
Python script out of the Guest Shell environment as an action. Therefore, EEM can be used as the tool to ensure that the
Python script can run any time there is a high-CPU condition, regardless of whether an administrator is logged in to the
router.

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
    csr1(config)#event manager applet highcpu authorization bypass
    csr1(config-applet)#event snmp oid 1.3.6.1.4.1.9.2.1.56.0 get-type exact entry-op gt entry-val "40" poll-interval 1 maxrun 180 ratelimit 300
    csr1(config-applet)#action 0.01 syslog msg "High CPU detected."
    csr1(config-applet)#action 0.02 cli command "enable"
    csr1(config-applet)#action 0.03 cli command "guestshell run python iosxe-highcpu.py"
    csr1(config-applet)#end

    ```

    Note that the `entry-val` parameter specifies the percentage at which to trigger the Python script. In normal
    conditions, 40% may be lower than desired to track a high CPU issue. However, this value is set lower for this lab
    to ensure we can repeatedly generate a high CPU event to test the script.

#### Step 3: Force a High CPU Event and Observe Results

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
