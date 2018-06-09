## Introducing Postman

TODO:

- [x] @mgalazka Draft "Tools of the Ninja - Other...Postman"
- [ ] Proofread
- [x] Update screenshots to match dCloud environment

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
API to query the router about these routes, the specific information being sought can be retrieved, parsed, and used 
to generate an alert.

As products continue to implement API's, possibilities of cross-product or cross-system integration become ever more 
popular. One example of this within Cisco is with pxGrid. This open API allows contextual information about security 
to be shared between cross-vendor security products to contain threats faster than the products could have 
accomplished on their own.

Many modern API's are RESTful API's, meaning that they follow HTTP methods and framework to exchange data.  While 
Postman is a full-featured and powerful toolset, it still provides a remarkably user-friendly experience as an API 
client. This functionality is helpful when working with products or services that offer a REST API. Postman can be a 
great first step to prototype the API call, and then subsequently understand how the response looks. Using this 
information, it becomes much easier to interact with the API programmatically.
