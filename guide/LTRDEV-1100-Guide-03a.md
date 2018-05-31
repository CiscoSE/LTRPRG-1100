## Using APIs

TODO:

- [x] @mgalazka Draft "Hone Your Ninja Skills - Using APIs"
- [ ] Proofread
- [ ] Edit for directory, example output, and style consistency

### Importance of API's

As discussed earlier in the introduction to Postman, API's are a structured method of communicating with software. Information be queried (similar to a CLI 'show' command on a router) or changed (think of 'config t' on a router CLI) in a programmatic way. Not only can commands be run through a script, but the information returned from an API is often structured in a way that allows for parsing of data. This allows for someone to code in logical steps to be taken depending on the returned values. In other words, API's are the key to allowing code to interact with software, devices, and other external components, amplifying the possibilities of what can be accomplished.

### Exercise 1: Understanding and using API's

#### Objectives

The objectives of this exercise are to:
* Learn how to find API info
* Use the docs to make an API call
* Automate with a script

#### Step 1: Learn how to find API info

While there are standards that API's typically follow, the particular calls, parameters, and expected results differ with every API. From a commonality standpoint, many API's utilize the same architectural style called REST. REST, or Representational State Transfer, is based on core HTTP functions such as GET, POST, PUT, and DELETE. Beyond this, documentation is necessary to understand what functions are available via API. In this step, we will explore a number of different API's documentation, so you can start to formulate ideas around how each one could be utilized.

1. Let's quickly revisit the documentation for Webex Teams API. Its documentation is interactive and robust, so it is a great example to peruse. Open up the [Webex Teams Developer Site](https://developer.webex.com/getting-started.html) and spend a few minutes looking through the Teams API reference material.
    1. Which HTTP functions are available when working with the 'Rooms' area of the Teams API?
    2. What is the expected output for a well-formed request to list the rooms to which the user belongs?

2. Next, explore the developer information available at the [Cisco Meraki Dev site](https://create.meraki.io). This site contains reference documentation, code samples, and tutorials related to Cisco Meraki products. These API's allow you to programmatically utilize the meraki wireless access points, network switches, security appliances, and more.
    1. Click on the [Build](https://create.meraki.io/build/) menu along the top of the page. Which example sounds interesting to you? Spend a few minutes checking out the different examples. Pull up one in particular, using [Meraki API with Google Forms](https://create.meraki.io/build/google-forms-with-the-dashboard-api/). As you read through this, think about what goal is being accomplished? What other ways could the API with a form like this be leveraged? Maybe a firewall rule change request?
    2. From the top menu, select [Learn](https://create.meraki.io/learn/) to list different tutorials available. We do not have the time to dive into any of these right now, but these types of learning exercises can help bolster your understanding of the Meraki API.
    3. Explore the [Postman API Docs](https://create.meraki.io/postman) for a full reference of the available API functions. For instance, click on `Devices` and then `List the devices in a network` to see the details of this particular GET call. Click to expand the example response in the right-side column. Which of these fields may be interesting if you were building an inventory script?

3. Many Cisco products have consolidated API information at the [Cisco DevNet](https://developer.cisco.com/) site. This web portal contains a plethora of reference documentation, tutorials, learning labs, sandbox environments, etc. This is a great place to start for learning more about the topics discussed in this lab.

#### Step 2: Using the docs to make an API call

Content to be inserted from previous guide / Postman / Webex Teams

#### Step 3: Automate with a script

Should we keep this section?
