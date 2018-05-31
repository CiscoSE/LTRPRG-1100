## Python for Network Programmability

TODO:

- [x] @mgalazka Draft "Tools of the Ninja - Python for Network Programmability"
- [ ] Edit for directory, example output, and style consistency
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

### Understanding Python Versions

When it comes to programming in Python, it's critical to understand which Python interpreter is installed in the 
environment. The reason for this is that Python 3.0 re-wrote certain aspects of the language, which broke backward 
compatibility with Python 2. While it is still common to find Python files (scripts) written for use with Python 2, 
most projects are now written for use with Python 3. In this lab, Python 3 is the interpreter to use.

While the two versions are different, it is entirely possible to have both Python 2 and Python 3 on the same computer. 
It's also possible to have several different versions of each installed at the same time (i.e. Python 3.4, 3.5, 3.6). 
For these reasons, it is important to understand which version of Python you are running.

### Setting up Virtual Environments

Different projects using Python may have different environment requirements. For instance, one project may need Python 
2.x interpreter, whereas others may need Python 3.x. Some projects may require many Python packages and modules to be 
installed, and others may only use built-in modules.

Traditionally, installing a package for Python is a global change on a particular host. This means that if one project 
needs access to one version of a package, and another project needs to upgrade to a different version of the same 
package, it could break the first project. Thankfully, there is a tool that can help tackle this problem: virtualenv.

Virtualenv allows isolating python environments to specific directories, as opposed to globally. This means each 
virtualenv can run its own Python executable in the correct version, and install its own packages and modules. 
By creating separate virtual environments per project, a developer can manage these dependencies of each project 
without inadvertently causing harm to other projects.

### Exercise 1: Setting Up a Python Environment

#### Objectives

The objectives for this exercise are to:

* Check the version of Python
* Set up a virtual environment to work in

#### Step 1: Checking the version of Python

In order to work with Python, we need to make sure that it is properly installed, able to run, and is of the 
correct version.

1.  Open a terminal, and at the command prompt, enter the command `python -V` (case-sensitive) and check the output. 
    The output should look similar to below:
    
    ```
    $ python -V
    Python 3.6.3
    ```

    In some scenarios when both Python 2.x and Python 3.x are installed on the same host, you may need to run 
    `python3 -V` to get these results. If this is the case, please use `python3` to run python in the following step.

#### Step 2: Setting up a Virtual Environment

Now that we know that Python 3 is available for use, it is time to set up a virtual environment to continue working in.

1.  First, create and enter a directory called `LTRDEV-1100` as a home for your project.
    ```
    $ mkdir LTRDEV-1100
    ```

2.  Next, create a virtual environment in this directory. By using the `-p python3` parameter, virtualenv will use the 
    current Python 3.x version installed on the host as its version. 

    ```
    $ virtualenv -p python3 LTRDEV-1100
    Running virtualenv with interpreter /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
    Using base prefix '/Library/Frameworks/Python.framework/Versions/3.6'
    New python executable in ~/LTRDEV-1100/bin/python3
    Also creating executable in ~/LTRDEV-1100/bin/python
    Installing setuptools, pip, wheel...done.
    ```

3.  Now that the virtual environment is created, go ahead and activate it so that any packages installed for our 
    project will stay within this specific environment. This is done by typing `source bin/activate` from within the 
    project's working directory.

    ```
    $ cd LTRDEV-1100
    $ source bin/activate
    (LTRDEV-1100) $
    ```

    Now that the environment has been activated, notice that the prompt is now prepended with the project name. This 
    means that any packages that you install or remove in this terminal window will be specific to this project unless 
    you `deactivate` or close the terminal.

### Exercise 2: Deploying Useful Packages

#### Objectives

The objectives for this exercise are to:

* Understand which packages are already installed
* Install useful packages for a Network Programmabity Ninja

#### Step 1: Understanding which Packages are Installed
Once a virtual environment is created, a few specific packages are automatically installed. However, sometimes when 
going back into a project after not working on it for a while, it is useful to view which packages are already 
installed. 

1.  First make sure that your terminal still shows the prepended project name `(LTRDEV-1100)`. If it does not, 
    then `cd` back into that directory and issue `source bin/activate` first.

2.  The `pip` tool is a software management system to install and maintain packages in Python. List installed packages 
    with `pip list` at the terminal.
    
    ```
    (LTRDEV-1100) $ pip list
    Package    Version
    ---------- -------
    pip        10.0.1
    setuptools 39.1.0
    wheel      0.31.0
    (LTRDEV-1100) $
    ```

    As seen here, this virtual environment is still 'vanilla' with no additional packages installed.

