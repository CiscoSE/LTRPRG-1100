# Hone Your Ninja Skills

## Using APIs

TODO:

- [x] @mgalazka Draft "Hone Your Ninja Skills - Using APIs"

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pharetra risus a fringilla hendrerit. Nam venenatis metus quis risus aliquam mattis. Ut vitae elementum libero. Nam malesuada felis in tincidunt luctus. Aliquam ut magna orci. Nulla a elementum erat. Aenean facilisis, nibh at blandit feugiat, odio est tincidunt sem, eu pretium sem lorem vel libero. Nullam felis nisl, eleifend interdum congue aliquam, dictum sit amet augue. Maecenas vel augue justo. Quisque scelerisque tempus sapien, eu elementum nibh venenatis ac. In vel purus eu arcu elementum volutpat.

## Using NETCONF/YANG

TODO:

- [ ] @curtissmith Draft "Hone Your Ninja Skills - Using NETCONF/YANG"

### Introducing Model Driven Programmability

Model Driven Programmability...SNMP isn't good enough anymore...RFC-3535 and model driven programmability stack..
.Client/Server model...Transport Protocol/Data Model...NETCONF/YANG developed to address RFC-3535.

Traditional network device management techniques, for example command line interface (CLI) and web user interface 
(UI), were designed for human to machine interaction for configuring and accessing operational details.  They by 
definition are not programmable.  Although attempts at automation through screen scraping or imitating interactive 
sessions are possible, they are error prone, unrealiable, and do not scale.

The need for reliable and scalable ways to manage network devices is not a new one.  Simple Network Management Protocol 
(SNMP) was first introduced as a IETF Internet Standard in 1988 as a standard interface configure and retrieve 
operational information from network devices.  SNMP was revised over the years, chiefly to improve performance and 
security of the protocol.  However, SNMP still isn't adequate for the job today, relegated to polling statistics and 
status.

In 2003, the IETF published [RFC3535](https://tools.ietf.org/html/rfc3535) *Overview of the 2002 IAB Network 
Management Workshop*, stating

> SNMP works reasonably well for device monitoring.

and found to be lacking in the following ways:

* Applications are necessary for SNMP to useful
* Lack of writeable MIBs in general and writeable MIBs for configuration more specifically
* Does not scale
* Too difficult to implement
* Lack of support for configuration retrieval or playback
* Mismatch between SNMP data-centric view of the world versus an operator's task-oriented view of the world 

"Model driven programmability inherits the power of models, making it easier to configure routers. It overcomes 
drawbacks posed by traditional router management techniques.

The solution lies in using data models – a programmatic and standards-based way of writing configurations to any network device. Use it to replace the process of manual configuration and implement YANG as the de-facto data modeling language."

### Exercise 1: Introducing NETCONF

#### Objectives

The objectives for this exercise are to:

* Understand the NETCONF protocol stack
* Understand NETCONF operations
* Learn how to use Python to make NETCONF requests

#### Step 1: Understanding the NETCONF Protocol Stack

lorem ipsum

#### Step 2: Understanding NETCONF Operations

lorem ipsum

#### Step 3: Using Python to make NETCONF Requests

lorem ipsum

### Exercise 2: Introducing YANG

#### Objectives

The objectives for this exercise are to:

* Understand YANG as a language, data models, and data
* Explore the anatomy of a YANG data model
* Use pyang to explore data models

#### Step 1: Understanding the YANG language, YANG Data Models, and YANG Data

lorem ipsum

#### Step 2: Exploring the Anatomy of a YANG Data Model

lorem ipsum

#### Step 3: Using pyang to Explore YAND Data Models

lorem ipsum

### Exercise 3: Exploring IOS XE YANG Data Models with NETCONF

#### Objectives

The objectives for this exercise are to:

* Foo
* Bar

#### Step 1: Foo

lorem ipsum

#### Step 2: Bar

lorem ipsum

## Guest Shell

TODO:

- [ ] @curtissmith Draft "Hone Your Ninja Skills - Guest Shell"

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pharetra risus a fringilla hendrerit. Nam venenatis metus quis risus aliquam mattis. Ut vitae elementum libero. Nam malesuada felis in tincidunt luctus. Aliquam ut magna orci. Nulla a elementum erat. Aenean facilisis, nibh at blandit feugiat, odio est tincidunt sem, eu pretium sem lorem vel libero. Nullam felis nisl, eleifend interdum congue aliquam, dictum sit amet augue. Maecenas vel augue justo. Quisque scelerisque tempus sapien, eu elementum nibh venenatis ac. In vel purus eu arcu elementum volutpat.
