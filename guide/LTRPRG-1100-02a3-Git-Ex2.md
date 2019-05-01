Navigation :: [Previous Page](LTRPRG-1100-02a2-Git-Ex1.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-02b1-Python.md)

---

### Exercise 2: Introducing Git Concepts and Commands

#### Objectives

The objectives for this exercise are to:

* Understand key Git version control system concepts
* Introduce the basic Git commands
* Learn how to work with a local Git repository
* Learn how to work with a remote Git repository

#### Step 1: Understanding Git Version Control Concepts

There is a simple flow to using Git for version control:

```
+----------------+      +---------+       +----------+
| Initialize or  |      |  Stage  |       |  Commit  |
|     Clone      +----->| Changes +------>|  Changes |
| Git Repository |      |         |       |          |
+----------------+      +---------+       +----------+
```

You start by either creating a new Git repository or cloning an existing Git repository hosted on a remote server.
In doing so, you create the Git directory (also called the repository), a working directory, and a staging area (also 
called the index).  The Git directory contains the metadata and object database and is copied from the server when 
a repository is cloned.  The working directory contains one version of the project copied to the file system 
from the compressed object database in the Git directory.  The staging area is a file inside the Git directory 
that contains an index of changes that are waiting to be committed.

Files that are changed but not staged are considered modified.  Files that are changed and added to the staging 
area are considered staged.  Files in the Git directory are considered committed.  In the next step, we will learn 
how to initialize and clone repositories, and modify, stage, and commit changes, and push those changes to GitHub.

#### Step 2: Learning Git Commands

Git has command line commands for managing Git repositories.  Here are the key commands and their usage you will need
to get started using Git successfully.

Open the Git Bash terminal by double clicking the Git Bash icon on the desktop:

![Git Bash Icon](assets/Git-01.png)

![Git Bash Terminal](assets/Git-02.png)

1. For a list of common Git commands, type `git help`:
    
    ```
    $ git help
    usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
    
    These are common Git commands used in various situations:
    
    start a working area (see also: git help tutorial)
       clone      Clone a repository into a new directory
       init       Create an empty Git repository or reinitialize an existing one
    
    work on the current change (see also: git help everyday)
       add        Add file contents to the index
       mv         Move or rename a file, a directory, or a symlink
       reset      Reset current HEAD to the specified state
       rm         Remove files from the working tree and from the index
    
    examine the history and state (see also: git help revisions)
       bisect     Use binary search to find the commit that introduced a bug
       grep       Print lines matching a pattern
       log        Show commit logs
       show       Show various types of objects
       status     Show the working tree status
    
    grow, mark and tweak your common history
       branch     List, create, or delete branches
       checkout   Switch branches or restore working tree files
       commit     Record changes to the repository
       diff       Show changes between commits, commit and working tree, etc
       merge      Join two or more development histories together
       rebase     Reapply commits on top of another base tip
       tag        Create, list, delete or verify a tag object signed with GPG
    
    collaborate (see also: git help workflows)
       fetch      Download objects and refs from another repository
       pull       Fetch from and integrate with another repository or a local branch
       push       Update remote refs along with associated objects
    
    'git help -a' and 'git help -g' list available subcommands and some
    concept guides. See 'git help <command>' or 'git help <concept>'
    to read about a specific subcommand or concept.
    $
    ```
    
    For help with a specific Git command, use the `-h` command line argument: `git <command> -h`, replacing `<command>` 
    with a specific Git command.  For example, we know `help` is a git command from the previous example, so try `git
    help -h`:
    
    ```
    $ git help -h
    usage: git help [--all] [--guides] [--man | --web | --info] [<command>]

    -a, --all             print all available commands
    -g, --guides          print list of useful guides
    -c, --config          print all configuration variable names
    -m, --man             show man page
    -w, --web             show manual in web browser
    -i, --info            show info page
    -v, --verbose         print command description
    $
    ```
    
    Choose another Git command listed in the output of `git help`, for example `git status -h`:
    
    ```
    $ git status -h
    usage: git status [<options>] [--] <pathspec>...

    -v, --verbose         be verbose
    -s, --short           show status concisely
    -b, --branch          show branch information
    --show-stash          show stash information
    --ahead-behind        compute full ahead/behind values
    --porcelain[=<version>]
                          machine-readable output
    --long                show status in long format (default)
    -z, --null            terminate entries with NUL
    -u, --untracked-files[=<mode>]
                          show untracked files, optional modes: all, normal, no. (Default: all)
    --ignored[=<mode>]    show ignored files, optional modes: traditional, matching, no. (Default: traditional)
    --ignore-submodules[=<when>]
                          ignore changes to submodules, optional when: all, dirty, untracked. (Default: all)
    --column[=<style>]    list untracked files in columns
    --no-renames          do not detect renames
    -M, --find-renames[=<n>]
                          detect renames, optionally set similarity index
    --show-ignored-directory
                          (DEPRECATED: use --ignore=matching instead) Only show directories that match an ignore pattern name.
    --no-lock-index       (DEPRECATED: use `git --no-optional-locks status` instead) Do not lock the index
    $
    ```
    
    If you need more in depth help with a command, you can get more complete documentation with the `git help 
    <command>`, replacing `<command>` with a specific Git command.  For example, try `git help status` (output 
    truncated for brevity):
    
    ```
    $ git help status
    ```
    
    In Windows, this might open a web browser window and display the help contents.  In macOS and Linux, this will 
    display the help contents in the terminal window.  You can use the Up/Down arrow keys to scroll through the 
    help output.  To exit help if viewed in the terminal window, type the `q` key.
    
    The most used Git commands are:
    
    * `git status`
    * `git init`
    * `got clone`
    * `git commit`
    * `git pull`
    * `git push`
    
