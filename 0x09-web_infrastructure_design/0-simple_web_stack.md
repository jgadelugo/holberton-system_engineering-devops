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

* What is the role of the domain name?

* What type of DNS record www is in www.foobar.com?

* What is the role of the web server?

* What is the role of the application server?

* What is the role of the database

* What is the server using to communicate with the computer of the user requesting the website


## What are the issues with this infrastructure?

* SPOF?

* Downtime when maintenace needed (like deploying new code web server needs to be restarted)?

* Cannot scale if too much incoming traffic?

[URL to design of one server web infrastructur](https://imgur.com/a/U594TaV)