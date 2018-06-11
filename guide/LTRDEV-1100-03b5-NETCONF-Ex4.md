Navigation :: [Previous Page](LTRDEV-1100-03b4-NETCONF-Ex3.md) :: [Table of Contents](LTRDEV-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRDEV-1100-03c1-GuestShell.md)

---

### Exercise 4: Exploring IOS XE NETCONF/YANG Example Use Cases

#### Objectives

The objectives for this exercise are to:

* Explore more IOS XE NETCONF/YANG example scripts

In this lab's GitHub repository are a few additional Python scripts we've provided as further examples of how to 
interface with your IOS XE network device with model driven programmability.

#### Step 1: Running IOS XE NETCONF Example Scripts

1. Open the Git Bash terminal by double clicking the Git Bash icon on the desktop:
    
    ![Git Bash Icon](assets/Git-01.png)
    
    ![Git Bash Terminal](assets/Git-02.png)

3. Navigate to the `code` directory in the Git repository for this lab:
    
    ```
    $ cd ~/lab/LTRDEV-1100
    $
    ```

4.  Make sure that your terminal still shows the prepended project name `(pythonenv)`. If it does not, then change to
your lab working directory and activate the Python virtual environment you created earlier in this lab:
    
    ```
    $ cd ~/lab
    $ source pythonenv/Scripts/activate
    (pythonenv) $
    ```

5. Navigate to the `code` directory in this lab's Git repository:
    
    ```
    (pythonenv) $ cd ~/lab/LTRDEV-1100/code
    (pythonenv) $
    ```
    
6. Run the `iosxe-get-capabilities.py` Python script with the `python` command (output truncated for brevity):
    
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

7. Run the `iosxe-get-hostname.py` Python script with the `python` command (output truncated for brevity):
    
    ```
    (pythonenv) $ python iosxe-get-hostname.py
    csr1
    (pythonenv) $
    ```

8. Run the `iosxe-get-intinfo.py` Python script with the `python` command (output truncated for brevity):
       
    ```
    (pythonenv) $ python iosxe-get-intinfo.py
    GigabitEthernet1, description: WAN interface
    (pythonenv) $
    ```

    These are simple examples of how to write Python scripts for model driven programmability using NETCONF and YANG.

---

Navigation :: [Previous Page](LTRDEV-1100-03b4-NETCONF-Ex3.md) :: [Table of Contents](LTRDEV-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRDEV-1100-03c1-GuestShell.md)