2. For first time Git setup, you should set your name and email address with the `git config` command.  Every commit 
you make includes this information, so it is important to set this after installing Git.  If you created a GitHub 
account, this should match the name and email address you used to register on GitHub.  If you did not create a GitHub
account, then you can use any name or email address you'd like.
    
    The `git config` command to set your name looks like this: `git config user.name "<First Last>"`.  The `user.name` 
    is a keyword option and should be typed exactly as shown in the example.  You would replace `"<First Last>"` with 
    your first and last name, for example `"Curtis Smith"`; be sure to include the double quotes.  Go ahead and set 
    set your name with the `git config` command:
    
    ```
    $ git config --global user.name "<First Last>"
    ```
    
    The Git `config` command to set your email address looks like this: `git config user.email "<user@example.com>"`. 
    The `user.email` is a keyword option and should be typed as shown in the example.  You would replace 
    `"<user@example.com>"` with your email address, for example: `"curtissm@cisco.com"`; be sure to include the double 
    quotes.  Go ahead and set your email address with the `git config` command:
    
    ```
    $ git config --global user.email "<email@example.com>"
    ```
    
    You only need to complete these steps once per Git installation.
    
#### Step 3: Learning to Work with Local Git Repositories

1. To create your very first Git repository, create a Git working directory and initialize the repository with the 
`git init` command, for example:
    
    ```
    $ mkdir -p ~/lab/clus19
    $ cd ~/lab/clus19
    $ git init
    Initialized empty Git repository in C:/Users/Administrator/lab/clus19/.git/
    $
    ```
    
    Now take a look at the contents of the directory.  You will find a hidden directory named `.git`:
    
    ```
    $ cd ~/lab/clus19
    $ ls -la
    total 4
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ./
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ../
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 .git/
    $
    ```
    
    The directory `~/lab/clus19` is the new Git working directory and `~/lab/clus19/.git` is the Git directory.  
    The working directory (and consequently the Git directory) are empty as you've not staged or committed anything
    to the repository yet.
    
