Navigation - [Previous Page](LTRDEV-1100-Guide-03.md)

---

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
    3. Which request should be used to pull information about people, specifically your own account?

#### Step 2: Making an API call

1. Let's take a look at how we can make an API call based on what we've read in the Teams API. Reference the [People](https://developer.webex.com/resource-people.html) section of the Webex Teams documentation.

2. Open up Postman and start filling in the details for a new request. Set the `Method` to `GET`.

3. Insert the following URL for the request: https://api.ciscospark.com/v1/people/me

4. Click on `Headers` to set the proper authorization for Webex Teams. The first header should have the key `Authorization` and its value should be set to `Bearer XYZ` where XYZ is replaced with your token. If you recall, the Webex Teams token should be open in a notepad window on your desktop. If not, you can access it again by clicking [here](https://developer.webex.com/getting-started.html#authentication).

5. Create a second header, with a key of `Content-Type` and a value of `application/json`, as shown in the documentation.

    ![Postman setup](assets/postman-12.png) 

6. Go ahead and hit `Send` in Postman to observe the results! If all goes well, you should be greeted with a `200 OK` status and a body of JSON-formatted key-value pairs.


#### Step 3: Automate with a script

When working with API's in postman, it is trivial to turn your API request into Python code. This can provide the basis to wrap scripting logic around the request. For instance, maybe you want to repeat 'people' info as we just did, but with a set of users. This code snippet can become the basis to facilitate automation.

1. In your already-open tab for getting your own details in Webex teams, click the `Code` button just below the `Save` button on the right side of the screen.

    ![Code button](assets/postman-13.png)

2. Select Python -> Requests from the upper left language dropdown. This presents code that can be copied to the clipboard and pasted in a file to run with the python interpreter. Easy as that!

    ![Code](assets/postman-14.png)


---

Navigation - [Next Page](LTRDEV-1100-Guide-03b.md)
