Navigation - [Previous Page](LTRDEV-1100-Guide-02c.md)

---

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

1. Open the Git Bash terminal application and type the command `python` at the command prompt:
    
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

---

Navigation - [Next Page](LTRDEV-1100-Guide-02e.md)
