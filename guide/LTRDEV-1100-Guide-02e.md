Navigation - [Previous Page](LTRDEV-1100-Guide-02e.md)

---

### Exercise 2: Setting up Python Virtual Environments

#### Objectives

The objectives for this exercise are to:

* Setup a Python virtual environment for this lab

Different projects using Python may have different environment requirements. For instance, one project may need Python 
2.x interpreter, whereas others may need Python 3.x. Some projects may require many Python packages and modules to be 
installed, and others may only use built-in modules.

Traditionally, installing a package for Python is a global change on a particular host. This means that if one project 
needs access to one version of a package, and another project needs to upgrade to a different version of the same 
package, it could break the first project. Thankfully, there is a tool that can help tackle this problem: Virtualenv.

Virtualenv allows isolating Python environments to specific directories, as opposed to globally. This means each 
virtual environment can run its own Python executable in the correct version, and install its own packages and modules. 
By creating separate virtual environments per project, a developer can manage these dependencies of each project 
without inadvertently causing harm to other projects.

#### Step 1: Setting up a Python Virtual Environment

Now that we know that Python v3.x is available for use, it is time to set up a virtual environment to continue working
in.

1.  First, create and enter a directory called `pythonenv` as a home for your project.
    
    ```
    $ cd ~/lab
    $ mkdir pythonenv
    ```

2.  Next, create a Python virtual environment in this directory. By default, Virtualenv will use the current Python 3
.x version installed on the host as its version, for example:

    ```
    $ python -m venv pythonenv
    
    $
    ```

3.  Now that the virtual environment is created, go ahead and activate it so that any packages installed for your 
project will stay within this specific environment. This is done by running the `activate` command in the virtual 
environment directory you created.  The path to the `activate` command will vary based on the platform you working.  
For Windows, the `activate` command can be found in `Scripts` directory, for example `pythonenv/Scripts/activate`.  
For macOS and Linux, the `activate` command can be found in the `bin` directory, for example `pythonenv/bin/activate`.
    
    For the purposes of this lab in the Windows lab environment we've prepared for you, using the Git Bash terminal 
    application, activate the Python virtual environment with the command `source pythonenv/Scripts/activate`, for example:
    
    ```
    $ source pythonenv/Scripts/activate
    (pythonenv) $
    ```
    
    Now that the environment has been activated, notice that the prompt is now prepended with the virtual 
    environment project name. This means that any packages that you install or remove in this terminal window will 
    be specific to this project unless you deactivate the virtual environment or close the terminal window session.
 
4. To deactivate the Python virtual environment, simply use the `deactivate` command (do not use the `source` command)
regardless of the platform you are running, for example:
    
    ```
    (pythonenv) $ deactivate
    $
    ```

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
    Collecting pip
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

### Exercise 4: Working with Python Interpreter

#### Objectives

The objectives for this exercise are to:

* Work with the Python interpreter
* Run a Python script

#### Step 1: Working with the Python Interpreter

Recall that Python is an interpreted language, meaning that every command is evaluated as it is run. The Python 
interpreter can be run interactively, allowing for real-time testing of code. This can be a great way to learn how a 
particular function acts, or as a quick way to execute a couple of one-time use Python code.

1.  First make sure that your terminal still shows the prepended project name `(pythonenv)`. If it does not, 
then change to your lab working directory and activate the Python virtual environment you created earlier in this 
lab, for example:
    
    ```
    $ cd ~/lab
    $ source pythonenv/Scripts/activate
    (pythonenv) $
    ```

2.  Run the interactive interpreter by issuing the `python` command in the terminal, for example:

    ```
    (pythonenv) $ python
    Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Inte
    l)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

3.  Notice that once the Python interpreter is running, the prompt changes to `>>>`. This is where you can input Python 
code. Start with printing `Hello World!` to the screen, as shown below:

    ```
    >>> print("Hello World!")
    Hello World
    >>>
    ```

4.  The interactive interpreter is mainly used for practicing, learning, debugging, or quick-use. As Python has many 
built-in math and numeric functions, it can be an easy way to do quick arithmetic. For example, calculate how 
much cash to bring for a $50 dinner, including 15% tip and 6% sales tax:

    ```
    >>> 50*(1.15+.06)
    60.5
    >>>
    ```
    
    Sometimes our on-the-fly mathematics needs are directly related to our network programmability ninja skills. For 
    instance, you may need to convert DSCP values to ToS values. Converting DSCP to ToS for quality of service is
    done by bit-shifting by 2 bits to the left (padding a binary number with two 0s). Doing this on paper, you would
    typically write out the binary representation of the DSCP integer, then pad two 0s on the right side of this 
    binary string, and then mentally convert that new binary string back into an integer. Python makes quick work of 
    this:
    
    ```
    >>> 46 << 2
    184
    >>>
    ```
    
    The `<<` operator executes a left bit-shift operation on the number to the left of the operator by the number of 
    bits indicated to the right of the operator. In this example, we bit-shifted two bits to the left on DSCP 46, 
    leaving us with a ToS value of 184. 

5.  To exit the interpreter, type `quit()` or use the key-sequence `CTRL-D` and it will return you to the 
    terminal prompt, for example:
    
    ```
    >>> quit()
    (pythonenv) $
    ```

#### Step 2: Running a Python Script

While the interactive Python interpreter is useful for occasional and instructional use, the majority of work with 
Python will be done by creating and running scripts. A Python script is a set of instructions written in a language 
that the Python interpreter understands. The script is written in a text editor or IDE, and 
then run against the Python interpreter.

1.  First make sure that your terminal still shows the prepended project name `(pythonenv)`. If it does not, 
then change to your lab working directory and activate the Python virtual environment you created earlier in this 
lab, for example:
    
    ```
    $ cd ~/lab
    $ source pythonenv/Scripts/activate
    (pythonenv) $
    ```

2.  Let's create a new Python script:
    
    ```
    (pythonenv) $ echo 'print("Hello World!")' >> helloworld.py
    ```

3.  Run the Python script by running the command `python helloworld.py`, for example:
    
    ```
    (pythonenv) $ python helloworld.py
    Hello World!
    (pythonenv) $
    ```

    By putting your Python instructions into a file, it can be called at any time by the Python interpreter. This is 
    key to reusing code.

---

Navigation - [Next Page](LTRDEV-1100-Guide-02f.md)


