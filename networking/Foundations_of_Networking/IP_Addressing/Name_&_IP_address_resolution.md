# Name & IP address resolution

This section is about explaining different name & IP resolution techniques and how they work.

Contents:

+ [DHCP](#dhcp)
+ [WINS](#wins)
+ [NAT](#nat)
+ [DNS](#dns)

### DHCP *(Dynamic Host Configuration Protocol)*

The image below shows the DHCP initiatlisation process.<br>
This process occurs when a new client is added to the network and DHCP is enabled.

<img src="../assets/dhcp-initialisation-process.jpeg" alt="DHCP Initialisation Process"/>

**Steps:**

1.  *DHCP Discover:* The client issues a this request which is picked up by any DHCP server on that network
<small><i>(sent using the MAC broadcast address (FF-FF-FF-FF-FF-FF) so sent to every device on that segment)</i></small>
2.  *DHCP Offer:* Server responds with this message containing a proposed IP *(& other info)*
3.  *DHCP Request:* Client sends this request with the information as to whether they have accepted or declined the offer
<small><i>(If there a multiple DHCP server on the segment, client will accept 1st offer they receive)</i></small>
4.  *DHCP Acknowledgement:* Server issues this to confirm to the client that has been assigned that IP

### WINS *(Windows Internet Name Service)*

This is an older version of DNS in that it is responsible for registering & resolving computer NetBIOS names to IPs. This is now deprecated in modern networks in favour of DNS.

Benefits:

+ Provides dynamic name-to-address database that maintains support for computer name registration & resolutions
+ Provides centralised management of name-to-address database
<small><i>(so no need to manage Imhosts file)</i></small>
+ Reduces NetBIOS-based broadcast traffic on subnets as it allows clients to query WINS server directly
+ Provides support for earliet Microsoft Windows & NetBIOS-based clients
+ Allows DNS-based cliients to find NetBIOS resources when WINS lookup integration is implemented

### NAT *(Network Address Translation)*

Originally defined in RFC 1632 but later extended in RFC 3022.

When router enters a network, it sets up a NAT table by:
+ Port Address Translation *(PAT)* which assigns a socket *(IP + unique port)* to all know Private IPs
+ *IP masquerading* translates the hidden Private IP into a Public IP as a "new" source address of the outgoing IP packet
+ Creates socket with Public IPs **but** with same unique port

### DNS *(Domain Name System)*

*DNS* contains a list of computer names & equivalent IPs.<br>
Needs **3** elements to work.

##### DNS Namespace

+ Defines a tree-like structure of names
+ Each branch identifies a different domain
+ Each domain contains resources containing:

  - Host names
  - IPs
  - *other info...*

+ Query options used to retrieve specific resource records from a particular domain

##### Name Server

+ This is a server application maintaining information about the domain tree structure
+ Contains authoritativ info about 1+ domains
+ Responds to queries about its own domains & forwards the other to correct *Name Server*
+ Allows *DNS Servers* to access info about the domains in the tree

##### Resolver

+ This is a clinet program generating DNS queries & sends to DNS server for fulfilment
+ Has direct access to 1+ *DNS Server*
+ Can process referrals for direct queries to other servers as needed


