Navigation :: [Previous Page](LTRPRG-1100-02a3-Git-Ex2.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-02b1-Python.md)

---

### Exercise 3: Cloning Remote Git Repositories

#### Objectives

The objectives for this exercise are to:

* Clone the remote Git repository for this lab

#### Step 1: Cloning the Remote Git Repository for this Lab

You do not need a GitHub account to download a working copy of a remote Git repository.  The `git clone` and 
`git pull` commands can be used to download a remote repository.  If you are only cloning and pulling 
updates from a remote repository, then you will next have to login to the remote Git server.

1.  Open the Git Bash terminal by double clicking the Git Bash icon on the desktop:
    
    ![Git Bash Icon](assets/GitBash-Icon.png)
    
    ![Git Bash Terminal](assets/GitBash-Term.png)

2. The `git pull` command will only work from inside a working directory that contains a Git repository hosted 
online in the first place.  Try this by moving to a directory that doesn't contain a `.git` Git directory.  Use the 
`cd ~/lab` command to change to a different directory and the `ls -la` command to confirm there is no directory named
`.git` present, for example:
        
    ```
    $ cd ~/lab
    $ ls -la
    total 16
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ./
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ../
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:19 clus19/
    $
    ```
3. Try the `git pull` command from this directory, for example:
    
    ```
    $ git pull
    fatal: Not a git repository (or any of the parent directories): .git
    $
    ```

4. To download a fresh copy of a remote repository to your local workstation, use the `git clone <repo URL>` command,
replacing `<repo URL>` with the URL to the remote Git repository.  The URL of a GitHub remote repository will be in 
the form of `https://github.com/<username>/<repo name>.git`.  For example if my `<username>` is `netprogninja` and my
repo name is `clus19`, the URL to my remote Git repository would be `https://github.com/netprogninja/clus19.git`.
    
    You can access this lab guide and all of the code and content for this lab from the GitHub repository
    [LTRPRG-1100](https://github.com/curtissmith/LTRPRG-1100) at `https://github.com/curtissmith/LTRPRG-1100` with a 
    webbrowser.  Let's clone this repository to your lab workstation with Git.  Use the `cd ~/lab` command to change 
    to the lab directory and run the `git clone https://github.com/curtissmith/LTRPRG-1100.git`
    command to clone the lab repository, for example:
    
    ```
    $ cd ~/lab
    $ git clone https://github.com/curtissmith/LTRPRG-1100.git
    Cloning into 'LTRPRG-1100'...
    remote: Counting objects: 117, done.
    remote: Compressing objects: 100% (84/84), done.
    remote: Total 117 (delta 51), reused 80 (delta 24), pack-reused 0
    Receiving objects: 100% (117/117), 86.75 KiB | 488.00 KiB/s, done.
    Resolving deltas: 100% (51/51), done.
    $ ls -la
    total 20
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:28 ./
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ../
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:19 clus19/
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:28 LTRPRG-1100/
    $ cd LTRPRG-1100
    $ ls -la
   total 18
    drwxr-xr-x 1 Administrator 197121    0 Jun  1 01:28 ./
    drwxr-xr-x 1 Administrator 197121    0 Jun  1 01:28 ../
    drwxr-xr-x 1 Administrator 197121    0 Jun  1 01:28 .git/
    -rw-r--r-- 1 Administrator 197121  848 Jun  1 01:28 ABSTRACT.md
    -rw-r--r-- 1 Administrator 197121  525 Jun  1 01:28 AGENDA.md
    -rw-r--r-- 1 Administrator 197121 1157 Jun  1 01:28 BIO.md
    -rw-r--r-- 1 Administrator 197121  325 Jun  1 01:28 README.md
    $
    ```
    
    Congratulations, you've cloned this lab's Git repository hosted online on GitHub!

This concludes the introduction to Git.  There are many resources online and at Cisco Live to help you become more 
proficient with revision control and Git.  Git is a powerful and essentual tool of the ninja and we will continue to 
use this tool to hone our skills throughout the rest of this lab.

---

Navigation :: [Previous Page](LTRPRG-1100-02a3-Git-Ex2.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-02b1-Python.md)
