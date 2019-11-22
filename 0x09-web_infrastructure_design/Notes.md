# High level notes for Web infrastructure project

## What it is and what it does

* **Server** is a physical machine, an actual computer, but in the Cloud era that could also be a virtual computer, generally called a vm. Typically held in datacenters which contain hundreds or thousands of computers that are accessible only by a network.

* **Web Server** is a software that delivers web pages.

* **Application Server** 

* **IP Port** are part of the addressing information used to identify the sender and receivers of messages. Allow different applications on the same computer to share network resources simultaneously

* **Database**

* **Code base** 

* **Load balancer** Distributes clients across multiple servers to handle many users. This increases the reliability, efficiency and availability of your enterprise application or website.

* **Load balancer algo**

*round robin* - This algo is the most commonly implemented. Uses each server in turn, according to their weights. Equally distributing processing time across all servers and dynamically adjusting the weights on the go.

*Static Round robin* - It is like round robin except it does not change the weight dynamically and it reintroduces servers immediately as servers go up and the full map is recomputed.

*Least Connections* - The server with the least connections reveives the connection. Recommended when very long sessions are expected. It is also dynamic.

* **IP Address** is the unique identifier for a computer

* **Network protocols** are sets of established rules that dictate how to format, transmit and receive data so computer network devices can communicate regardless of the differences in their underlying infrastructures, designs or standards

* **TCP/IP** (Transmission Control Protocol/Internet Protocol) is a suite of communication protocols used to interconnect network devices on the internet.

* **DNS** (Domain name system) is the technology that translates human-adapted, text-based domain names to machine adapted, numerical-based IP

#### resource records for DNS

* **A record** is used to find the IP address of a computer connected to the internet from a domain name (A stands for Address)

* **CNAME record** (Canonical Name record) maps one domain to another. This is good when running multiple services. Must always point to another domain name, never directly to an IP address

* **MX record** Specifies the mail server responsible for accepting email messages on behalf of a domain name. It is possible to configure several MX records, typically pointing to an array of mail servers for load balancing and redundancy

* **TXT** is used to provide the ability to associate arbitrary text with a host or other name, such as human readable information about a server, network, data center or other accounting information
