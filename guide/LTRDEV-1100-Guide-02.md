# Tools of the Ninja

## Git and GitHub

TODO:

- [x] @curtissmith Draft "Tools of the Ninja - Git and GitHub"
- [ ] Proofread
- [ ] Add example output and screenshots

### Introducing Git and GitHub

[Git](https://git-scm.com/) is a free and open source distributed version control system.  It was designed to be 
lightweight, easy to learn, and capable to handle projects large and small alike.  Git has a small footprint and is 
very fast.

A version control system records and manages changes to files over time.  A version control system will have 
mechnisms that allow you to see the differences between versions and revert back to earlier versions of files being 
managed.  Generally speaking, most people's idea of version control is to create copies of files and archive them in 
a series of directories on their file system.  This is very error prone as one file copy mistake and you could 
overwrite a file by mistake.  Also, this method rarely works when multiple people are modifying the same files at the
 same time.
 
A Git repository, or repo for short, is a group of files that are tracked as a project.  A Git repo can reside on your 
computer, but the repository must be hosted on a server if two or more people are going to access the repository.  
[GitHub](https://github.com/) is the largest online host of Git repositories on the Internet.  GitHub also serves as 
a community for developers.  GitHub is free, but any repositories you create and host on GitHub must be public.  
Private repositories are supported with a [paid subscription account upgrade](https://github.com/account/upgrade).

### Exercise 1: Creating a GitHub Account

#### Objectives

The objectives for this exercise are to:

* Create a GitHub account
* Explore GitHub

#### Step 1: Creating a GitHub Account

Although creating a GitHub account is not required to clone Git repositories hosted on GitHub, why not join and 
participate in one of the largest developer communities on the Internet?  Doing so gives you the opportunity to see 
what other people are working on or are interested in, learn how software is built by following projects, and share 
your work - no matter how small - with the community.

1. Open a web browser and navigate to [GitHub](https://github.com/): `https://github.com/`.
2. On the GitHub homepage, fill out the form to [Sign up](https://github.com/join?source=header-home), choosing a 
unique username, entering your email adress, and creating a password.  Click the `Sign up for GitHub` button.
3. Choose the personal plan `Unlimited public repositories for free.`  Optionally click to select `Send me updates on
GitHub news, offers, and events`.  Click the `Continue` button.
4. Tailor your GitHub experience by answering the questions.  Click the `Submit` button.

Congratulations, you have joined the GitHub community!

#### Step 2: Exploring GitHub

1. Take a few minutes to [explore GitHub](https://github.com/explore).
2. Take a few minutes to follow new and interesting people:
    1. Search for and follow your Cisco Live lab proctors: [Curtis Smith](https://github.com/curtissmith) 
(`curtissmith`) and [Matthew Galazka](https://github.com/mgalazka) (`mgalazka`).
    2. Search for and follow your fellow Cisco Live lab participants.
3. Take a few minutes to discover new repositories:
    1. Search for and star the Cisco Live [LTRDEV-1100 session](https://github.com/curtissmith/LTRDEV-1100) repository.
    2. Search for the [Cisco DevNet](https://github.com/CiscoDevNet) repositories.

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
a repository is cloned.  The working directory contains one version of the project and are copied to the file system 
from the compressed object database in the Git directory.  The staging area is a file inside the Git directory 
contains an index of changes that are waiting to be committed.

Files that are changed but not staged are considered modified.  Files that are changed and added to the staging 
area are considered staged.  Files in the Git directory are considered committed.  In the next step, we will learn 
how to initialize and clone repositories, and modify, stage, and commit changes, and push those changes to GitHub.

#### Step 2: Learning Git Commands

Git has command line commands for managing Git repositories.  Here are the key commands and their usage you will need
 to get started to participate in projects or manage your own projects.

1. For a complete list of Git commands, type `git help` (output truncated for brevity):
    
    ```
    $ git help
    
    foo
    
    $
    ```
    
    For more help with a specific Git command, type `git <command> -h`, for example:
    
    ```
    $ git clone -h
     
    foo
     
    $
    ```
    
2. For first time setup, you should set your name and email address with the `git config` command.  Every commit you 
make includes this information, so it is important to set this after installing Git.  This should match the name and 
email address you used to register on GitHub, for example:
    
    ```
    $ git config --global user.name "Curtis Smith"
    
    foo
    
    $ git config --global user.email <curtissm@cisco.com>
    
    foo
    
    $
    ```
    
3. To create your very first Git repository, create a Git working directory and initialize the repository with the 
command `git init`, for example:
    ```
    $ mkdir -p ~/coding/ciscolive/helloworld
    $ cd ~/coding/ciscolive/hellowworld
    $ git init
    
    foo
    
    $
    ```
    
    Now take a look at the contents of the directory.  You find a hidden directory named `.git`:
    
    ```
    $ ls -al
    .		..		.git
    $
    ```
    
    The directory `~/coding/ciscolive/helloworld` is your new Git working directory and 
    `~/coding/ciscolive/helloworld/.git` is your Git directory.  Your working directory (and consequently your Git 
    directory) are empty as you've not staged or committed anything to the repository yet.
    
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
    $ echo "# Hello World" >> README.md
    $
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
    
6. Let's make your first commit to your first Git repository!  Use the `git commit` to commit your staged changes:
    
    ```
    $ git commit -m "My first Git commit"
    [master (root-commit) a2c0a25] My first Git commit
     1 file changed, 0 insertions(+), 0 deletions(-)
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
    
    3. In the box labeled `Repository name` type `helloworld`.
    
    4. You may add an optional `Description`, for example `My first Git repository`.
    
    5. Click the `Create repository` button.
    
    6. Now let's push your existing local repository to the new remote repository you've created on GitHub.  First, 
    use the `git remote add` command to add the local repository to the remote repository (replace the URL in the 
    example below with the URL of your new remote repository):
    
    ```
    $ git remote add origin https://github.com/curtissmith/helloworld.git
    $
    ```
    
    Second, push your local changes to the remote repository with the `git push` command:
    
    ```
    $ git push -u origin master
    Counting objects: 6, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (6/6), 455 bytes | 455.00 KiB/s, done.
    Total 6 (delta 0), reused 0 (delta 0)
    To https://github.com/curtissmith/helloworld.git
     * [new branch]      master -> master
    Branch 'master' set up to track remote branch 'master' from 'origin'.
    $
    ```
    
    and check the status:
    
    ```$ git status
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
    1. Try this by moving to a directory that doesn't contain a `.git` Git directory, for example:
        
        ```
        $ cd ~/coding/ciscolive
        $ ls -a
        .		..		helloworld
        $ git pull
        fatal: Not a git repository (or any of the parent directories): .git
        $
        ```
        
    2. To download a fresh copy of a remote repository to your local workstation, use the `git clone` command.  For 
    example, you can access this lab guide and all of the code and content for this session from [GitHub]
    (https://github.com/curtissmith/LTRDEV-1100) at `https://github.com/curtissmith/LTRDEV-1100`:
        
        ```
        $ git clone https://github.com/curtissmith/LTRDEV-1100
        Cloning into 'LTRDEV-1100'...
        remote: Counting objects: 117, done.
        remote: Compressing objects: 100% (84/84), done.
        remote: Total 117 (delta 51), reused 80 (delta 24), pack-reused 0
        Receiving objects: 100% (117/117), 86.75 KiB | 488.00 KiB/s, done.
        Resolving deltas: 100% (51/51), done.
        $ ls
        LTRDEV-1100	helloworld
        $ cd LTRDEV-1100/
        $ ls -a
        .		.git		AGENDA.md	README.md
        ..		ABSTRACT.md	BIO.md
        $ git status
        On branch master
        Your branch is up to date with 'origin/master'.
        
        nothing to commit, working tree clean
        $
        ```

## Ansible for Network Programmability

TODO:

- [ ] @curtissmith Draft "Tools of the Ninja - Git and GitHub"
- [ ] Proofread
- [ ] Add example output and screenshots

### Introducing Ansible

Easy button for network programmability...configuration management...

"Configuration management tools help manage infrastructure at scale. Consider the challenges of managing large data 
centers:

* Updating packages on thousands of virtual machines.
* Changing configuration files on hundreds of servers.
* Orchestrating a workflow such as the deployment of a new application to production across different data centers.
* Running multiple CLI commands on dozens of servers to retrieve operational data.

All of this is prone to various human error. As such, configuration management tools provide features that are useful
to solve problems such as these."

ad hoc across multiple hosts...simple task flow automation...workflow automation...

### Exercise 1: Foo

#### Objectives

The objectives for this exercise are to:

* Foo
* Bar

#### Step 1: Foo

loreum ipsum

#### Step 2: Bar

lorem ipsum

## Vagrant Up for Network Engineers

TODO:

- [x] @curtissmith Draft "Tools of the Ninja - Vagrant Up for Network Engineers"
- [ ] Proofread
- [ ] Add example output

### Introducing Vagrant Up for Network Engineers

[Vagrant](https://www.vagrantup.com/) is an Open Source tool for creating workflows to build and manage virtual 
machine environments.  Vagrant is developed and maintained by the San Francisco-based company [HashiCorp](https://www
.hashicorp.com/).  Vagrant is not just for software developers.  Developers, designers, DevOps engineers, and network
 engineers alike can use Vagrant to automatically provision consistent and disposable virtual environments that can be  
leveraged for application or scripting design, development, and testing.

You can use Vagrant to learn and test APIs, write and test scripts, and validate network device platform commands 
and configuration if the system you are interested can be virtualized.  Fortunately, many Cisco devices 
have been virtualized: IOS XE using the CSR 1000v image, NX-OS using the Nexus 9000v image, and IOS XR using the 
XRv image, to name a few.  Earn some developer street cred by learning how to "Vagrant Up"!

### Exercise 1: Introducing Vagrant

#### Objectives

The objectives for this exercise are to:

* Explain what problem Vagrant solves
* Introduce the basic Vagrant commands
* Explore a Vagrantfile

#### Step 1: Describing Vagrant

How many times have you said "It worked fine in the lab, I don't know why it won't work in production."?  Or how many 
times when troubleshooting an appication problem you've heard someone say "It worked fine in dev, I don't know whjy 
it won't work in prod."?  Network engineers oftentimes test configuration on their own test switch or router.  
Developers oftentimes develop and test code on their workstations.  But if your switch or or their workstation don't 
match production systems or environments, testing and development won't reflect reality and unfornsee issues may 
arise.  You need a lab environment that closely reflects your production network.  Developers need a dev environment 
that closely matches their production systems.  This is where Vagrant comes into play. 

Vagrant can be used to create virtual environments that closely, if not identically, match real-life, production 
environments.  Traditionally, building test dev environments was time consuming and could not be easily reproduced 
or replicated. With Vagrant, you can build a network programmability environment once that can create a virtual 
machine from basic templates called [boxes](https://www.vagrantup.com/intro/getting-started/boxes.html), customize 
the operating system, install required software, and more.  Vagrant manages virtualization platforms refered to as 
[providers](https://www.vagrantup.com/intro/getting-started/providers.html).

Instead of building or recreating a virtual machine from scratch every time you need a network programmability 
environment, Vagrant boxes provide a base image from which virtual machines can be cloned.  HashiCorp maintains and 
hosts third-party boxes online, but you may also use install a box from a local `.box` file you create yourself or 
obtain a trusted source or from a custom URL.

Vagrant by itself is not a virtualization platform and cannot start a virtual machine.  Instead, Vagrant provides a 
common and consistent command line interface to control and manage virtual machines running inside VirtualBox, 
VMware, Amazon Web Services, and more using the virtualization platforms' APIs.

This is not limited to commonly virtualized operating systems like Microsoft  Windows or Linux  distributions.  
Vagrant supports many guest and host operating systems.  Anything that can be run as a virtual machine in a supported  
Vagrant provider can be supported, including Cisco IOS XE, NX-OS, and IOS XR!

Take a brief moment to discover the publicly available [catalog of Vagrant boxes](https://app.vagrantup
.com/boxes/search).

#### Step 2: Learning Vagrant Commands

Regardless of the Vagrant provider used as the virtualization platform, Vagrant has common commands for initializing an 
environment, installing and uninstalling boxes, booting an environment, connecting to the virtual machine, powering 
down an environment, cleaning up an environment, and more.

1. For a complete list of Vagrant commands, type `vagrant -h` (output truncated for brevity):
    
    ```
    $ vagrant -h
    
    foo
    
    $
    ```

2. For more help with a specific Vagrant command, type `vagrant <command> -h`, for example:
    
    ```
    $ vagrant box -h
     
    foo
     
    $
    ```
    
3. Vagrant boxes are globally stored for the current user logged into the host system running Vagrant.  Boxes are 
never modified; boxes are cloned from the base image provided by the box.  If you manage multiple 
Vagrant projects that use the same Vagrant box, modifying a guest virtual machine in one environment will not affect 
a guest virtual machine in other environments.
    
    1. To list the locally stored boxes on your system, type `vagrant box list`, for example:
        
        ```
        $ vagrant box list
        
        foo
        
        $
        ```
    
    2. To download and install a Vagrant box from [HashiCorp's Vagrant Cloud box catalog](https://app.vagrantup
    .com/boxes/search), type `vagrant box add <box descriptor>`.  For example, to install the box named 
    `hashicorp/precise64`:
        
        ```
        $ vagrant box add hashicorp/precise64
        
        foo
        
        $
        ```
    3. To remove a Vagrant box altogether from your system, type `vagrant box remove <box descriptor>`.  For example,
     to uninstall the box downloaded in the previous example:
        
        ```
        $vagrant box remove hashicorp/precise64
        
        foo
        
        $
        ```
    
4. Every Vagrant environment needs initialized.  To initialize a new Vagrant environment, type `vagrant init`.  This 
will establish the current working directory as the environment root directory and create a Vagrantfile (more on 
Vagrantfiles in Step 3.).  For example, to create a directory `my_first_vagrant_env` and initialize a new Vagrant 
environment:
    
    ```
    $ mkdir my_first_vagrant_env
    $ vagrant init
    
    foo
    
    $
    ```
    
5. To start up the new Vagrant environment, type `vagrant up`, for example:
    
    ```
    $ vagrant up
    
    foo
    
    $
    ```
    
6. To connect to the virtual machine in your new environment, you have two options, depending on what is supported 
by the virtual machine cloned from the Vagrant box:
    
    1. To connect using SSH, type `vagrant ssh`, for example:
        
        ```
        $ vagrant ssh
        
        foo
        
        $
        ```
    
    2. To connect using RDP, type `vagrant rdp`.
    
7. To see the status of the Vagrant environment, type the command `vagrant status`, for example:
    
    ```
    $ vagrant status
    
    foo
    
    $
    ```
    
    This will show you the current, default machine status.  If there are multiple Vagrant environments running, then
     type the command `vagrant global-status` to see all virtual machine environments, for example:
     
     ```
     $ vagrant global-status
     
     foo
     
     $
     ```
     
8. There are several Vagrant commands to manage the state of a Vagrant environment:
    
    1. To suspend the Vagrant environment, type `vagrant suspend`.
    2. To resume the Vagrant environment, type `vagrant resume`.
    3. To shutdown the Vagrant environment, type `vagrant halt`.
    4. To restart the Vagrant environment and force Vagrant to re-load the Vagrantfile, type `vagrant reload`.
    5. When you are done with the Vagrant environment, you can delete everything and clean up the working directory 
    (leaving the Vagrantfile).  Be aware that you will lose changes to the virtual machine and environment.  To 
    delete the Vagrant environment, type `vagrant destroy`, for example:
        
        ```
        $ vagrant destroy
        
        foo
        
        $
        ```
    
    Each of these commands can take the virtual machine ID or name as listed in the output of the command `vagrant 
    global-status` as an argument to specify a specific virtual machine if you have multiple machines running on your 
    system.  For example, if you want to destroy a specific virtual machine with machine ID `1a2b3c4d`, then type the
     command `vagrant destroy 1a2b3c4d`.

#### Step 3: Exploring a Vagrantfile

Every Vagrant environment or project requires a [Vagrantfile](https://www.vagrantup.com/docs/vagrantfile/).  The 
most basic reason for requiring a Vagrantfile is to describe the type of virtual machine and how to configure and  
provision the virtual machine.  The Vagrantfile is called a Vagrantfile because that is also the filename 
`Vagrantfile`.  Only one Vagrantfile is needed per Vagrant project environment.  The Vagrantfile should be managed 
in a version control system (such as Git and Github, which you will learn about later in this lab) so that your 
peers can check out the Vagrantfile for an environment and simply `vagrant up` to get the environment up and running.
 
The syntax of a Vagrantfile is the [Ruby](http://www.ruby-lang.org/en/) programming language, but it is not necessary 
have an understanding of Ruby to edit a Vagrantfile.  Let's take a look at the default Vagrantfile that is created 
for you when you run the command `vagrant init hashicorp/precise64`:

    # -*- mode: ruby -*-
    # vi: set ft=ruby :
    
    # All Vagrant configuration is done below. The "2" in Vagrant.configure
    # configures the configuration version (we support older styles for
    # backwards compatibility). Please don't change it unless you know what
    # you're doing.
    Vagrant.configure("2") do |config|
      # The most common configuration options are documented and commented below.
      # For a complete reference, please see the online documentation at
      # https://docs.vagrantup.com.
    
      # Every Vagrant development environment requires a box. You can search for
      # boxes at https://vagrantcloud.com/search.
      config.vm.box = "hashicorp/precise64"
    
      # Disable automatic box update checking. If you disable this, then
      # boxes will only be checked for updates when the user runs
      # `vagrant box outdated`. This is not recommended.
      # config.vm.box_check_update = false
    
      # Create a forwarded port mapping which allows access to a specific port
      # within the machine from a port on the host machine. In the example below,
      # accessing "localhost:8080" will access port 80 on the guest machine.
      # NOTE: This will enable public access to the opened port
      # config.vm.network "forwarded_port", guest: 80, host: 8080
    
      # Create a forwarded port mapping which allows access to a specific port
      # within the machine from a port on the host machine and only allow access
      # via 127.0.0.1 to disable public access
      # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
    
      # Create a private network, which allows host-only access to the machine
      # using a specific IP.
      # config.vm.network "private_network", ip: "192.168.33.10"
    
      # Create a public network, which generally matched to bridged network.
      # Bridged networks make the machine appear as another physical device on
      # your network.
      # config.vm.network "public_network"
    
      # Share an additional folder to the guest VM. The first argument is
      # the path on the host to the actual folder. The second argument is
      # the path on the guest to mount the folder. And the optional third
      # argument is a set of non-required options.
      # config.vm.synced_folder "../data", "/vagrant_data"
    
      # Provider-specific configuration so you can fine-tune various
      # backing providers for Vagrant. These expose provider-specific options.
      # Example for VirtualBox:
      #
      # config.vm.provider "virtualbox" do |vb|
      #   # Display the VirtualBox GUI when booting the machine
      #   vb.gui = true
      #
      #   # Customize the amount of memory on the VM:
      #   vb.memory = "1024"
      # end
      #
      # View the documentation for the provider you are using for more
      # information on available options.
    
      # Enable provisioning with a shell script. Additional provisioners such as
      # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
      # documentation for more information about their specific syntax and use.
      # config.vm.provision "shell", inline: <<-SHELL
      #   apt-get update
      #   apt-get install -y apache2
      # SHELL
    end

Let's break this down; it is acutally much simpler than it might appear.

1. The line `# -*- mode: ruby -*-` simply indicates that the Vagrantfile is written in the Ruby language syntax.  
This line is required and should always be the first line of the Vagrantfile.
    
2. Throughout the Vagrantfile, you will find lines that begin with a `#`.  These are comments and are ignored by 
Vagrant but provide you with guidance and allow you to document your Vagrantfile for clarity.  Nearly the entire 
Vagrantfile is comments.

3. If we remove the comments, we are just left with three lines of actual Vagrantfile configuration:
    
    ```
    Vagrant.configure("2") do |config|
      config.vm.box = "hashicorp/precise64"
    end
    ```
    
    In fact, these three lines are all that are really required to bring up a virtual machine environment.
    
     1. `Vagrant.configure("2") do |config|` is the syntax to indicate that this is a configuration for Vagrant 
        version 2.  
     2. `config.vm.box = "hashicorp/precise64"` is the syntax to specify the Vagrant box used to clone and boot 
        the virtual machine.  The box descriptor would be changed based on the box you choose.
     3. `end` indicates the end of the configuration.
        
    All other configuration of the environment uses the defaults from Vagrant and VirtualBox.

## Python for Network Programmability

TODO:

- [ ] @mgalazka Draft "Tools of the Ninja - Python for Network Programmability"

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pharetra risus a fringilla hendrerit.

## Other Desktop Network Programmability Tools

TODO:

- [ ] @mgalazka Draft "Tools of the Ninja - Other...Postman"
- [ ] @mgalazka Draft "Tools of the Ninja - Other...Webex Teams"
- [ ] @curtissmith Draft "Tools of the Ninja - Other...PyCharm"

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pharetra risus a fringilla hendrerit.
