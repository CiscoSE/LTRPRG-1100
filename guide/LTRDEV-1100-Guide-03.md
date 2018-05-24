# Hone Your Ninja Skills

## Using APIs

TODO:

- [ ] @mgalazka Draft "Hone Your Ninja Skills - Using APIs"

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pharetra risus a fringilla hendrerit. Nam venenatis 
metus quis risus aliquam mattis. Ut vitae elementum libero. Nam malesuada felis in tincidunt luctus. Aliquam ut magna
orci. Nulla a elementum erat. Aenean facilisis, nibh at blandit feugiat, odio est tincidunt sem, eu pretium sem 
lorem vel libero. Nullam felis nisl, eleifend interdum congue aliquam, dictum sit amet augue. Maecenas vel augue 
justo. Quisque scelerisque tempus sapien, eu elementum nibh venenatis ac. In vel purus eu arcu elementum volutpat.

## Using NETCONF/YANG

TODO:

- [x] @curtissmith Draft "Hone Your Ninja Skills - Using NETCONF/YANG"
- [ ] Proofread
- [ ] Edit for directory, example output, and style consistency

### Introducing Model Driven Programmability

Traditional network device management techniques, for example command line interface (CLI) and web user interface 
(UI), were designed for human to machine interaction for configuring and accessing operational details.  They by 
definition are not programmable.  Although attempts at automation through screen scraping or imitating interactive 
sessions are possible, they are error prone, unrealiable, and do not scale.

The need for reliable and scalable ways to manage network devices is not a new one.  Simple Network Management Protocol 
(SNMP) was first introduced as a IETF Internet Standard in 1988 as a standard interface configure and retrieve 
operational information from network devices.  SNMP was revised over the years, chiefly to improve performance and 
security of the protocol.  However, SNMP still isn't adequate for the job today, relegated to polling statistics and 
status.

