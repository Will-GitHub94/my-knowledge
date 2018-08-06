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
