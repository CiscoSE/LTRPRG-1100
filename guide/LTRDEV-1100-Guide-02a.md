Navigation - [Previous Page](LTRDEV-1100-Guide-02.md)

---

## Git and GitHub

TODO:

- [x] @curtissmith Draft "Tools of the Ninja - Git and GitHub"
- [x] Proofread
- [x] Add example output and screenshots

### Introducing Git and GitHub

[Git](https://git-scm.com/) is a free and open source distributed version control system.  It was designed to be 
lightweight, easy to learn, and capable to handle projects large and small alike.  Git has a small footprint and is 
very fast.

A version control system records and manages changes to files over time.  A version control system will have 
mechanisms that allow you to see the differences between versions and revert back to earlier versions of files being 
managed.  Generally speaking, most people's idea of version control is to create copies of files and archive them in 
a series of directories on their file system.  This is prone to error as one file copy mistake and you could 
lose a lot of work by mistake.  Also, this method rarely works when multiple people are modifying the same files at the
same time.
 
A Git repository, or repo for short, is a group of files that are tracked as a project.  A Git repository can reside on 
your computer, but the repository must be hosted on a server if two or more people are going to access the repository.  
[GitHub](https://github.com/) is the largest online host of Git repositories on the Internet.  GitHub also serves as 
a community for developers.  GitHub is free, but any repositories you create and host on GitHub with a free account must
be public.  Private repositories are supported with a [paid subscription account upgrade](https://github.com/account/upgrade).

### Exercise 1: Creating a GitHub Account

#### Objectives

The objectives for this exercise are to:

* Create a GitHub account
* Explore GitHub

#### Step 1: Creating a GitHub Account

Although creating a GitHub account is not required to clone Git repositories hosted on GitHub, why not join and 
participate in one of the largest developer communities on the Internet?  Doing so gives you the opportunity to see 
what other people are working on or are interested in, learn how software is built by following projects, and share 
your work - no matter how small - with the community.  Cisco product teams, Cisco DevNet, and Cisco SEs all share and
collaborate through GitHub.

1. Open a web browser and navigate to [GitHub](https://github.com/): `https://github.com/`.
2. On the GitHub homepage, fill out the form to [Sign up](https://github.com/join?source=header-home), choosing a 
unique username, entering your email adress, and creating a password.  Click the `Sign up for GitHub` button.
3. Choose the personal plan `Unlimited public repositories for free.`  Optionally click to select `Send me updates on
GitHub news, offers, and events`.  Click the `Continue` button.
4. Tailor your GitHub experience by answering the questions.  Click the `Submit` button.

Congratulations, you have joined the GitHub community!

#### Step 2: Exploring GitHub

1. Take a few minutes to follow new and interesting people:
    1. Search for and follow your Cisco Live lab proctors:
    [Curtis Smith](https://github.com/curtissmith) (`curtissmith`) and
    [Matthew Galazka](https://github.com/mgalazka) (`mgalazka`).
    2. Search for and follow your fellow Cisco Live lab participants.
2. Take a few minutes to discover new repositories:
    1. Search for and star the Cisco Live [LTRDEV-1100 session](https://github.com/curtissmith/LTRDEV-1100) repository.
    2. Search for and bookmark the [Cisco DevNet](https://github.com/CiscoDevNet) organization where sample code from
    Cisco DevNet is shared.
    3. Search for and bookmark the [Cisco Systems Engineers](https://github.com/CiscoSE) organization where sample 
    code from Cisco SE community is shared.

### Exercise 2: Introducing Git Concepts

#### Objectives

The objectives for this exercise are to:

* Understand key Git version control system concepts
* Introduce the basic Git commands

#### Step 1: Understanding Git Version Control Concepts

There is a simple flow to using Git for version control:

```
+----------------+      +---------+       +----------+
| Initialize or  |      |  Stage  |       |  Commit  |
|     Clone      +----->| Changes +------>|  Changes |
| Git Repository |      |         |       |          |
+----------------+      +---------+       +----------+
```

You start by either creating a new Git repository or cloning an existing Git repository hosted on a remote server.  In 
doing so, you create the Git directory (also called the repository), a working directory, and a staging area (also 
called the index).  The Git directory contains the metadata and object database and is copied from the server when 
a repository is cloned.  The working directory contains one version of the project copied to the file system 
from the compressed object database in the Git directory.  The staging area is a file inside the Git directory 
that contains an index of changes that are waiting to be committed.

Files that are changed but not staged are considered modified.  Files that are changed and added to the staging 
area are considered staged.  Files in the Git directory are considered committed.  In the next step, we will learn 
how to initialize and clone repositories, and modify, stage, and commit changes, and push those changes to GitHub.

#### Step 2: Learning Git Commands

Git has command line commands for managing Git repositories.  Here are the key commands and their usage you will need
to get started to participate in projects or manage your own projects.

1. For a complete list of Git commands, type `git help` (output truncated for brevity):
    
    ```
    $ git help    
    ```
    
    For more help with a specific Git command, type `git <command> -h`, for example `git clone -h` (output truncated 
    for brevity):
    
    ```
    $ git clone -h     
    ```
    
2. For first time Git setup, you should set your name and email address with the `git config` command.  Every commit 
you make includes this information, so it is important to set this after installing Git.  This should match the name 
and  email address you used to register on GitHub, for example:
    
    ```
    $ git config --global user.name "Curtis Smith"    
    $ git config --global user.email "curtissm@cisco.com"
    ```
    
3. To create your very first Git repository, create a Git working directory and initialize the repository with the 
command `git init`, for example:
    ```
    $ mkdir -p ~/lab/clus18
    $ cd ~/lab/clus18
    $ git init
    Initialized empty Git repository in C:/Users/Administrator/lab/clus18/.git/
    $
    ```
    
    Now take a look at the contents of the directory.  You will find a hidden directory named `.git`:
    
    ```
    $ ls -la
    $ ls -la
    total 4
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ./
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ../
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 .git/
    $
    ```
    
    The directory `~/lab/clus18` is your new Git working directory and `~/lab/clus18/.git` is your Git directory.  
    Your working directory (and consequently your Git directory) are empty as you've not staged or committed anything
    to the repository yet.
    
4. Let's confirm this is the case with the command `git status`:
    
    ```
    $ git status
    On branch master
    
    No commits yet
    
    nothing to commit (create/copy files and use "git add" to track)
    ```
    
    At any time you can invoke the `git status` command from inside your Git repository working directory to see 
    whether there are any staged changes or whether your copy of the repository is in sync with the remote server if 
    it is hosted online.
    
5. Let's create a new file to track:
    
    ```
    $ echo "# Hello World!" >> README.md
    ```
    
    and check the status:
    
    ```
    $ git status
    On branch master
    
    No commits yet
    
    Untracked files:
        (use "git add <file>..." to include in what will be committed)
    
	        README.md
    
    nothing added to commit but untracked files present (use "git add" to track)
    ```
    
    You can see that there is an unstaged file in your working directory.  Let's stage the file with the `git add` 
    command:
    
    ```
    $ git add README.md
    warning: LF will be replaced by CRLF in README.md.
    The file will have its original line endings in your working directory.
    $
    ```
    
    and the check the status again:
    
    ```
    $ git status
    On branch master
    
    No commits yet
    
    Changes to be committed:
        (use "git rm --cached <file>..." to unstage)
    
	        new file:   README.md
    
    $
    ```
    
    You can see there is a staged file in your working directory that is uncommitted.
    
6. Let's make your first commit to your first Git repository!  Use the `git commit` command to commit your staged 
changes:
    
    ```
    $ git commit -m "My first Git commit" README.md
    warning: LF will be replaced by CRLF in README.md.
    The file will have its original line endings in your working directory.
    [master (root-commit) d6cbb59] My first Git commit
     1 file changed, 1 insertion(+)
     create mode 100644 README.md
    $
    ```
    
    and check the status:
    
    ```
    $ git status
    On branch master
    nothing to commit, working tree clean
    $
    ```
    
    Congratulations, you've created your first Git repository and made your first commit to that repository!
    
7. Let's create a remote repository on GitHub and push our repository locally to the server.
    
    1. First, navigate to [Github](https://github.com/) `https://github.com/` and ensure you've logged in with the 
    account you created earlier.
    
    2. At the top right of the page, click the `+` and click `New Repository`.
    
    3. In the box labeled `Repository name` type `clus18`.
    
    4. You may add an optional `Description`, for example `My Cisco Live US 2018 Git repository`.
    
    5. Click the `Create repository` button.
    
    6. Now let's push your existing local repository to the new remote repository you've created on GitHub.  First, 
    use the `git remote add` command to add the local repository to the remote repository (replace the URL in the 
    example below with the URL of your new remote repository):
    
    ```
    $ git remote add origin https://github.com/curtissmith/clus18.git
    ```
    
    Second, push your local changes to the remote repository with the `git push` command:
    
    ```
    $ git push -u origin master
    Counting objects: 3, done.
    Writing objects: 100% (3/3), 234 bytes | 234.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/curtissmith/clus18.git
     * [new branch]      master -> master
    Branch 'master' set up to track remote branch 'master' from 'origin'.
    $
    ```
    
    and check the status:
    
    ```
    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.
    
    nothing to commit, working tree clean
    $
    ```
    
    You can further confirm that your local repository is in sync with your remote repository and chdeck for changes 
    with the `git pull` command:
    
    ```
    $ git pull
    Already up to date.
    $
    ```
    
    If there had been any remote changes that were not in your local Git directory, then those changes would have 
    been synchronized in your Git directory and copied to your working directory.
    
    Navigate to your remote repository on GitHub and you should see the results of your labor!

8. The `git pull` will only work from inside a working directory that contains a Git repository in the first place.  
Try this by moving to a directory that doesn't contain a `.git` Git directory, for example:
        
    ```
    $ cd ~/lab
    $ ls -la
    total 16
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ./
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ../
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:19 clus18/
    $ git pull
    fatal: Not a git repository (or any of the parent directories): .git
    $
    ```
        
    To download a fresh copy of a remote repository to your local workstation, use the `git clone` command.  For 
    example, you can access this lab guide and all of the code and content for this session from
    [GitHub](https://github.com/curtissmith/LTRDEV-1100) at `https://github.com/curtissmith/LTRDEV-1100`:
        
    ```
    $ cd ~/lab
    $ git clone https://github.com/curtissmith/LTRDEV-1100
    Cloning into 'LTRDEV-1100'...
    remote: Counting objects: 117, done.
    remote: Compressing objects: 100% (84/84), done.
    remote: Total 117 (delta 51), reused 80 (delta 24), pack-reused 0
    Receiving objects: 100% (117/117), 86.75 KiB | 488.00 KiB/s, done.
    Resolving deltas: 100% (51/51), done.
    $ ls -la
    total 20
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:28 ./
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ../
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:19 clus18/
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:28 LTRDEV-1100/
    $ cd LTRDEV-1100
    $ ls -la
   total 18
    drwxr-xr-x 1 Administrator 197121    0 Jun  1 01:28 ./
    drwxr-xr-x 1 Administrator 197121    0 Jun  1 01:28 ../
    drwxr-xr-x 1 Administrator 197121    0 Jun  1 01:28 .git/
    -rw-r--r-- 1 Administrator 197121  848 Jun  1 01:28 ABSTRACT.md
    -rw-r--r-- 1 Administrator 197121  525 Jun  1 01:28 AGENDA.md
    -rw-r--r-- 1 Administrator 197121 1157 Jun  1 01:28 BIO.md
    -rw-r--r-- 1 Administrator 197121  325 Jun  1 01:28 README.md
    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.
    
    nothing to commit, working tree clean
    $
    ```
    
    Congratulations, you've cloned a Git repository hosted on GitHub.

---

Navigation - [Next Page](LTRDEV-1100-Guide-02b.md)
