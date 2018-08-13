# Other concepts related to addressing

Contents:

    + [Ports](#ports)
    + [Packets](#packets)
    + [Remote Access](#remote-access)

***

## Ports

Serve as an endpoint in an Operating System (OS) for different types of communication.

These are associated with the IP of te host & protocal type of communication.

They are identified by Port Numbers _(16-bit)_.

There a **3** categories...

|            | Range   | Assigned by | Use(s) |
|------------|:-------:|:-----------:|:---:|
|**Well-known** | 0 - 223 |    IANA     |Identify specified service type<br>Standards defined protocols & services _(i.e. 80 = HTTP)_ |
|**Registered**|1024 - 49151| IANA<br>_(Can also be bought by anyone)_|-|
|**Dynamic/private**|49152 - 65535| OS |-|

*_**Note:** IANA = Internet Assigned Numbers Authority_
***


## Packets

These are formatted units of data that are carried across packet-switched networks.

There are several benefits:

    + Bandwidth of communications link can be shared across multiple devices
    + Each packed is able to find it's own way across the network meaning they are easily routed if a specific link goes down

There's 2 parts to a packet:

### Control information

This is in the **header** of the packet which provides data to deliver the packet safely. This information includes:

    + The source & destination address'
    + Error detection codes
    + The sequencing information

### Payload/user information

This is in the **body** of the packet and contains the actual data that the user cares about.

***

## Remote Access

**Remote Access** is the ability to communicate with a computer or network from a remote location with data link _(i.e. Internet)_ which is accomplished by:

### Virtual Private Network _(VPN)_

**VPN** allows you to establish a virtual point-to-point link between client & server using the Internet.

It needs client-side & server-side software.

Typically, it gives remote access to a corporate network as if they were present in the building.

### Remote Desktop Software

This can be done with 3rd-party software **or** apps built into the OS.

They require software or a service to be running on the client & server sides.

It allows the end user to interact with programs running on the server-side where the apps are actually running server-side **but** are being displayed on the client.

The client is typically sent real-time screenshots of what is happening on the server.

This is how VMS are accessed remotely.

### Terminal emulation

This allows users to remotely control devices connected to the network via the Command Line Interface _(CLI)_.

There are 2 commonly used methods:

1. **Telnet**: _This is the older form but still has use. It has no security features & sends commands in clear text across the link_

2. **SSH**: _This is the replacement for_ Telnet. _It has extensive security features & allows for authentication. It also allows for transmitted data to be encrypted_