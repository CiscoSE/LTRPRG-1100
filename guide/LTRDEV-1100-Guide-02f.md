Navigation - [Previous Page](LTRDEV-1100-Guide-02e.md)

---

### Introducing Postman

TODO:

- [x] @mgalazka Draft "Tools of the Ninja - Other...Postman"
- [ ] Proofread
- [ ] Update screenshots to match dCloud environment

[Postman](https://www.getpostman.com/) is a development environment focused specifically on working with application 
programming interfaces (API's). An API is a well-defined structure that allows communication between different pieces
of software. Many network engineers are aware that a Cisco Nexus switch has a command line interface where users can
type well-defined commands and receive expected output. Some may be surprised to learn that the same Nexus switch 
also has an API interface where users can send specific queries and receive structured responses ideal for 
programmatic consumption.

The benefits to utilizing API's are in the way that the information can be consumed and processed, as well as the 
rate and control with which changes can be made. As an example on the information processing side, imagine that you 
have a critical router and you want to be alerted if a certain route or set of routes change or disappear from the 
routing table. Monitoring for this situation with traditional network management tools may prove difficult.  Using an 
API to query the router about these routes, the specific information being sought can be retreived, parsed, and used 
to generate an alert.

As products continue to implement API's, possibilities of cross-product or cross-system integration become ever more 
popular. One example of this within Cisco is with pxGrid. This open API allows contextual information about security 
to be shared between cross-vendor security products to contain threats faster than the products could have 
accomplished on their own.

Many modern API's are RESTful API's, meaning that they follow HTTP methods and framework to exchange data.  While 
Postman is a full-featured and powerful toolset, it still provides a remarkably user-friendly experience as an API 
client. This functionality is helpful when working with products or services that offer a REST API. Postman can be a 
great first step to prototype the API call, and then subsequently understand how the resposne looks. Using this 
information, it becomes much easier to interact with the API programmatically.

### Exercise 1: Learn Postman Basics

#### Objectives

The objectives for this exercise are to:

* Become familiar with the layout of Postman
* Understand how to make an API call
* Analyze the results of an API call

#### Step 1: Becoming Familiar with Postman Layout

Postman is organized in three main sections: the header bar, the side bar, and the build area. The header bar is 
located at the top and provides access to common administrative tasks: creating new requests, importing data, 
changing settings, and so forth. The side bar is on the left side and it contains a history of requests made, as well
as a section titled, "Collections," which we will look at in a later exercise. The build area is the majority of the
screen real estate in the Postman app, and it is where you can build and send API requests.

![Postman Layout](assets/postman-01.png)

1. Locate the method dropdown at the top of the build area. This allows you to select the type of API request to 
make, such as an HTTP GET, PUT, POST, and so on. For our introductory lesson, please select `GET` as the method.

2. Next to the method dropdown, notice the field to input a URL. This is the web location for the API with which you 
want to interact. Immediately to the right of this URL is a button to add parameters to the URL. These are akin to 
appending the URL with key/value pairs via `?myvariable=1&another=2` syntax often noted at the end of web URLs.

3. Just below the URL field, there are a few more options to define the request. For instance, you can define headers
with the request. This is common with web requests in general. For instance, this is the method by which your mobile
phone's web browser can indicate that it is a mobile device, and hence you get the mobile version of a web page 
automatically. With API's it is important as well; often times authentication keys, data formats, and more can be 
defined in headers.

4. The bottom half of the build area is where the response from the API requests is displayed. This will show the 
response code, the time to receive a response, and details of the response including any body and headers.

#### Step 2: Making an API call

1. In order to make an API call, we first have to select the HTTP method. 
    
    Three of the most common methods used in API calls are `GET`, `POST`, and `PUT`. `GET` is used when getting 
    information from an API. A `GET` request specifies the information in which it is interested via the URL, 
    parameters, and headers. A `POST` request is one that is sending information to the API. This is often in the 
    form of creating a new data entry of some sort through the API. Lastly, the `PUT` is often used to update 
    existing information through the API.
    
    In our example, we will be making a `GET` request, so please make sure this is the method selected.

2. Now that we know we will be making a request for information, we need a location to find the API we are querying. 
Please specify the URL as `https://postman-echo.com/get` in the URL field. We do not require any parameters for this API.

3. Click `Send` and watch for the response. If successful, the `Status` should return `200 OK` which means that the 
request was accepted by the API.

#### Step 3: Analyzing the Results

![Postman results](assets/postman-02.png)

1. After verifying the important response code is `200 OK` we can start to dig into the other components of the 
response. Notice the body of the response that is shown below. The response is a set of data displayed in the JSON format of key/value pairs. 

2. Aside from the body of the response, there are also headers that give information about the response. For 
instance, the header `Content-Type` specifies `application/json` as its value. This data is important if working with
API's programmatically, as JSON formatted data would be parsed differently than, say, XML formatted data.
    
    ![Postman result headers](assets/postman-03.png)
    
### Exercise 2: Working in Postman

#### Objectives

The objectives for this exercise are to:

* Learn how and why to create a Collection
* Save variables in an Environment
* Use Postman to generate a Python script

#### Step 1: Creating a Collection

In Postman, Collections allow you to save similar requests together for easy access. Imagine a situation where you 
are learning how to use a particular product or service API. More often than not, there may be more than one request necessary.

For instance, if you are working with the Cisco Meraki dashboard API, you may need to save several different API 
calls in order to replicate the work later, or reference them to use in a script. The Cisco Meraki dashboard API 
first call may be to list the organizations of which you are a member. Next, another GET request may be to list the 
networks available in an organization. After this, you may make another call to list the devices that belong to a particular network.

As you can see, utilizing multiple tabs in the build area becomes important, and furthermore, saving the requests to 
reference later is very helpful. Let's look at how to make a Collection in Postman to save related requests.

1. Ensure that you still have the `postman-echo.com` GET request tab open. If you previously closed it without saving
it, please revisit the last exercise to re-create it.

2. On the far right side of the build area, click the dropdown icon next to `Save` and then click `Save As...`
    
    ![Postman Save](assets/postman-04.png)
    
3. In the `Save Request` box that pops up, note that the lower portion of the screen allows you to search for, 
select, or create a new collection. Click `+Create Collection` and then type in `LTRDEV-1100` as the new collection 
name. Click the checkbox to fully create the collection, and then click on the newly created collection to select it.
Now, click `Save to LTRDEV-1100` to save this request.
    
    ![Postman Create Collection](assets/postman-05.png)
    
    You can use this technique in the future to save API requests as you are working on them. When managing network 
    infrastructure that has fully featured API's, a collection could even be the ordered list of requests necessary 
    to complete a controlled change during a maintenance window. 

#### Step 2: Saving variables using Environments

When working with a particular API or set of API's pertaining to the same project, often times there are some 
variables that end up being re-used. For instance, you may be using the same authentication token on every request 
made. Or, perhaps all API calls are being made to the same domain name, even if the rest of the URI is different. The
domain name can be saved in a variable named 'domain' and then referenced with `{{domain}}` in the request builder.

This ability to define and use variables is helpful for a few reasons. First, it is more efficient to define it once 
and then use it many times. Second, since the variable is defined once in one place, it is less likely to suffer from
an inadvertent mistake in one place. And third, as we can save these variables into named groups called 
`Environments` we can set up multiple profiles for different users or API environments.

While variables can be created and saved in multiple scopes within Postman, we will focus on Environments. An 
environment is a set of key/value pairs (variables), and it can be quickly toggled for a particular request.  This 
would allow you to easily change between a test environment and a QA environment, for instance, with the appropriate 
tokens, URL's, etc for each.

1. First, create a new environment. To do this, click the dropdown for `+ New` in the upper left corner of Postman, 
and then select `Environment`.
    
    ![Postman new menu](assets/postman-06.png)
    
2. In this new dialog box, we can name the environment `LTRDEV-1100` and define a variable. Using our basic API 
request example from before, create a variable named `domain` and define the value as `postman-echo.com`.  Click Add 
to save the environment.
    
    ![Postman new environment](assets/postman-07.png)
    
3. Now that our environment is defined, let's enable it for use with a new request. near the upper right portion of 
the app, there is a dropdown selection box that shows the active environment. This will likely read `No Environment` 
at this point. Click the drop-down and select `LTRDEV-1100` as the environment to use.
    
    ![Postman select environment](assets/postman-08.png)
    
4. Let's create an API request using the variable defined in this environment (tip: if you need a quick reference to 
a variable name or value, click the "eye" icon immediately to the right of the active environment drop-down menu). In
 a new request tab, ensure the method is set to `GET` and enter the URL: `https://{{domain}}/get` and then click `Send`.
    
    ![Postman request with variable](assets/postman-09.png)
    
5. Notice that the request completed with a status of `200 OK` to the API at postman-echo.com. Also notice that if 
you mouseover the variable in the request URL, Postman will popup a box showing the variable is an environment 
variable as well as its value.

#### Step 3: Generating a Python script from Postman

While Postman is a very useful tool to when developing API requests, and can also be used in an ad-hoc way to 
prescriptively make API calls, often times it is helpful to run the API call in a script. This allows for much 
greater flexibility in the way requests are made, and also how results are processed.

Postman makes this process easy, as it can auto-generate code to use in a script.

1. In Postman, open the request from your LTRDEV-1100 collection. Then click on `Code` just underneath the `Send` and
`Save` buttons.
    
    ![Postman code select](assets/postman-10.png)
    
2. Ensure that the language in the upper left dropdown is set to `Python Requests`. In this window, it shows Python 
code necessary to execute this API call directly from a Python script. As a matter of fact, you can `Copy to 
Clipboard` and paste this into PyCharm to test it out.
    
    ![Postman code gen](assets/postman-11.png)

---

Navigation - [Next Page](LTRDEV-1100-Guide-02g.md)
