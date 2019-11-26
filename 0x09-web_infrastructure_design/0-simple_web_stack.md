# Design a one server web infrastructure that hosts the website www.foobar.com
## start your explanation by having a user wanting to access your website

## you must have
* 1 server
* 1 web server (Nginx)
* 1 application server
* 1 application file (code base)
* 1 database (MySQL)
* 1 domain name foobar.com configed with a www record that points to your server IP 8.8.8.8

## Questions

* What is a server?
    A server is a computer without a monitor.
* What is the role of the domain name?
    Human readable address to represent an IP Address
* What type of DNS record www is in www.foobar.com?
    A record!
* What is the role of the web server?
    Frontend show html and css
* What is the role of the application server?
    runs your base code
* What is the role of the database
    To pass data from storage to webserver through app server
* What is the server using to communicate with the computer of the user requesting the website
    The IP Address through the browser/internet

## What are the issues with this infrastructure?

* SPOF?
    Single point of failure the server itself
* Downtime when maintenace needed (like deploying new code web server needs to be restarted)?
    everything oges down
* Cannot scale if too much incoming traffic?
    No because no load balancer
[URL to design of one server web infrastructur](https://imgur.com/a/U594TaV)