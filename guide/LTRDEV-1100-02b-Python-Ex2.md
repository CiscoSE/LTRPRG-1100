Navigation - [Previous Page](LTRDEV-1100-02b-Python-Ex2.md)

---

### Exercise 2: Setting up Python Virtual Environments

#### Objectives

The objectives for this exercise are to:

* Setup a Python virtual environment for this lab

Different projects using Python may have different environment requirements. For instance, one project may need a 
Python 2.x interpreter, whereas others may need Python 3.x. Some projects may require many Python packages and 
modules to be installed, and others may only use built-in modules.

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

---

Navigation - [Next Page](LTRDEV-1100-Guide-02f.md)


