Navigation - [Previous Page](LTRDEV-1100-03b-NETCONF-Ex3.md)

---

## Guest Shell

## Introducing Guest Shell

A powerful software feature called Guest Shell has been brought to products running Cisco IOS XE.  Originally 
exclusively available only on Nexus switching products running NX-OS, Guest Shell is now available on the Catalyst, 
ISR, and CSR products running IOS XE.

Guest Shell is a virtualized Linux-based environment running on the network device, designed to run standard and custom 
Linux applications, including Python, for automated management of Cisco devices.  Guest Shell provides a secure 
environment, decoupled from the host network device, in which you can install and run scripts or software packages, 
while maintaining a fault and resource isolation from IOS XE.

### On-box vs. Off-box Network Programmability

So far in this lab, you have been focusing on so-called off-box network programmability.  That is to say, you've been 
running applications on a workstation and interfacing with network devices.  The applications reside on a workstation
and connect to a network device.  With on-box network programmability, you have the ability to host and run 
applications directly on the network device itself.

Off-Box network programmability is ideal for:

* configuration management and automation
* telemetry and operational data
* SDN controller functionality, e.g. Cisco DNA Center

On-Box network programmability is ideal for:

* network device provisioning automation
* IOS XE Embedded Event Manager (EEM) response automation
* edge compute for network applications and Internet of Things (IoT)

Guest Shell facilitates on-box network programmability, but with Application Hosting, Linux Containers (LXCs) can be 
installed for custom, purpose-built applications as well on network device platforms that support it.  This lab will 
focus on Guest Shell for script and utility hosting on IOS XE.

Here is a brief reference for the platforms that support Guest Shell today:

| Feature | Guest Shell 1.0 (Lite) | Guest Shell 1.0 | Guest Shell 2.1 |
| --- | --- | --- | --- |
| Operating System | IOS XE 16.5.1a | IOS 16.5 | NX-OS 7.x |
| Platform | Catalyst 3650/3850 | Catalyst 9000, ISR 4000 | Nexus 3000, 9000 |
| Guest Shell Environment | MontaVista CGE7 | CentOS 7 | CentOS 7 |
| Python | v2.7 | v2.7, v3.0 | v2.7, v3.0 |
| RPM Install | No | Yes | Yes |

---

Navigation - [Next Page](LTRDEV-1100-03c-GuestShell-Ex1.md)
