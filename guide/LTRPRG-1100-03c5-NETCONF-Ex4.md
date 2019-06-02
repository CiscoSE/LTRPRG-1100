Navigation :: [Previous Page](LTRPRG-1100-03c4-NETCONF-Ex3.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-03d1-GuestShell.md)

---

### Exercise 4: Exploring IOS XE NETCONF/YANG Example Use Cases

#### Objectives

The objectives for this exercise are to:

* Explore more IOS XE NETCONF/YANG example scripts

In this lab's GitHub repository are a few additional Python scripts we've provided as further examples of how to 
interface with your IOS XE network device with model driven programmability.

#### Step 1: Running IOS XE NETCONF Example Scripts

1. Open the Git Bash terminal by double clicking the Git Bash icon on the desktop:
    
    ![Git Bash Icon](assets/GitBash-Icon.png)
    
    ![Git Bash Terminal](assets/GitBash-Term.png)

2.  Make sure that your terminal still shows the prepended project name `(pythonenv)`. If it does not, then activate 
the Python virtual environment you created earlier in this lab with the `source ~/lab/pythonenv/Scripts/activate` 
command, for example:
    
    ```
    $ source ~/lab/pythonenv/Scripts/activate
    (pythonenv) $
    ```

3. Navigate to the `code` directory in this lab's Git repository with the `cd ~/lab/LTRPRG-1100/code` command:
    
    ```
    (pythonenv) $ cd ~/lab/LTRPRG-1100/code
    (pythonenv) $
    ```
    
4. Run the `iosxe-get-capabilities.py` Python script with the `python iosxe-get-capabilities.py` command, for example 
(output truncated for brevity):
    
    ```
    (pythonenv) $ python iosxe-get-capabilities.py
    ***Here are the Remote Devices Capabilities***
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
    (pythonenv) $
    ```
    
    This output should look familiar.  This is the NETCONF capabilities from the network device; the same 
    capabilities we saw in the last exercise in this lab.

5. Run the `iosxe-get-config.py` Python script with the `python iosxe-get-config.py` command, for example 
(output truncated for brevity):
    
    ```
    (pythonenv) $ $ python iosxe-get-config.py
    <?xml version="1.0" ?>
    <rpc-reply message-id="urn:uuid:db6fe2a1-06ee-4c3d-8de4-9c869fce3d1b" xmlns="urn
    :ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:b
    ase:1.0">
        <data>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <version>16.8</version>
                    <boot-start-marker/>
                        <boot>
                            <system>
                                <bootfile>
                                    <filename-list>
                                        <filename>bootflash:csr1000v-universalk9.16.08.03.SPA.bin</filename>
                                    </filename-list>
                                </bootfile>
                            </system>
                        </boot>
                    <boot-end-marker/>
    ```
    
    This output should also look familiar.  This is the `running-config` from the network device in XML-encoded text.
    This is the IOS XE `running-config` as represented by the `Cisco-IOS-XE-native` YANG model.

6. Run the `iosxe-get-hostname.py` Python script with the `python iosxe-get-hostname.py` command:
    
    ```
    (pythonenv) $ python iosxe-get-hostname.py
    csr1
    (pythonenv) $
    ```

7. Run the `iosxe-get-intinfo.py` Python script with the `python iosxe-get-intinfo.py` command:
       
    ```
    (pythonenv) $ python iosxe-get-intinfo.py
    GigabitEthernet1, description: empty
    Loopback1,        description: empty
    Loopback2,        description: empty
    Loopback3,        description: empty
    (pythonenv) $
    ```

These are simple examples of how to write Python scripts for model driven programmability using NETCONF and YANG.  
Take and study these examples and use them to explore your own use cases.  These should serve as a starting point for
helping you automate repeatable, repetitive tasks like a Network Programmability Ninja.

Let's take a look at how to extend network programmability to the edge of your network with IOS XE Guest Shell.

---

Navigation :: [Previous Page](LTRPRG-1100-03c4-NETCONF-Ex3.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-03d1-GuestShell.md)
