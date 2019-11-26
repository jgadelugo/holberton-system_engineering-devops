# Design a three server web infrastructure that hosts the website www.foobar.com

## Must have
* 2 servers
* 1 web server (Nginx)
* 1 application server
* 1 application server
* 1 load-balancer (HAproxy)
* 1 set of application files (code base)
* 1 database (MySQL)

## Questions

* Why did we add each additional element?
    load balancer to handle traffic and another server so that we dont have a single point of failure there any more
* What distribution algorithm your load balancer is configured with and how it works?
    round robin  or static round robin or source?
* Is your load-balancer enabling an Active-Active or Active-Passive setup? Explain the difference.
 active-active is when both running at the same time equally distributing info
 active-passive only one at a time and the other goes on line when needed
* How a database Primary-Replica (Master-Slave) cluster works?
    Master can read and write and slave can only read
* What is the difference between the primary node and the Replica node in regards to the application


## What are the issues with this infrastructure?

* Where are SPOF?
    the load balancer
* Security isses? (no firewall, no HTTPS)
    no firewalls and https so user data is not safe
* no monitoring?
    monitoring catches possible errors or problems

[URL to design of a three server web infrastructure](https://imgur.com/a/U594TaV)
