## Guest Shell

TODO:

- [ ] @curtissmith Draft "Hone Your Ninja Skills - Guest Shell"

A powerful software feature called Guest Shell has been brought to products running Cisco IOS XE.  Originally 
exclusively available on Nexus switching products running NX-OS, Guest Shell is now availabe on the Catalyst, ISR, 
and CSR product families.

Guest Shell is a virtualized Linux-based environment running on the network device, designed to run standard and custom 
Linux applications, including Python, for automated management of Cisco devices.  Guest Shell provides a secure 
environment, decoupled from the host network device, in which you can install and run scripts or software packages.

### On-box vs. Off-box Network Programmability

So far in this lab, we have been focussing on so-called off-box network programmability.  That is to say, we've been 
running applications on a workstation and interfacing with network devices.  The applications reside on a workstation
and connect to a network device.  With on-box network programmability, we have the ability to host and run 
applications directly on the network device itself.  Guest Shell makes this very easy, but with Application Hosting, 
entire Linux Containers (LXCs) can be installed for custom, purpose-built applications as well on platforms that 
support it.  This lab will focus on Guest Shell for script and utility hosting on IOS XE.

Here is a brief reference for the platforms that support Guest Shell today:

| Feature | Guest Shell 1.0 (Lite) | Guest Shell 1.0 | Guest Shell 2.1 |
| --- | --- | --- | --- |
| Operating System | IOS XE 16.5.1a | IOS 16.5 | NX-OS 7.x |
| Platform | Catalyst 3650/3850 | Catalyst 9000, ISR 4000 | Nexus 3000, 9000 |
| Foo | bar | bar | bar |

### Exercise 1: Unleashing Network Programmability at the Edge with IOS XE

#### Objectives

The objectives for this exercise are to:

* Learn how to configure and access Guest Shell on IOS XE
* Learn how to install and run applications in Guest Shell on IOS XE
* Learn how to access the IOS XE CLI from Guest Shell 

#### Step 1: Enabling Guest Shell on IOS XE

1. Establish an SSH connection to the IOS XE device.
2. From the IOS XE device CLI, enter privileged EXEC mode, for example:
    ```
    csr1kv>enable
    csr1kv#
    ```
3. Enter confugure mode, for example:
    ```
    csr1kv# configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    csr1kv(config)#
    ```
4. IOx is a prerequisite for Guest Shell, so we need to turn on IOx, for example:
    ```
    csr1kv#iox
    csr1kv#end
    ```
 5. It can take a few minutes for the IOx subsystem and process to start.  Before continuing on, check to ensure 
 IOx is running with the `show iox-service` command, for example:
    ```
    csr1kv#show iox-service 
    Virtual Service Global State and Virtualization Limits:
    
    Infrastructure version : 1.7
    Total virtual services installed : 0
    Total virtual services activated : 0
    
    Machine types supported   : LXC
    Machine types disabled    : KVM
    
    Maximum VCPUs per virtual service : 0
    Resource virtualization limits:
    Name                         Quota     Committed     Available  
    --------------------------------------------------------------
    system CPU (%)                   7             0             7  
    memory (MB)                   1024             0          1024  
    bootflash (MB)               20000             0          6715  
    
    
    IOx Infrastructure Summary:
    ---------------------------
    IOx service (CAF)    : Running 
    IOx service (HA)     : Not Running 
    IOx service (IOxman) : Running 
    Libvirtd             : Running 
    
    csr1kv#

    ```
    
    Once you've verified the `IOx service (CAF)`, `IOx service (IOxman)`, and `Libvirtd` services are in the 
    `Running` state, continue to the next step.
6. Enabling Guest Shell requires a bit of configuration first.  We must:
    * Configure a Virtual Port Group - The Virtual Port Group is the interface the IOS XE network device uses to 
        communicate with guest shell.
    * Configure Network Address Translation - The IOS XE network device provides access to off-box resources through 
        NAT.
    1. A Virtual Port Group is only required on ISR and CSR IOS XE routing platforms.  On Catalyst IOS XE switching 
    platforms, Guest Shell connectivity is bridged from the `Mgmt0` <cjs - need to validate interfance name> management 
    interface.  Create and configure a Virtual Port Group, for example:
        ```
        csr1kv#configure terminal 
        Enter configuration commands, one per line.  End with CNTL/Z.
        csr1kv(config)#inter
        csr1kv(config)#interface VirtualPortGroup 0
        csr1kv(config-if)#ip address 192.168.35.1 255.255.255.0
        csr1kv(config-if)#no shutdown 
        csr1kv(config-if)#exit
        csr1kv(config)#

        ```
    2. Configure Network Address Translation (required on all routing and switching platforms), for example:
        ```
        csr1kv(config)#interface VirtualPortGroup 0
        csr1kv(config-if)#ip nat inside
        csr1kv(config-if)#interface GigabitEthernet 1
        csr1kv(config-if)#ip nat outside
        csr1kv(config-if)#exit
        csr1kv(config)#ip access-list standard NAT_ACL
        csr1kv(config-std-nacl)#permit 192.168.0.0 0.0.255.255
        csr1kv(config-std-nacl)#exit
        csr1kv(config)#ip nat inside source list NAT_ACL interface GigabitEthernet1 overload
        csr1kv(config)#
        ```
7.  To enable Guest Shell itself, first run the following commands in config mode:
    ```
    csr1kv(config)#app-hosting appid guestshell
    csr1kv(config-app-hosting)#vnic gateway1 virtualportgroup 0 guest-interface 0 guest-ipaddress 192.168.35.2 netmask 255.255.255.0 gateway 192.168.35.1 name-server 8.8.8.8 default
    csr1kv(config-app-hosting)#resource profile custom cpu 1500 memory 512
    csr1kv(config-app-hosting)#
    ```
    
    Exit from config mode, and run the `guestshell enable` command in EXEC mode:
    
    ```
    csr1kv(config-app-hosting)#end
    csr1kv#guestshell enable
    Interface will be selected if configured in app-hosting
    Please wait for completion
    guestshell activated successfully
    Current state is: ACTIVATED
    guestshell started successfully
    Current state is: RUNNING
    Guestshell enabled successfully
    
    csr1kv#
    ```
    
    You can confirm Guest Shell is enabled and active with the `show app-hosting list` command, for example:
    
    ```
    csr1kv#show app-hosting list
    App id                           State
    ------------------------------------------------------
    guestshell                       RUNNING
    
    csr1kv#
    ```
    
    Confirm the `VirtualPortGroup0` interface is present and configured with the `show ip interface brief` command, for 
    example:
    
    ``` 
    csr1kv#show ip interface brief
    Interface              IP-Address      OK? Method Status                Protocol
    GigabitEthernet1       10.0.2.15       YES DHCP   up                    up      
    VirtualPortGroup0      192.168.35.1    YES manual up                    up      
    csr1kv#
    ```
    
    Test to confirm the Guest Shell vnic is active and reachable with the `ping` command, for exaple:
    
    ```
    csr1kv#ping 192.168.35.2
    Type escape sequence to abort.
    Sending 5, 100-byte ICMP Echos to 192.168.35.2, timeout is 2 seconds:
    !!!!!
    Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
    csr1kv#
    ```

#### Step 2: Installing and Running Applications On-Box with Guest Shell on IOS XE

lorem ipsum

### Step 3: Accessing the IOS XE CLI from Guest Shell

lorem ipsum
