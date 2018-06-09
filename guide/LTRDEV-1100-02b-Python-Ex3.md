### Exercise 3: Deploying Useful Python Packages

#### Objectives

The objectives for this exercise are to:

* Understand which Python packages are already installed
* Install useful Python packages for the Network Programmability Ninja

#### Step 1: Understanding which Python Packages are Installed

Once a virtual environment is created, a few specific packages are automatically installed. However, sometimes when 
going back into a project after not working on it for a while, it is useful to view which packages are already 
installed. 

1.  First make sure that your terminal still shows the prepended project name `(pythonenv)`. If it does not, 
then change to your lab working directory and activate the Python virtual environment you created earlier in this 
lab, for example:
    
    ```
    $ cd ~/lab
    $ source pythonenv/Scripts/activate
    (pythonenv) $
    ```

2. The `pip` tool is a software management system to install and maintain packages in Python. Before working with it in this virtual environment, it must be updated:

    ```
    (pythonenv) $ python -m pip install --upgrade pip==10.0.1
    Cache entry deserialization failed, entry ignored
    Collecting pip==10.0.1
      Using cached https://files.pythonhosted.org/packages/0f/74/ecd13431bcc456ed390
    b44c8a6e917c1820365cbebcb6a8974d1cd045ab4/pip-10.0.1-py2.py3-none-any.whl
    Installing collected packages: pip
      Found existing installation: pip 9.0.3
        Uninstalling pip-9.0.3:
          Successfully uninstalled pip-9.0.3
    Successfully installed pip-10.0.1
    
    (pythonenv) $
    ```

3. Now that `pip` has been updated in this virtual environment, it can be used to manage packages and modules in Python. List installed packages with `pip list` at the terminal.
    
    ```
    (pythonenv) $ pip list
    Package    Version
    ---------- -------
    pip        10.0.1
    setuptools 39.0.1

    (pythonenv) $
    ```

    As seen here, this virtual environment is still 'vanilla' with no additional packages installed.

#### Step 2: Installing Useful Python Packages

There are plenty of useful packages when working with network programmability. 

* requests: This installs a library useful for making HTTP operations, which is necessary for working with REST API's.
* ncclient: The ncclient library provides a client library for working with NETCONF.
* paramiko: Paramiko provides an implementation of SSHv2 into Python, enabling a python script to interact with a 
    network device over SSH.
* netmiko: Netmiko is a library that simplifies Paramiko for use with network devices such as those running 
    Cisco IOS-XE.
* ipaddress: This library allows Python to handle IP addresses with functions to effectively work with IP's and subnets.

1. We can use `pip` to install packages into our virtual environment, for example `pip install  netmiko` to install this one particular package. `pip` takes care of dependencies as well, meaning that if other packages are necessary for netmiko, they will be installed as well.
    (output truncated for brevity):

    ```
    (pythonenv) $ pip install netmiko
    Successfully installed asn1crypto-0.24.0 bcrypt-3.1.4 cffi-1.11.5 cryptography-2.2.2 idna-2.6 netmiko-2.1.1 paramiko-2.4.1 pyasn1-0.4.3 pycparser-2.18 pynacl-1.2.1 pyserial-3.4 pyyaml-3.12 scp-0.11.0 six-1.11.0 textfsm-0.4.1
    (pythonenv) $
    ```

2. In addition to using `pip` for installing new packages, it can also be used to upgrade existing packages. For instance, use `pip install -U setuptools==39.2.0` to upgrade the setuptools package:

    ```
    (pythonenv) $ pip install -U setuptools==39.2.0
    Collecting setuptools==39.2.0
      Using cached https://files.pythonhosted.org/packages/7f/e1/820d941153923aac1d49d7fc37e17b6e73bfbd2904959fffbad77900cf92/setuptools-39.2.0-py2.py3-none-any.whl
    Installing collected packages: setuptools
      Found existing installation: setuptools 39.0.1
        Uninstalling setuptools-39.0.1:
          Successfully uninstalled setuptools-39.0.1
    Successfully installed setuptools-39.2.0

    (pythonenv) $
    ```

3. Many times, projects list the specific package and version requirements so that repeatable installations are possible and successful. This will typically show up as a file named `requirements.txt` and can often be found at the root of a project's file structure. One of these files exists in the git repository for this lab, which will allow for a quick installation of all required packages. Use this file to install the remaining packages required for this lab:
    
    ```
    (pythonenv) $ pip install ~/lab/LTRDEV-1100/requirements.txt

    ```

4. Now, all of the correct packages and versions should be installed. Confirm with the command `pip list`, for example:
    
    ```
    (pythonenv) $ pip list
    Package      Version
    ------------ ---------
    asn1crypto   0.24.0
    bcrypt       3.1.4
    certifi      2018.4.16
    cffi         1.11.5
    chardet      3.0.4
    cryptography 2.2.2
    idna         2.6
    lxml         4.2.1
    ncclient     0.5.3
    netmiko      2.1.1
    paramiko     2.4.1
    pip          10.0.1
    pyasn1       0.4.3
    pycparser    2.18
    PyNaCl       1.2.1
    pyserial     3.4
    PyYAML       3.12
    requests     2.18.4
    scp          0.11.0
    setuptools   39.2.0
    six          1.11.0
    textfsm      0.4.1
    urllib3      1.22
    (pythonenv) $
    ```
    
Alright! Now that the virtual environment is active and is ready for any future packages, it is a great time to 
start trying out Python.