2. Let's confirm this is the case with the command `git status`:
    
    ```
    $ git status
    On branch master
    
    No commits yet
    
    nothing to commit (create/copy files and use "git add" to track)
    ```
    
    At any time you can invoke the `git status` command from inside the Git repository working directory to see 
    whether there are any staged changes or whether your copy of the repository is in sync with the remote server if 
    it is hosted online.

3. Let's create a new file to track with the Linux `echo` command and redirect the output to a file names `README.md`:
    
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
    
    and check the status again:
    
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

4. Let's make your first commit to your first Git repository!  Use the `git commit` command to commit your staged 
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
    
#### Step 3: Learning to Work with Remote Git Repositories

So far, you've been working with a local repository that only exists on the developer workstation we've provided you 
for this lab.  At the end of this lab, the lab environment will be destroyed and you will lose all of your work.  
Working with remote repositories allows you to store your project on a server for easy retrieval from any location.  
GitHub is a hosted service in the Cloud, but organizations might choose to install GitGub Enterprise on-premise.  The 
process is the same regardless of which hosted solution you use.

1. If you created a GitHub account, let's create a remote repository on GitHub and push your local repository to the 
server.  If you did not create a GitHub account, then you may skip this step.
    
    First, navigate to [Github](https://github.com/) `https://github.com/` and ensure you've logged in with the 
    account you created earlier.
    
    At the top right of the page, click the `+` and click `New Repository`.
    
    ![Git New Repository](assets/Git-03.png)
    
    In the box labeled `Repository name` type `clus19`.
    
    You may add an optional `Description`, for example `My Cisco Live US 2019 Git repository`.
    
    ![Git New Repository](assets/Git-04.png)
    
    Click the `Create repository` button.
    
    Now let's push your existing local repository to the new remote repository you've created on GitHub.  First, 
    use the `git remote add` command to add the local files to the remote server destination.  Make sure to replace 
    `<username>` in the example below to match your username and `<reponame>` with the name of the remote repository 
    you just created.  For example: `https://github.com/curtissmith>clus19.git` if your username is `curtissmith` and
     your repository name is `clus19`.
    
    ```
    $ git remote add origin https://github.com/<username>/<reponame>.git
    ```
    
    Next, push your local changes to the remote repository with the `git push` command:
    
    ```
    $ git push -u origin master
    Counting objects: 3, done.
    Writing objects: 100% (3/3), 234 bytes | 234.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/curtissmith/clus19.git
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
    
    You can further confirm that your local repository is in sync with your remote repository and check for changes 
    with the `git pull` command:
    
    ```
    $ git pull
    Already up to date.
    $
    ```
    
    If there had been any remote changes that were not in your local Git directory, then those changes would have 
    been synchronized in your Git directory and copied to your working directory.
    
    Navigate to your remote repository on GitHub and you should see the results of your labor!
    
    ![GitHub Repository](assets/Git-05.png)
    
    Congratulations, you've created a new Git repository on GitHub.
    
2. You do not need a GitHub account to download a working copy of a remote Git repository.  The Git `clone` and 
`pull` commands can be used download a remote repository.  The `git pull` will only work from inside a working 
directory that contains a Git repository in the first place.  Try this by moving to a directory that doesn't contain a
 `.git` Git directory, for example:
        
    ```
    $ cd ~/lab
    $ ls -la
    total 16
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ./
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:16 ../
    drwxr-xr-x 1 Administrator 197121 0 Jun  1 01:19 clus19/
    $ git pull
    fatal: Not a git repository (or any of the parent directories): .git
    $
    ```
        
    To download a fresh copy of a remote repository to your local workstation, use the Git `clone` command.  For 
    example, you can access this lab guide and all of the code and content for this session from
    [GitHub](https://github.com/curtissmith/LTRPRG-1100) with the URL `https://github.com/curtissmith/LTRPRG-1100.git`:
        
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
    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.
    
    nothing to commit, working tree clean
    $
    ```
    
    Congratulations, you've cloned a Git repository hosted on GitHub.

---

Navigation :: [Previous Page](LTRPRG-1100-02a2-Git-Ex1.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-02b1-Python.md)