#### Step 2: Installing Useful Packages
There are plenty of useful packages when working with network programmability. 

* requests: This installs a library useful for making HTTP operations, which is necessary for working with REST API's.
* ncclient: The ncclient library provides a client library for working with NETCONF.
* paramiko: Paramiko provides an implementation of SSHv2 into Python, enabling a python script to interact with a 
    network device over SSH.
* netmiko: Netmiko is a library that simplifies Paramiko for use with network devices such as those running 
    Cisco IOS-XE.
* ipaddress: This library allows Python to handle IP addresses with functions to effectively work with IP's and subnets.

1. We can use `pip` to install these packages into our virtual environment. Issue: 
    `pip install requests ncclient paramiko netmiko ipaddress` to install all of these packages and their prerequisites.

    ```
    (LTRDEV-1100) $ pip install requests ncclient paramiko netmiko ipaddress
    Collecting requests
    ... [output truncated] ...
    ```

    Alright! Now that the virtual environment is active and is ready for any future packages, it is a great time to 
    start trying out python.

### Execise 3: Working with Python 

#### Objectives

The objectives for this exercise are to:

* Work with the Python interpreter
* Run a Python Script

#### Step 1: Working with the Python Interpreter

Recall that Python is an interpreted language, meaning that every command is evaluated as it is run. The Python 
interpreter can be run interactively, allowing for real-time testing of code. This can be a great way to learn how a 
particular function acts, or as a quick way to execute a couple of one-time use Python code.

1.  Run the interactive interpreter by issuing `python` at the terminal.

    ```
    (LTRDEV-1100) $ python
    Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    ```

2.  Notice that once the Python interpreter is running, the prompt changes to `>>>`. This is where you can input Python 
    code. Start with printing `Hello World!` to the screen, as shown below.

    ```
    >>> print("Hello World!")
    Hello World
    >>>
    ```

3.  The interactive interpreter is mainly used for practicing, learning, debugging, or quick-use. As Python has many 
    built-in math and numeric functions, it can be an easy way to do quick arithmetic. Need to know how much cash to 
    bring for a $50 dinner, including 15% tip and 6% sales tax?

    ```
    >>> 50*(1.15+.06)
    60.5
    >>>
    ```
    
    Sometimes our on-the-fly mathematics needs are directly related to our network ninja skills. For instance, you may 
    need to convert DSCP values to ToS values. Converting DSCP to ToS for quality of service is done by bit-shifting by 
    2 bits to the left (padding a binary number with two 0's). Doing this on paper, one would typically write out the 
    binary representation of the DSCP integer, then pad two 0's on the right side of this binary string, and then 
    mentally convert that new binary string back into an integer. Tough? Then use Python.
    
    ```
    >>> 46 << 2
    184
    >>>
    ```
    
    The `<<` operator executes a left bit-shift operation on the number to the left of the operator by the number of 
    bits indicated to the right of the operator. In this example, we bit-shifted two bits to the left on DSCP 46, 
    leaving us with a ToS value of 184. 

4.  To exit the interpreter, type `quit()` or use the key-sequence `CTRL-D` and it will return you to the 
    terminal prompt.

#### Step 2: Running a Python Script

While the interactive Python interpreter is useful here and there, the majority of work with Python will be done by 
creating and running scripts. A Python script is a set of instructions written in a language that the Python 
interpreter understands. The script is written in a text editor or developement environment, and then run against the 
Python interpreter.

1.  Return to your terminal window, and ensure that your are in your virtual environment. If the prompt is not 
    prepended with `(LTRDEV-1100)` please `cd` to your project directory and issue `source bin/activate`.

2.  Create your first python script by editing the file `helloworld.py` in nano by issuing the command:
    `nano -w helloworld.py`

    This will open the nano text editor program.

3.  Let's create our first script! Type the following into nano:

    ```
    print("Hello world!")
    myNumber = 5
    print("My favorite number is", myNumber)
    ```

4.  Once you have inputted this into nano, type the command sequence `CTRL-X`, followed by `y` to save changes, and 
    hit enter to accept the filename.

5.  Run the script by issuing `python helloworld.py`
    
    ```
    (LTRDEV-1100) $ python helloworld.py
    Hello world!
    My favorite number is 5
    (LTRDEV-1100) $
    ```

    By putting your Python instructions into a file, it can be called at any time by the Python interpreter. This is 
    key to reusing code.
