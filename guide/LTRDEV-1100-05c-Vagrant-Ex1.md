Navigation :: [Previous Page](LTRDEV-1100-05b-Postman.md) :: [Table of Contents](LTRDEV-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRDEV-1100-05c-Vagrant.md)

### Exercise 1: Introducing Vagrant

#### Objectives

The objectives for this exercise are to:

* Explain what problem Vagrant solves
* Introduce the basic Vagrant commands
* Explore a Vagrantfile

#### Step 1: Describing Vagrant

How many times have you said "It worked fine in the lab, I don't know why it won't work in production."?  Or how many 
times when troubleshooting an application problem you've heard someone say "It worked fine in dev, I don't know why 
it won't work in prod."?  Network engineers oftentimes test configuration on their own test switch or router.  
Developers oftentimes develop and test code on their workstations.  But if your switch or or their workstation don't 
match production systems or environments, testing and development won't reflect reality and unforeseen issues may 
arise.  You need a lab environment that closely reflects your production network.  Developers need a dev environment 
that closely matches their production systems.  This is where Vagrant comes into play. 

Vagrant can be used to create virtual environments that closely, if not identically, match real-life, production 
environments.  Traditionally, building test dev environments was time consuming and could not be easily reproduced 
or replicated. With Vagrant, you can build a network programmability environment once that can create a virtual 
machine from basic templates called [boxes](https://www.vagrantup.com/intro/getting-started/boxes.html), customize 
the operating system, install required software, and more.  Vagrant manages virtualization platforms referred to as 
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

Take a brief moment to discover the publicly available
[catalog of Vagrant boxes](https://app.vagrantup.com/boxes/search).

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
    
    To list the locally stored boxes on your system, type `vagrant box list`, for example:
    
    ```
    $ vagrant box list
    
    foo
    
    $
    ```
    
    To download and install a Vagrant box from [HashiCorp's Vagrant Cloud box catalog](https://app.vagrantup
    .com/boxes/search), type `vagrant box add <box descriptor>`.  For example, to install the box named 
    `hashicorp/precise64`:
    
    ```
    $ vagrant box add hashicorp/precise64
    
    foo
    
    $
    ```
    
    To remove a Vagrant box altogether from your system, type `vagrant box remove <box descriptor>`.  For example,
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
    
    * To suspend the Vagrant environment, type `vagrant suspend`.
    * To resume the Vagrant environment, type `vagrant resume`.
    * To shutdown the Vagrant environment, type `vagrant halt`.
    * To restart the Vagrant environment and force Vagrant to re-load the Vagrantfile, type `vagrant reload`.
    * When you are done with the Vagrant environment, you can delete everything and clean up the working directory 
    (leaving the Vagrantfile).  Be aware that you will lose changes to the virtual machine and environment.  To 
    delete the Vagrant environment, type `vagrant destroy`.
    
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

Let's break this down; it is actually much simpler than it might appear.

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
    
    * `Vagrant.configure("2") do |config|` is the syntax to indicate that this is a configuration for Vagrant 
    version 2.  
    * `config.vm.box = "hashicorp/precise64"` is the syntax to specify the Vagrant box used to clone and boot the 
    virtual machine.  The box descriptor would be changed based on the box you choose.
    * `end` indicates the end of the configuration.
        
    All other configuration of the environment uses the defaults from Vagrant and VirtualBox.
Navigation :: [Previous Page](LTRDEV-1100-05b-Postman.md) :: [Table of Contents](LTRDEV-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRDEV-1100-05c-Vagrant.md)

