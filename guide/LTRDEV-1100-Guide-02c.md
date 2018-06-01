Navigation - [Previous Page](LTRDEV-1100-Guide-02b.md)

---

## Python for Network Programmability

TODO:

- [x] @mgalazka Draft "Tools of the Ninja - Python for Network Programmability"
- [x] Edit for directory, example output, and style consistency
- [ ] Proofread

### Introducing Python

[Python](https://www.python.org/) is a popular programming language and a great first language to learn. Python is 
highly readable, object oriented, and it can be run interactively through the Python interpreter. One reason that 
Python has become quite popular is due to its plethora of available modules, or reusable code, to tackle many different 
projects or tasks. Additionally, Python is available for many different operating systems, some of which even include 
it by default. This allows the same Python scripts to be written, modified, and executed by users on Windows, Mac, 
Linux, and more.

Learning a language like Python is really important on a journey towards network programmability. Python gives the 
flexibility to create reusable code to solve a particular problem, or perhaps automate a series of steps. Through its 
modules, Python can be used to communicate with networking devices in many ways, including SSH, NETCONF, 
and REST API's. With so many uses, it is one of the most powerful tools a Network Programmability Ninja can have.

### Exercise 1: Understanding How to Run Python

#### Objectives

The objectives for this exercise are to:

* Understand how to invoke different versions of the Python interpreter

When it comes to programming in Python, it's critical to understand which Python interpreter is installed in the 
environment. The reason for this is that Python 3.0 re-wrote certain aspects of the language, which broke backward 
compatibility with Python 2. While it is still common to find Python files (scripts) written for use with Python 2, 
most projects are now written for use with Python 3. In this lab, Python 3 is the interpreter to use.

While the two versions are different, it is entirely possible to have both Python 2 and Python 3 on the same computer. 
It's also possible to have several different versions of each installed at the same time (i.e. Python 3.4, 3.5, 3.6). 
For these reasons, it is important to understand which version of Python you are running.

#### Step 1: Running the Python Interpreter

In order to work with Python, we need to make sure that it is properly installed, able to run, and is of the 
correct version.  On all operating systems and platforms, the Python interpreter executable is `python`.

1. Open the Git Bash terminal 
application and type the command `python` at the command prompt:
    
    ```
    $ python
    Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Inte
    l)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
    
    You've successfully started the Python interpreter, which identifies itself as version 3.6.5.  Type `quit()` and 
    press the `Enter`/`Return` key to exit out of the interpreter:
    
    ```
    >>>quit()
    $
    ```

#### Step 2: Checking the Version of the Python Interpreter

1.  Open a terminal, and at the command prompt, enter the command `python -V` (case-sensitive) and check the output. 
    The output should look similar to below:
    
    ```
    $ python -V
    Python 3.6.5
    ```
    
    In some situations, both Python 2.x and Python 3.x are installed on the same system.  Which version of the Python
    interpreter you invoke with the `python` command depends on which executable your operating systems shell finds 
    in the command search path environment variable.
    
    In typical macOS and Linux installation, there are command aliases `python`, `python3` to invoke Python v2.x 
    and 3.x, respectively.  In a typical Windows installation, the Python v3.x Windows installer will install the 
    Python version helper command `py`.
    
    In a terminal, run the command `py -V`, for example:
    
    ```
    $ py -V
    Python 3.6.5
    $
    ```
    
    In Windows, to invoke the Python v2.x interpreter specifically, use the command `py -2`, for example:
    
    ```
    $ py -2 -V
    Python 2.7.15
    $
    $ py -2
    Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AM
    D64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> quit()
    $
    ```
    
    In Windows, to invoke the Python v3.x interpreter specifically, use the command `py -3`, for example:
    
    ```
    $ py -3 -V
    Python 3.6.5
    $ py -3
    Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Inte
    l)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    $
    ```
    
    For the purposes of this lab, we've setup the lab workstation environment to only include the Python v3.x 
    interpreter `python` command to be in the command search path.  Unless otherwise specified, we assume Python v3.x
    in this lab and you can invoke the interpreter or run applications with the `python` command.

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
    $ virtualenv pythonenv
    Using base prefix 'c:\\users\\administrator\\appdata\\local\\programs\\python\\python36-32'
    New python executable in C:\Users\Administrator\lab\pythonenv\Scripts\python.exe
    Installing setuptools, pip, wheel...done.
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
 
4. To deactivate the Python virtual environment, simply use the `deactivate` command regardless of the platform you 
are running, for example:
    
    ```(pythonenv) $ deactivate
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

2.  The `pip` tool is a software management system to install and maintain packages in Python. List installed packages 
with `pip list` at the terminal.
    
    ```
    (pythonenv) $ pip list
    Package    Version
    ---------- -------
    pip        10.0.1
    setuptools 39.2.0
    wheel      0.31.1

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

1. We can use `pip` to install these packages into our virtual environment, for example `pip install requests 
ncclient paramiko netmiko ipaddress` to install all of these packages and their prerequisites with one command 
(output truncated for brevity):

    ```
    (pythonenv) $ pip install requests ncclient paramiko netmiko ipaddress
    Successfully installed asn1crypto-0.24.0 bcrypt-3.1.4 certifi-2018.4.16 cffi-1.11.5 chardet-3.0.4
    cryptography-2.2.2 idna-2.6 ipaddress-1.0.22 lxml-4.2.1 ncclient-0.5.3 netmiko-2.1.1 paramiko-2.4.1 pyasn1-0.4.3 
    pycparser-2.18 pynacl-1.2.1 pyserial-3.4 pyyaml-3.12 requests-2.18.4 scp-0.11.0 six-1.11.0 textfsm-0.4.1 
    urllib3-1.22
    (pythonenv) $
    ```

    Confirm with the command `pip list`, for example:
    
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
    ipaddress    1.0.22
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
    wheel        0.31.1
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

Navigation - [Next Page](LTRDEV-1100-Guide-02d.md)
