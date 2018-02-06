# Space-based

### Problem

> "As an architect, a lot of the time we are faced with highly-scalable systems. Either existing or new ones that we're creating."

<img src="../assets/basic-app-architecture.png" alt="Basic Web App"/>

In the image above, we have a browser that hits a web server that hits a db...very run-of-the-mill basic flow for a web app.

The problem we run into is that we are overloading our web server with requests and, therefore, our response times will decrease rapidly.<br>
What do we do in this situation? We need to add more web servers...

<img src="../assets/basic-app-scaled-web-server.png" alt="Scaled Web Server"/>


The problem we run into now is that multiple requests are coming into the **1** app server from multiple web servers causing the bottle neck.<br>
What do we do in this situation? You guessed it, need to add more app servers...

<img src="../assets/basic-app-scaled-app-server.png" alt="Scaled App Server"/>

So now we are getting the throughput we want but now we hit the database...<br>
*Scaling out a web server?* Piece of cake.<br>
*Scaling out an app server?* Bit harder and more expensive but doable...<br>
*Scaling out a database?* Mmmmm...very costly in money and time<br>

You'll notice that from the images above, even if you can scale the db a little, the db will **always** be your bottleneck.

If we had infinite resources *(money/time)*, can we solve this problem? We can have infinite web servers, we can have infinite app servers but can we have infinite data?
...
..
.
Ofourse we can!! And it's called **Space-based Architecture**

### Solution *(space-based)*

The image below lays out the components of a *space-based architecture*

<img src="../assets/space-based-architecture.png" alt="Spaced-based architecture"/>

#### Components

##### Processing Unit

 - The core of our application
 - We can have infinite of these
 - It's a term in this pattern which really just means "the application"
 - It's filled with *standalone modules*
 - Has its own internal *in memory data*
 <small>><i>(and a persistent data store with that - optional)</i></small>
 - Also has a *data replication engine* so when data comes in, it's able to put in memory and then asynchronously put it off to the persistent data store

##### Virtualised middleware

 - *Messaging grid* is responsible for controlling session data/requests and where it goes *(load balancing basically...)*
 - *Data grid* is reponsible for data replication between *Processing Units* because what we **don't** have in this pattern is a centralised data store
 <small>><i>(In theory the above is true as it is not part of the pattern, in practice you typically do though...as if all *Processing Unit*s go down, you still need a centralised copy of the data. The data grid here will then control the replication between in memory data <br>and</b> keep the centralised store up-to-date)</i></small>
 - *Processing grid* is responsible for managing parallel process requests. Gnerally, in a highly-scalable environment, the request may not be going to just 1 *Processing Unit*. A request will come in and the *Processing grid* can say, "Wow! I can split that data/request into these 2 *Processing Units*". Therefore, I am now not getting only the scalability but the performance as well
 - By the way, the sending of data/requests to *Processing Units* is **asynchronous** even though it is drawn in a synchronous manner above
 - *Deployment manager* is reponsible for managing the dynamic *Processing Unit* deployment...
 <small>><i>("Okay I can kill that one, kill that one, ooo bring that one online..." - get it?)</i></small>

### Considerations

 - All about variable scalability
 <small>><i>(When demand is high, like in-play betting, bring online more *Processing Unit*s...when demand is low, you can take out those uneeded *Processing Unit*s)</i></small>
 - Good for applications that have variable load or inconsistent peak times
 - Not a good fit for traditional large-scale relational database systems
 - Relativley complex and expensive pattern to implement
