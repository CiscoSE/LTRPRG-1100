Navigation :: [Previous Page](LTRPRG-1100-02b4-Python-Ex3.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-02c1-Teams.md)

---

### Exercise 4: Working with the Python Interpreter

#### Objectives

The objectives for this exercise are to:

* Learn how to work with the Python interpreter
* Learn how to run a Python script

#### Step 1: Working with the Python Interpreter

Recall that Python is an interpreted language, meaning that every command is evaluated as it is ran line-by-line. The 
Python interpreter can be ran interactively, allowing for real-time testing of code. This can be a great way to learn
how a particular function acts, or as a quick way to execute one-time use Python code.

1.  Open the Git Bash terminal by double clicking the Git Bash icon on the desktop:
    
    ![Git Bash Icon](assets/GitBash-Icon.png)
    
    ![Git Bash Terminal](assets/GitBash-Term.png)

2.  Make sure that your terminal still shows the prepended project name `(pythonenv)`. If it does not, then activate 
the Python virtual environment you created earlier in this lab with the `source ~/lab/pythonenv/Scripts/activate` 
command, for example:
    
    ```
    $ source ~/lab/pythonenv/Scripts/activate
    (pythonenv) $
    ```

2.  Run the interactive Python interpreter by issuing the `python` command in the terminal, for example:
    
    ```
    (pythonenv) $ python
    Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD6
    4)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

3.  Notice that once the interactive interpreter is running, the prompt changes to `>>>`. This is where you can input 
Python code. Start with printing `Hello World!` to the screen with the Python function `print()`.  For example, type 
the code snippet `print("Hello World")` and press the `Enter` or `Return` key in the interactive interpreter:
    
    ```
    >>> print("Hello World!")
    Hello World!
    >>>
    ```

4.  The interactive interpreter is mainly used for practicing, learning, debugging, or quick one-time use. As Python 
has many built-in math and numeric functions, it can be an easy way to do quick arithmetic.  For example, to 
calculate how much cash to bring for a $50 dinner, including 15% tip and 6% sales tax, type the code snippet
`50*(1.15+.06)` and press the `Enter` or `Return` key:
    
    ```
    >>> 50*(1.15+.06)
    60.5
    >>>
    ```

5.  Sometimes our on-the-fly mathematics needs are directly related to our Network Programmability Ninja skills. For 
instance, you may need to convert DSCP values to ToS values. Converting DSCP to ToS for quality of service is
done by bit-shifting by 2 bits to the left (padding a binary number with two zeroes). Doing this on paper, you would
typically write out the binary representation of the DSCP integer, then pad two zeroes on the right side of this 
binary string, and then mentally convert that new binary string back into an integer. Python makes quick work of 
this.  For example, type the code snippet `46 << 2` and press the `Enter` or `Return` key to make the conversion:
    
    ```
    >>> 46 << 2
    184
    >>>
    ```
    
    The Python operator `<<` executes a left bit-shift operation on the number to the left of the operator by the number
    of bits indicated to the right of the operator. In this example, we bit-shifted two bits to the left on DSCP 46, 
    leaving us with a ToS value of 184.

5.  To exit the interactive interpreter, type `quit()` and press the `Enter` or `Return` key to exit out of the 
interpreter, for example:
    
    ```
    >>>quit()
    $
    ```

#### Step 2: Running a Python Script

While the interactive Python interpreter is useful for occasional and instructional use, the majority of work with 
Python will be done by creating and running scripts. A Python script is a set of instructions written in a language 
that the Python interpreter understands. The script is written in a text editor and run against the Python interpreter.

1.  Make sure that your terminal still shows the prepended project name `(pythonenv)`. If it does not, then change to
your lab working directory and activate the Python virtual environment you created earlier in this lab with the
`source ~/lab/pythonenv/Scripts/activate` command, for example:
    
    ```
    $ source ~/lab/pythonenv/Scripts/activate
    (pythonenv) $
    ```

2.  Let's create a Python script with a little Bash shell code snippet using the shell built-in `echo` command and 
redirect the output to a file named `helloworld.py` with the `echo 'print("Hello World!")' >> ~/lab/helloworld.py` 
command, for example:
    
    ```
    (pythonenv) $ echo 'print("Hello World!")' >> ~/lab/helloworld.py
    (pythonenv) $
    ```

3.  Change to the director `~/lab` with the `cd ~/lab` command and run the Python script by with the command
`python helloworld.py`, for example:
    
    ```
    (pythonenv) $ cd ~/lab
    (pythonenv) $ python helloworld.py
    Hello World!
    (pythonenv) $
    ```

    By putting your Python instructions into a file, it can be called at any time by the Python interpreter.  This is 
    key to reusing code.

This is a basic tutorial to introduce the concepts necessary to interact with Python and execute Python applications.
There are countless introductory Python primers of all kinds in multiple mediums to help with the syntax of Python 
code.  This lab contains examples of Python code for real-world use cases for network programmability, but more can 
be found in GitHub.

Let's continue to learn more tools of the Ninja!

---

Navigation :: [Previous Page](LTRPRG-1100-02b4-Python-Ex3.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-02c1-Teams.md)