In 2003, the IETF published [RFC3535](https://tools.ietf.org/html/rfc3535) *Overview of the 2002 IAB Network 
Management Workshop*, stating

> SNMP works reasonably well for device monitoring.

and found to be lacking in the following ways:

* Applications are necessary for SNMP to useful
* Lack of writeable MIBs in general and writeable MIBs for configuration more specifically
* Does not scale
* Too difficult to implement
* Lack of support for configuration retrieval or playback
* Mismatch between SNMP data-centric view of the world versus an operator's task-oriented view of the world 

The solution lies in using data models - a programmatic and standards-based way of describing writing configurations 
to any network device. Use model driven programmability to replace the process of manual configuration.  Model driven
programmability inherits the power of models, making it easier to configure routers.  It overcomes drawbacks posed by 
traditional network device management techniques.

```
           +----------------+  +----------------+  +----------------+  Model Driven      ^
     Apps  |   App1         |  |   App2         |  |   App3         |  Configuration     |
           +----------------+  +----------------+  +----------------+       +            |
                                                                            |            |
           +--------------------------------------------------------+       |            |
     APIs  |                   Model Driven APIs                    |       |            |
           +--------------------------------------------------------+       |            |
                                                                            |            |
           +----------------+  +----------------+  +----------------+       |            |
 Protocol  |    NETCONF     |  |    RESTCONF    |  |      gRPC      |       |            |
           +----------------+  +----------------+  +----------------+       |            |
                                                                            |            |
           +-------------------------+  +-----------------+  +------+       |            |
 Encoding  |           XML           |  |      JSON       |  |  GPB |       |            |
           +-------------------------+  +-----------------+  +------+       |            |
                                                                            |            |
           +----------------+  +------------------------------------+       |            |
Transport  |      SSH       |  |              HTTPS                 |       |            |
           +----------------+  +------------------------------------+       |            |
                                                                            |            |
           +--------------------------------------------------------+       |            +
   Models  |                    YANG Data Models                    |       |       Model Driven
           +--------------------------------------------------------+       v        Telemetry
```

To this end, the IETF went to work and created a few new Internet standards to help address these shortcomings and 
move to model driven programmability: NETCONF and YANG.

### Exercise 1: Introducing YANG

#### Objectives

The objectives for this exercise are to:

* Understand YANG as a language, data models, and data
* Explore the anatomy of a YANG data model
* Use pyang to explore data models

YANG (Yet Another Next Generation) was developed by the IETF NETMOD (Network Modeling) Working Group and published as
[RFC 6020](https://tools.ietf.org/html/rfc6020) in 2010.  YANG has become the de facto data modeling language.  But 
YANG is more than just a modeling language.  It is also the data models and the data itself.  When we talk about YANG, 
depending on the context, we mean YANG as a language, YANG as a data model, and YANG data.

![What is YANG](assets/YANG.png)

##### Understanding YANG as a Language

YANG is a modular and structured language that represents, or describes, data models in an XML tree format.  The YANG
modeling language is protocol independent and can be converted into any encoding format such as XML or JSON - more 
on that later in this lab.  You and I may speak English; YANG is the way that our programs can speak to our network 
devices without confusion or interpretation.  Here is a brief example of the YANG modeling language:

```
module ietf-interfaces {
    import ietf-yang-types {
        prefix yang;
    }
    container interfaces {
        list interface {
            key "name";
            leaf name {
            type string;
        }
        leaf enabled {
            type boolean;
            default "true";
    }
}
```

##### Understanding YANG as a Model

A data model does nothing more than describe or represent data.  This is a way to agree how to describe something, 
for example a person:

* Person
    * Gender, e.g. male or female
    * Height, e.g. feet and inches or meters
    * Weight, e.g. pounds or kilograms
    * Eye Color, e.g. blue, green, brown, or hazel
    * Hair Color, e.g. blond, brown, or black
    
Even with a generic data model such as this simple example, we can describe a person in a manner that is easily 
understood.  Although YANG data models could be used to describe anything, they were developed to describe network 
devices and the services we build with those devices.

A YANG data model might describe a network device data or network service data.  Some examples of each include:

* Device Data Model
    * Interface
    * VLAN
    * EIGRP
    
* Service Data Model
    * L3 MPLS VPN
    * VRF
    * System Management
    
For the purposes of getting started with model driven programmability, it is easier to focus on device data models. 

YANG data models can be written by anyone, but the most frequently used models come from the IETF in the form of 
Internet standards or from [OpenConfig](http://www.openconfig.net/) in the form of community and industry developed 
vendor neutral models.  Vendors also write vendor and product specific data models for their products and services.

##### Understanding YANG Data

Don't confuse the data model, the data format, and the data itself.  Consider the following three examples:

1. Text -
    
    ```
    switch# show int bri
    
    --------------------------------------------------------------------------------
    Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port
    Interface                                                                    Ch #
    --------------------------------------------------------------------------------
    Eth1/1        1       eth  fabric down    SFP not inserted            10G(D) --
    ```
    
 2. XML -
    
    ```
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <nf:rpc-reply xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://www.cisco.com/nxos:1.0:if_manager">
     <nf:data>
      <show>
       <interface>
        <__XML__INTF_ifeth_brf>
         <__XML__PARAM_value>
          <__XML__INTF_output>Ethernet1/1-3</__XML__INTF_output>
         </__XML__PARAM_value>
         <__XML__OPT_Cmd_show_interface_if_eth_brief___readonly__>
          <__readonly__>
           <TABLE_interface>
            <ROW_interface>
             <interface>Ethernet1/1</interface>
             <vlan>1</vlan>
             <type>eth</type>
             <portmode>fabric</portmode>
             <state>down</state>
             <state_rsn_desc>SFP not inserted</state_rsn_desc>
             <speed>10G</speed>
             <ratemode>D</ratemode>
            </ROW_interface>
           </TABLE_interface>
          </__readonly__>
         </__XML__OPT_Cmd_show_interface_if_eth_brief___readonly__>
        </__XML__INTF_ifeth_brf>
       </interface>
      </show>
     </nf:data>
    </nf:rpc-reply>
    ]]>]]>
    ```
    
3. JSON - 
    
    ```
    {
        "interfaces": [
            {
                "interface": "Ethernet1/1", 
                "vlan": "1", 
                "type": "eth", 
                "portmode": "fabric", 
                "state": "down", 
                "state_rsn_desc": "SFP not inserted", 
                "speed": "10G", 
                "ratemode": "D"
            }    
        ]
    }
    ```

Each of these represent the exact same data, displayed in three different common formats: human-readable text, XML, 
and JSON.  Because the YANG data is described as a YANG data model in a structured manner using the YANG language, we
can programmatically display the data in any format that suits our need.

#### Step 1: Exploring the Anatomy of a YANG Data Model

The YANG modeling language is used to build YANG data models using a standard syntax.  There are several 
important constructs used in YANG.

1. Every YANG data model contains a `module` which contains the name of the model, describes the data, and 
documents the revision history of the model itself.
2. YANG defines four types of nodes for data modeling:
    * A `leaf` node contains a single, simple value like an integer or string, for example:
        ```
        leaf host-name {
           type string;
           description "Hostname for this system";
       }
       ```
    * A `leaf-list` node is a sequence of one or more `leaf` nodes, for example:
        ```
        leaf-list domain-search {
         type string;
         description "List of domain names to search";
        }
        ```
    * A `list` node is a sequence of  entries identified by a key value of each key leaf.  A `list` node
    can contain `leaf`, `leaf-list`, `list`, or `container` nodes.  For example,
        ```
        list user {
            key "name";
            leaf name {
                type string;
            }
            leaf full-name {
                type string;
            }
            leaf class {
                type string;
            }
        }
        ```
    * A `container` node is a group of related nodes as child nodes and no value itself.  There is no
     limit to the number of child nodes within a `container` node.  A `container` node can include `leaf`, 
     `leaf-list`, `list`, or other `container` child nodes.  For example,
        ```
        container system {
            container login {
                leaf message {
                    type string;
                    description
                        "Message given at start of login session";
                }
            }
        }
        ```

#### Step 2: Using pyang to Explore YANG Data Models

Now that we have a basic understanding of a YANG data model, let's take a look at an actual model.  You can obtain 
the IETF and OpenConfig YANG data models from GitHub.

1. Create a working directory and clone the IETF YANG repository:
    
    ```
    $ mkdir ~/coding/ciscolive/ietf
    $ cd ~/coding/ciscolive/ietf
    $ git clone https://github.com/YangModels/yang
    Cloning into 'yang'...
    remote: Counting objects: 13445, done.
    remote: Compressing objects: 100% (187/187), done.
    remote: Total 13445 (delta 353), reused 529 (delta 353), pack-reused 12905
    Receiving objects: 100% (13445/13445), 23.11 MiB | 581.00 KiB/s, done.
    Resolving deltas: 100% (9076/9076), done.
    $
    ```
2. Open PyCharm and the IETF YANG Git repository you just cloned by clicking the `File` menu, click `Open...`, 
navigate to the directory `ietf`, and click the `Open` button.
    
    In PyCharm, navigate through the project explorer to find a YANG data model, for example click to expand 
    `standard`, `ietf`, and `RFC`.  Double click to open `ietf-interfaces.yang`.
    
    As you scroll through this file representing the `module ietf-interface` data model, you will find the 
    elements we discussed earlier in this lab.  You can see the structure and nodes.  Each node should be documented 
    with a description.  You can get a sense for what operational state and configuration details you this YANG data 
    model describes.
    
3. I think we can agree browsing a directory full of files written in the YANG modeling language can get tedious.  A 
data format that is good for programming is not necessarily good for human readability.  Fortunately, we have a tool
that can help you called [pyang](https://github.com/mbj4668/pyang) that is a quick `pip install` away.
    
    From the command line terminal, ensure that pyang is installed:
    ```
    $ pip3 install pyang
    ```
    
    Now navigate to the directory that contains the `ietf-interfaces.yang` YANG data model file, for example:
    
    ```
    $ cd ~/coding/ciscolive/ietf/yang/standard/ietf/RFC
    ```
    
    Use pyang to display the data model in a human readable tree format:
    
    ```
    $ pyang -f tree ietf-interfaces.yang
    module: ietf-interfaces
    +--rw interfaces
    |  +--rw interface* [name]
    |     +--rw name                        string
    |     +--rw description?                string
    |     +--rw type                        identityref
    |     +--rw enabled?                    boolean
    |     +--rw link-up-down-trap-enable?   enumeration {if-mib}?
    |     +--ro admin-status                enumeration {if-mib}?
    |     +--ro oper-status                 enumeration
    |     +--ro last-change?                yang:date-and-time
    |     +--ro if-index                    int32 {if-mib}?
    |     +--ro phys-address?               yang:phys-address
    |     +--ro higher-layer-if*            interface-ref
    |     +--ro lower-layer-if*             interface-ref
    |     +--ro speed?                      yang:gauge64
    |     +--ro statistics
    |        +--ro discontinuity-time    yang:date-and-time
    |        +--ro in-octets?            yang:counter64
    |        +--ro in-unicast-pkts?      yang:counter64
    |        +--ro in-broadcast-pkts?    yang:counter64
    |        +--ro in-multicast-pkts?    yang:counter64
    |        +--ro in-discards?          yang:counter32
    |        +--ro in-errors?            yang:counter32
    |        +--ro in-unknown-protos?    yang:counter32
    |        +--ro out-octets?           yang:counter64
    |        +--ro out-unicast-pkts?     yang:counter64
    |        +--ro out-broadcast-pkts?   yang:counter64
    |        +--ro out-multicast-pkts?   yang:counter64
    |        +--ro out-discards?         yang:counter32
    |        +--ro out-errors?           yang:counter32
    x--ro interfaces-state
         x--ro interface* [name]
            x--ro name               string
            x--ro type               identityref
            x--ro admin-status       enumeration {if-mib}?
            x--ro oper-status        enumeration
            x--ro last-change?       yang:date-and-time
            x--ro if-index           int32 {if-mib}?
            x--ro phys-address?      yang:phys-address
            x--ro higher-layer-if*   interface-state-ref
            x--ro lower-layer-if*    interface-state-ref
            x--ro speed?             yang:gauge64
            x--ro statistics
               x--ro discontinuity-time    yang:date-and-time
               x--ro in-octets?            yang:counter64
               x--ro in-unicast-pkts?      yang:counter64
               x--ro in-broadcast-pkts?    yang:counter64
               x--ro in-multicast-pkts?    yang:counter64
               x--ro in-discards?          yang:counter32
               x--ro in-errors?            yang:counter32
               x--ro in-unknown-protos?    yang:counter32
               x--ro out-octets?           yang:counter64
               x--ro out-unicast-pkts?     yang:counter64
               x--ro out-broadcast-pkts?   yang:counter64
               x--ro out-multicast-pkts?   yang:counter64
               x--ro out-discards?         yang:counter32
               x--ro out-errors?           yang:counter32
    $
    ```
    
    The first thing you should notice is how much easier this is to read and understand.
    
    The line `module: ietf-interfaces` contains the module name.
    
    The line beginning `+--rw interfaces` is a container node, which contains a list node:
    
    The line beginning `|  +--rw interface* [name]` is a list node with the key `[name]`, which contains several leaf
    nodes.  For example, the line `+--rw description?                string` is a leaf node that describes a string
    value.  You can see the data model itself is very detailed and well structured but difficult to read if you're 
    looking for pertinent data for your application.  With the use of pyang, on the other hand, you are given just 
    the right amount of information needed to find the data you need for your application.
            
    The `ro` or `rw` next to the node name indicates whether the data is non-configuration data (`ro`) or 
    configuration data (`rw`).  A `?` after the node name indicates that the data is optional and may not be 
    present on the network device.  A `*` after the node name indicates that the node is a leaf or leaf-list.
    For more information about the symbols and conventions used by pyang in the tree format, use the command 
    `pyang --tree-help`.
            
    The second thing that you should notice is the lack of data. Remember, we are only viewing the YANG data 
    model, not YANG data from a network device. We will explore actual YANG data from an IOS XE device later in 
    this lab after we introduce NETCONF.

### Exercise 2: Introducing NETCONF

#### Objectives

The objectives for this exercise are to:

* Understand the NETCONF protocol stack
* Understand NETCONF operations
* Learn how to use Python to make NETCONF requests

NETCONF (Network Configuration) was originally developed and published as
[RFC 4741](https://tools.ietf.org/html/rfc4741) in 2006 and revised as
[RFC 6241](https://tools.ietf.org/html/rfc6241) in 2011.  NETCONF has become the de facto network management protocol
for model driven programmability.  The protocol defines a simple mechanism for managing a network device, retrieving 
configuration data from a network device, uploading new configuration data to a network device, and manipulating 
configuration data on a network device.

NETCONF does not define the data, that is the job of YANG.  NETCONF defines the mechanism for communicating with a 
network device.

#### Step 1: Understanding the NETCONF Protocol Stack

The NETCONF network management protocol is a client-server model using remote precudure call (RPC) over a secure 
connection-oriented session.  The client sends the RPC encoded in XML, and the server replies with a respone encoded 
in XML.  The client RPC and server response are typically YANG data models and YANG data, encoded in an XML data 
format.  The most common transport protocol used to secure NETCONF connections is typically SSH.  The NETCONF 
protocol stack and relationship to SSH and YANG can be represented as follows:

```
 +-----------------------------------------------------------------------------------+
 | +--------------+  +--------------------+  +---------------------------+           |
 | |              |  |   Configuration/   |  |                           |           |
 | |   Content    |  |    Operational     |  |        YANG Data          |           |
 | |              |  |       Data         |  |                           |           |
 | +------+-------+  +---------+----------+  +------------+--------------+           |
 |        |                    |                          |                          |
 | +------+-------+  +---------+----------+  +------------+--------------+           |
 | |              |  |                    |  |    <get>, <get-config>,   |           |
 | |  Operations  |  |  Actions to Take   |  |     <edit-config>, etc    |    XML    |
 | |              |  |                    |  |                           |           |
 | +------+-------+  +---------+----------+  +------------+--------------+           |
 |        |                    |                          |                          |
 | +------+-------+  +---------+----------+  +------------+--------------+           |
 | |              |  |  Remote Procedure  |  |                           |           |
 | |   Messages   |  |     Call (RCP)     |  |    <rpc>, <rpc-reply>     |           |
 | |              |  |                    |  |                           |           |
 | +------+-------+  +---------+----------+  +------------+--------------+           |
 +--------|--------------------|--------------------------|--------------------------+
          |                    |                          |
   +------+-------+  +---------+----------+  +------------+---------------+
   |              |  |                    |  |                            |
   |  Transport   |  |      TCP/IP        |  |           SSH              |
   |              |  |                    |  |                            |
   +--------------+  +--------------------+  +----------------------------+
```

* Transport Layer - NETCONF uses is a secure TCP/IP transport protocol, for example SSH as detailed in
    [RFC 6242] (https://tools.ietf.org/html/rfc6242).
* Messages Layer - NETCONF encodes all communication in XML sent with remote procedure call (RPC).
* Operations Layer - NETCONF messages are sent as operations, which are specific actions to take.  NETCONF operations
    will be covered in more detail later in this lab.
* Content Layer -  This is the configruation and operational data from the network device, YANG data, to be exact.

In the NETCONF protocol, the client is referred to as the `manager` and the server is referred to as the `agent`.  
The manager is you, or your workstation or network management system.  The agent is the network device you manage.  
Here is another way to visually represent the NETCONF protocol stack and client-server relationship of the NETCONF 
manager and agent:

```
                     +-------------------------------------+
                     |     +------------------------------+|
 +--------------+    |     |         +------------------+ ||    +--------------+
 |              |    |     |         |     +-----------+| ||    |              |
 |   Manager    <----> SSH | NETCONF | XML | YANG Data || |<---->    Agent     |
 |              |    |     |         |     +-----------+| ||    |              |
 +--------------+    |     |         +------------------+ ||    +--------------+
                     |     +------------------------------+|
                     +-------------------------------------+
```

#### Step 2: Understanding NETCONF Operations

NETCONF protocol provides a set of actions called operations that are used to retrieve device operational 
information and manage device configuration.  Not all operations are supported by an agent and RPC replies should be 
checked for errors responses.  Here is a brief introduction to the common protocol operations you should be familiar 
with to get started:

* The `<get>` NETCONF operation is used to retrieve the running configuration and operation state from a network 
device.  

* The `<get-config>` NETCONF operation is used to retrieve all or a subset of a specific configuration from a network 
device.

* The `<edit-config>` NETCONF operation is used to load or a subset of specific configuration to the target datastore
on a network device.  The device will analyze the source and target configuration and make only the necessary 
changes to the target configuration.  The target configuration is not necessarily replaced, allowing you to make 
configuration changes without deleting the configuration first.

* The `<copy-config>` NETCONF operation is used to create or replace the entire target configuration datastore with a
specific source datastore.  If the target datastore exists, then the target datastore will be overwritten.

* The `<delete-config>` NETCONF operation is used to delete the entire target configuration datastore (the 
`<running>` datastore cannot be deleted).

* The `lock` and `unlock` NETCONF operations are used to lock or unlock a configuration datastore, preventing other 
CLI, SNMP, or NETCONF sessions from making configuration changes while locked.

* The `<close-session>` NETCONF operation is used to terminate a NETCONF session gracefully.

* The `<kill-session>` NETCONF operation is used to terminate a NETCONF session forcefully.  All active operations 
are aborted, all locks are resources are released, and the NETCONF session is closed.

A NETCONF `datastore` is a place on the NETCONF agent, or network device, that contains the configuration and 
operational state data.  A NETCONF `configuration datastore` is a datastore that contains the necessary configuration
to make the network device operational.  Every NETCONF operation must specify a target datastore.  The `<running>` 
configuration datastore is the only mandatory datastore specified by the NETCONF Internet Standard.  However, other 
datastores may be supported by the network device vendor.

### Exercise 3: Exploring IOS XE YANG Data Models with NETCONF

#### Objectives

The objectives for this exercise are to:

* Learn how to configure NETCONF in IOS XE 
* Learn how to verify the NETCONF configuration in IOS XE
* Learn how to make NETCONF connections using Python

Added in IOS XE Denali 16.3.1...Added support for Catalyst 9300 and 9500 series switches in IOS XE Denali 16.5.1b..
.Added support for Catalyst 9400 series switches in IOS XE Denali 16.6.2...Added support for Catalyst 9500 High 
Performance series switches in IOS XE 16.8.1a...

#### Step 1: Configuring NETCONF in IOS XE

To work with NETCONF on IOS XE, you must be a user with privilage level 15 and enable the NETCONF interface on your 
network device.  To do so, open a command line terminal and complete the following steps:

1. Establish an SSH connection to the IOS XE device.

2. From the IOS XE device, create a new user for NETCONF sessions and configure the IOS XE NETCONF interface:
    ```
    csr1kv>enable
    csr1kv# configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    csr1kv(config)#username netconf privilege 15 password C1sco12345
    csr1kv(config)#netconf-yang
    csr1kv(config)#end
    csr1kv#
    ```

That's all there is to it!  Let's test and verify NETCONF on your IOS XE device.

#### Step 2: Verifying NETCONF in IOS XE

You can use the following commands to verify the NETCONF configuration in IOS XE:

1. To display information about the IOS XE device NETCONF datastores, use the `show netconf-yang datastores` command,
for example:
    
    ```
    csr1kv#show netconf-yang datastores
    Datastore Name             : running
    
    csr1kv#
    ```
    
    You can see the default, manadatory `<running>` datastore is present.

2. To display information about active NETCONF sessions, use the `show netconf-yang sessions` command, for example:
    
    ```
    csr1kv#show netconf-yang sessions
    There are no active sessions
    
    csr1kv#
    ```
    
    You can see there are currently no active sessions, but we will change that soon!

3. To display information about NETCONF statistic on your IOS XE device, use the `show netconf-yang statistics` 
command, for example:
    
    ```
    csr1kv#show netconf-yang statistics
    netconf-start-time  : 2018-05-21T02:27:35+00:00
    in-rpcs             : 0
    in-bad-rpcs         : 0
    out-rpc-errors      : 0
    out-notifications   : 0
    in-sessions         : 0
    dropped-sessions    : 0
    in-bad-hellos       : 0
    
    csr1kv#
    ```
    
    Again, not much to see until we start using NETCONF later in this lab.

4. To display the status of the software processes required to support model driven programmability, use the `show 
platform software yang-management process` command, for example:
    
    ```
    csr1kv#show platform software yang-management process
    confd            : Running 
    nesd             : Running 
    syncfd           : Running 
    ncsshd           : Running 
    dmiauthd         : Running 
    nginx            : Running 
    ndbmand          : Running 
    pubd             : Running 
    
    csr1kv#
    ```
    
    Note that the `nginx` process is running if `ip http server` or `ip http secure-server` is configured in IOS XE.  
    This process is not required to be in the `Running` state for NETCONF to function correctly.

5. Let's make your first NETCONF connection to your IOS XE network device.
    
    We will establish a NETCONF connection manually using the `ssh` command from the command line terminal on your 
    lab workstation (output truncated for brevity):
    
    ```
    $ ssh -p 2223 netconf@127.0.0.1 -s netconf
    netconf@127.0.0.1's password: 
    <?xml version="1.0" encoding="UTF-8"?>
    <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <capabilities>
    <capability>urn:ietf:params:netconf:base:1.0</capability>
    <capability>urn:ietf:params:netconf:base:1.1</capability>
    <capability>urn:ietf:params:netconf:capability:writable-running:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:xpath:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:validate:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:validate:1.1</capability>
    <capability>urn:ietf:params:netconf:capability:rollback-on-error:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:notification:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:interleave:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:with-defaults:1.0?basic-mode=explicit&amp;also-supported=report-all-tagged</capability>
    <capability>urn:ietf:params:netconf:capability:yang-library:1.0?revision=2016-06-21&amp;module-set-id=88c694c75e847aba17e8ab19254ad090</capability>
    <capability>http://tail-f.com/ns/netconf/actions/1.0</capability>
    <capability>http://tail-f.com/ns/netconf/extensions</capability>
    <capability>http://cisco.com/ns/cisco-xe-ietf-ip-deviation?module=cisco-xe-ietf-ip-deviation&amp;revision=2016-08-10</capability>
    <capability>http://cisco.com/ns/cisco-xe-ietf-ipv4-unicast-routing-deviation?module=cisco-xe-ietf-ipv4-unicast-routing-deviation&amp;revision=2015-09-11</capability>
    </capabilities>
    <session-id>40</session-id></hello>]]>]]> 
    ```
    
    Leave this session in this terminal window open.
    
    Now return to the window with the original SSH session to your IOS XE device.  Use the `show netconf-yang 
    sessions` to view the active NETCONF session you've just established, for example:
    
    ```
    csr1kv#show netconf-yang sessions                    
    R: Global-lock on running datastore
    C: Global-lock on candidate datastore
    S: Global-lock on startup datastore
    
    Number of sessions : 1
    
    session-id  transport    username             source-host           global-lock  
    -------------------------------------------------------------------------------
    40          netconf-ssh  netconf              10.0.2.2              None         
    
    csr1kv#
    ```
    
    Return to the NETCONF session window and type `^c` to terminate the session.  Let's take a look at the screen 
    output from our first NETCONF session.
        
    When you established a secure NETCONF over SSH as a NETCONF manager (client), the IOS XE network device as the 
    agent (server) sent  a list of its NETCONF capabilities in an XML encoded data format.
    
    Note the list of capabilities should look somewhat familiar: they are YANG data models!  In fact, this 
    demonstrates that Cisco IOS XE supports industry standard YANG data models from the IETF and OpenConfig and 
    vendor specific YANG data models from Tail-F (acquired by Cisco in 2014) and Cisco.
    
    Note the `<session-id>40</session-id>` corresponds with the session ID from the IOS XE CLI command
    `show netconf-yang sessions` output.

Using SSH to establish a NETCONF connection manually is not recommended and was only shown here for illustrative 
purposes.  Doing so would require that you copy-and-paste XML encoded RPC commands by hand to manage and configure 
your network device.  That defeats the purspose and intent of what we're teaching in this lab.  Now that we have 
successfully configured and tested NETCONF on IOS XE, let's see how to put Python to use to write applications for 
model drive programmability using NETCONF.

#### Step 3: Using Python to Make NETCONF Connections

In the previous example we used SSH to establish a NETCONF session.  While it is a good example of the communication 
flow, it is not the most user friendly method for using NETCONF.  Alternatively, we will use the Python library 
[ncclient](https://github.com/ncclient/ncclient) to communicate via NETCONF with an IOS XE network device 
programmatically.

1. From the command line terminal, ensure that ncclient is installed:
    
    ```
    $ pip3 install ncclient
    ```

2. Invoke the Python interpreter with the `python3` command:
    
    ```
    $ python3
    Python 3.6.5 (default, Mar 30 2018, 06:41:53) 
    [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

3. Import the `ncclient` Python library with the code snippet `from ncclient import manager`:
    
    ```
    >>> from ncclient import manager
    ```
    
    Import the `sys` Python library with the code snippet `import sys`:
    
    ```
    >>> import sys
    ```
    
    Establish a NETCONF connection and say "Hello" with the code snippet `m = manager.connect(host='127.0.0.1', 
    port=2223, username='netconf', password='C1sco12345', hostkey_verify=False)`:
    
    ```
    >>> m = manager.connect(host='127.0.0.1', port=2223, username='netconf', password='C1sco12345', hostkey_verify=False)
    ```
    
    Print the capabilities returned by the IOS XE network device with the code snippet `for capability in m.server_capabilities: print(capability.split('?')[0])` (output truncated for brevity)
    
    ```
    >>> for capability in m.server_capabilities:
    ...     print(capability.split('?')[0])
    ... 
    urn:ietf:params:netconf:base:1.0
    urn:ietf:params:netconf:base:1.1
    urn:ietf:params:netconf:capability:writable-running:1.0
    urn:ietf:params:netconf:capability:xpath:1.0
    urn:ietf:params:netconf:capability:validate:1.0
    urn:ietf:params:netconf:capability:validate:1.1
    urn:ietf:params:netconf:capability:rollback-on-error:1.0
    urn:ietf:params:netconf:capability:notification:1.0
    urn:ietf:params:netconf:capability:interleave:1.0
    urn:ietf:params:netconf:capability:with-defaults:1.0
    urn:ietf:params:netconf:capability:yang-library:1.0
    http://tail-f.com/ns/netconf/actions/1.0
    http://tail-f.com/ns/netconf/extensions
    http://cisco.com/ns/cisco-xe-ietf-ip-deviation
    http://cisco.com/ns/cisco-xe-ietf-ipv4-unicast-routing-deviation
          
    >>> 
  
    ```
    
    Close the NETCONF session and exit the Python interpreter with the code snippet `quit()`:
    
    ```
    >>> quit()
    $
    ```

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