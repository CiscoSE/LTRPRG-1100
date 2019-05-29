Navigation :: [Previous Page](LTRPRG-1100-03-Hone.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-03b1-REST.md)

---

## Application Programming Interfaces (APIs)

### Introducing APIs

As alluded to earlier in the introduction to Postman, APIs are a structured method of communicating with software. 
Information can be queried (similar to a CLI `show` command on a network device) or changed (think of `config t` on a 
network device CLI) in a programmatic way. Not only can commands be run through a script, but the information returned 
from an API is often structured in a way that allows for easy parsing or manipulation of data. This allows for someone
to code in logical steps to be taken depending on the returned values. In other words, APIs are the key to allowing
code to interact with software, devices, and other external components, amplifying the possibilities of what can be 
accomplished.

The benefits of utilizing APIs are in the way that the information can be consumed and processed, as well as the 
rate and control with which changes can be made. For example, imagine that you have a critical router and you want to
be alerted if a certain route or set of routes change or disappear from the routing table. Monitoring for this 
situation with traditional network management tools may prove difficult.  Using an API to query the router about 
these routes, the specific information being sought can be retrieved, parsed, and used to generate an alert.  The 
same APIs can be used to programmatically react to the alert, creating a new static route, shutting down a link, or 
some other action to automate the process of reacting to an error condition.

As products continue to implement APIs, possibilities of cross-product or cross-system integration become ever more 
popular. One example of this within Cisco is with pxGrid. This open API allows contextual information about security 
to be shared between Cisco and cross-vendor security products alike to contain threats faster than the products could 
have accomplished on their own.

Many modern APIs are RESTful APIs, meaning that they follow HTTP methods and framework to exchange data.  While 
Postman is a full-featured and powerful tool, it still provides a remarkably user-friendly experience as an API 
client. This functionality is helpful when working with products or services that offer a REST API. Postman can be a 
great first step to prototype the API call, and then subsequently understand how the response looks. Using this 
information, it becomes much easier to interact with APIs with Python or other programming languages.

Not all APIs are RESTful or use the HTTP application protocol for communication.  We're also going to introduce 
NETCONF for model driven programmability.  NETCONF is an IETF standard network management protocol that provides for 
interfacing with network device programmatically - an API.

Let's use the tools we've introduced earlier in this lab to hone your skills and get you on your way to using 
different APIs relevant to Cisco products and services in your own work and play.

---

Navigation :: [Previous Page](LTRPRG-1100-03-Hone.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: [Next Page](LTRPRG-1100-03b1-REST.md)
