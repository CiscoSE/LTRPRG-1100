Navigation :: [Previous Page](LTRPRG-1100-02b1-Python.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-02b3-Python-Ex2.md)

---

### Exercise 1: Understanding How to Run Python

#### Objectives

The objectives for this exercise are to:

* Understand how to invoke different versions of the Python interpreter

When it comes to programming in Python, it's critical to understand which Python interpreter is installed in the 
environment. The reason for this is that Python 3.0 re-wrote certain aspects of the language, which broke backward 
compatibility with Python 2. While it is still common to find Python code written for use with Python 2, most 
projects are now written for use with Python 3. To date, Python 2 is the default Python version installed on 
Apple macOS or Linux distributions, but be aware that Python 2 will not longer be maintained after January 1, 
2020.  We recommend you are aware of Python 2 and how to run Python 2 code if necessary, but focus your learning on
Python 3 in your journey of network programmability.  In this lab, Python 3 is the interpreter to use.

While the two versions are different, it is entirely possible to have both Python 2 and Python 3 on the same system. 
It's also possible to have several different versions of each installed at the same time (i.e. Python 2.7, 3.4, 3.6,
3.7). For these reasons, it is important to understand which version of Python you are running.

#### Step 1: Running the Python Interpreter

In order to work with Python, we need to make sure that it is properly installed, able to run, and is of the 
correct version.  There are various conventions for the command name for the Python interpreter(s) installed on a 
system.  On all operating systems and platforms, it is common for the Python interpreter executable to be `python`.  
However, which version of Python?  Let's show how to invoke the interpreter and see which version(s) are installed.

1. Open the Git Bash terminal by double clicking the Git Bash icon on the desktop:
    
    ![Git Bash Icon](assets/GitBash-Icon.png)
    
    ![Git Bash Terminal](assets/GitBash-Term.png)

2. Type the command `python` at the command prompt, for example:
    
    ```
    $ python
    Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD6
    4)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
    
    You've successfully started the Python interpreter, which identifies itself as version 3.7.3.  We'll look at 
    how to interact with the interpreter later in this lab.  For now, type `quit()` and press the `Enter` or `Return` 
    key to exit out of the interpreter, for example:
    
    ```
    >>>quit()
    $
    ```

#### Step 2: Checking the Version of the Python Interpreter

1.  Enter the command `python -V` (case-sensitive) and check the output.  The output should look
similar to below:
    
    ```
    $ python -V
    Python 3.7.3
    $
    ```
    
    In some situations, both Python 2.x and Python 3.x are installed on the same system.  Which version of the Python
    interpreter you invoke with the `python` command depends on which executable your operating system shell finds 
    in the command search path environment variable.
    
    In typical macOS and Linux installations, there are command aliases `python2` and `python3` to invoke Python 
    version 2.x and 3.x, respectively.  Use the `-V` command line argument to the Python interpreter command line 
    executable to determine which version of Python you are invoking.
    
2.  In a typical Windows installation, the Python v3.x Windows installer will install the Python version helper 
command `py`.  Since we're working in a Windows developer environment in this lab, you can see how the `py` command 
works.
    
    Run the command `py -V`, for example:
    
    ```
    $ py -V
    Python 3.7.3
    $
    ```
    
    In Windows, to invoke the Python v2.x interpreter specifically, use the `py -2 -V` and `py -2` commands, for 
    example:
    
    ```
    $ py -2 -V
    Python 2.7.16
    $ py -2
    Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AM
    D64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
    
    Type `quit()` and press the `Enter` or `Return` key to exit out of the interpreter, for example:
    
    ```
    >>>quit()
    $
    ```
    
    In Windows, to invoke the Python v3.x interpreter specifically, use the command `py -3 -V` `py -3` commands, for 
    example:
    
    ```
    $ py -3 -V
    Python 3.7.3
    $ py -3
    Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD6
    4)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
    
    Type `quit()` and press the `Enter` or `Return` key to exit out of the interpreter, for example:
    
    ```
    >>>quit()
    $
    ```
    
    For the purposes of this lab, we've setup the lab workstation environment to only include the Python v3.x 
    interpreter `python` command to be in the command search path.  Unless otherwise specified, we assume Python 
    version 3 in this lab and you can invoke the interpreter or run applications with the `python` command.

Next, let's take a look at how you can manage the Python interpreter version and Python development environment for 
projects with Python virtual environments.

---

Navigation :: [Previous Page](LTRPRG-1100-02b1-Python.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-02b3-Python-Ex2.md)
