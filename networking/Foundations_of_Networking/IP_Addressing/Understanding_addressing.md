# Understanding addressing

Contents:
+ [Physical addressing](#physical-addressing)
+ [Logical addressing](#logical-addressing)
+ [Logical & Physical collaboration](#logical-&amp;-physical-collaboration)
+ [Sending signals](#sending-signals)
+ [Domain types](#domain-types)

### Physical addresssing

The **physical address** of a device is its **MAC address** which is 48-bits long.<br>
This address **never** changes and is stuck with the device throughout it's life

MACs have 2 parts:

1. Organisationally Unique Identifies *(OUI)*:
  *  24-bits long
  *  Specifices manufacturer of device
  *  Needs to be registered by manufacturers
2. Host portion:
  *  24-bits long
  *  Changes for each MAC made
  &nbsp;&nbsp;<small><i>(Allows for over 16 million unique MAC addresses)</i></small>
  *  2 devices on network cannot share same MAC

<img src="../assets/mac-address-split.png"/>

Variations on the basic MAC:

+  60-bit Extended Unique Identifies *(EUI-60)*:
  -  OUI:&nbsp;&nbsp;&nbsp;24-bits long
  -  Host portion:&nbsp;&nbsp;40-bits long
+  64-bit EUI *(EUI-64)*:
  -  OUI:&nbsp;&nbsp;&nbsp;24-bits-long
  -  Host portion:&nbsp;&nbsp;40-bits long
  -  Able to work with IPv6 to create unique IPv6 addresses

**Notes:**

+ Switches do **not** have MAC addresses as their port takes the MAC address of the device that they're connected to.
+ Routers will have different MAC addresses as they'll have 1 for each subnet *(or to other routers)*.

### Logical addressing

The **logical address** of a device is its **IP address**.<br>
This address is determined by the *Network Layer Protocol* being used.<br>
Automatic Private Internet Protocal Addressing *(APIPA)* is another way to dynamically assign IPs

APIPA:

+  **Only** usable by Microsoft OS'
+  All addresses fall in range of *169.254.0.1 - 169.254.255.255*
+  Most OS' failover to APIPA if no other addressing is available
+  Many routers & switches are intended for home users to use APIPA as default

### Logical & physical collaboration

**Goal:** Sending packets from 1 computer to another that are on different subnets
**Prereq:** The sender knows the source & destination IP address but does not know how to get to the destination...
**Steps:**
1.  *Sender* sends packets to *Default Gateway*, by:
  +  Setting Source MAC to its own MAC
  +  Setting Destination MAC to MAC of interface on **Router**
  <small><i>(Switches do <b>not</b have interfaces)</i></small>
  +  Setting Source Logical *(IP)* address to its own IP
  +  Setting Destination IP to IP of receiving computer
2.  *Sender* releases packet out onto network so gets to *Router*
<small><i>(1st hop - switch is not incorporated in a hop)</i></small>
3.  *Router* analyses packet's Source & Destination IP's to determine ultimate destination
4.  If receiver not connected directly to *Router*, checks it's Routing Table to find which router needs to send it to:
  +  Sets the Source MAC to the interface that the packet came from
  +  Sets the Destination MAC to MAC of interface of *Router* sending to
5.  Releases packet back onto network
<small><i>(2nd hop)</i></small>
6.  2nd *Router* analyses packet's Source & Destination IP's to determine whether the packet is meant for a device on it's subnet:
  +  Sets the Source MAC to interface packet came in on
  +  Sets the Destination MAC to MAC of receiver
7.  Release packet back on to network so can finally reach it's destination computer!
<small><i>(3rd hop)</i></small>

*IP Address is used to find the desination from 1 computer to another while the MAC is used to move the packet/frame each step of the way it's required to go in order to reach destination*

### Sending signals

There are **3** different ways that a device can send out signals across a network

##### Unicast

+ 1 device sends packet to **only** 1 other device
<small><i>(<br>1</b>-to-<br>1</b> communication)</i></small>
+ When switches are used in a network, most traffic is done this way
<small><i>(Strength as it allows for 1-to-1 communication so no eavesdropping/collisions)</i></small>

##### Broadcast
*Desintation MAC address = FF-FF-FF-FF-FF-FF*

+ 1 device sends packet to **all** available devices at same time
<small><i>(<b>1</b>-to-<b>all</b> communication)</i></small>
+ Example of usage:
  + Network-wide alerts
  + When the system is first trying to find IP of device on DHCP network
+ When hubs were used, most network traffic was of this type

##### Multicast

+ 1 device sends packet to **group** of specific devices
<small><i>(<b>1</b>-to-<b>many</b> communication)</i></small>
+ Exampe of usage:
  + Video conferencing

### Domain types

+ There are **2** main domain types

##### Broadcast Domain

+ All devices are able to receive signal sent by another in the network
+ To be part of this, signal **cannot** have passed through switch or another middleman kind of device

##### Collision Domain

+ Happens when 2+ devices are able to cause their signals to interfere with each other
+ Bus topology *(e.g. networks using hubs)* create these type of domain
+ Not much of an issue as they used to be as switches used over hubs
