# Commonly Used Network Devices

Contents:

- [NICs](#network-interface-cards-controllers-nics)
- [Bridges](#bridges)
- [Hubs](#hubs)
- [Switches](#switches)
- [Access Points](#access-points)
- [Modems](#modems)

***

## Network Interface Cards/Controllers _(NICs)_

A _Network Interface **Card**_ is older than a _**Controller**_ & is in expansion cards as opposed to being built-in to the motherboard/device/USB.

These allow computers or other devices to access the network.

They work on _Layers 1 & 2_ of the OSI Model.

### Considerations

When purchasing a NIC, you need to make sure it matches:

- **Tech in use**: _For example, 802.11n Wifi requires 802.11n NIC. UTP cabling requires UTP NIC_

- **Speed in use**: _For example, GB Ethernet requires GB Ethernet NIC..._

- **Network Architecture**: _For example, Token Ring network requires Token Ring NIC and, likewise, Ethernet network requires Ethernet NIC_

***

## Bridges

**Bridges** break up the network into smaller segments so fewer collisions take place & there is better ability to get packets through the network communication link.

These are older technology but are still relevant as they are the forerunner to [switches](#switches).

They work on _Layer 2_ of the OSI Model.

They can read frames to determine if they are allowed to pass which reduces the amount of traffic on the overlal network as it is divided into multiple segments.

***

## Hubs

These are being replaced by [switches](#switches).

They work on _Layer 1_ of the OSI Model.

They logically function as a bus topology whereby the signal comes into the **Hub** which will then be broadcast to all other devices connected to that **Hub** & generates bus topology which means devices on the network have to contend to find out who gets to send the data first.

If there is too many hosts, there will be constant collisions which could cripple the network _*sad face*_.

There are **3** types:

### 1. Passive Hub

These work like cable splitters.

The more devices that are connected to them, the weaker the signal is to each device.

_Do correlative graph here..._

### 2. Active Hub

These need a large _(ish)_ amount of power as they add power to the signal when passing through the port of a device. This prevents weakening of the signal when multiple devices are attached.

These repeat the signal to **ALL** hosts connected _(Broadcast)_.

These are used to connect other **Hubs** together. However, you need to follow the _5-4-3_ rule:

- _No more than **5** segments can be linked together_
- _Up to **4** linking devices can be used to form segments_
- _Only **3**/5 segments can be populated by computers_

### 3. Intelligent Hub

These are like **Active Hubs** but with additional features, for example:

- **Network diagnostic**: _Troubleshoot & send back any problems on the network_
- **Managements abilities**: _Turn on/off ports as wanted to more efficiently manage connected devices_

***

## Switches

These are used to connect multiple computers together.

They work on _Layer 2_ of the OSI Model _(some can also work on higher levels - **Multilayer Switch**)_.

They store a list of MAC Address' of computers connected to it.

### Basic Switch

This is the most common type of **Switch** & is, essentially, a multiport **bridge** as can be used to separate larger networks into smaller segments called _"Collision Domains" (more on these in a bit)_...

These commonly convert media from 1 type to another.

Some swithces have fiber coming into them _(common in corporate environments)_ but send signals out over copper twisted pair wires.

Variations of the basic switch are:

- **Managed**: _These are programmable & used to control how data behaves on the network. These are most often found in corporate environments_.
- **Unmanaged**: _These are **not** programmable and, instead, come with a default configuration. Most can only be changed within the predefined limits & others cannot be changed at all! Most home/SOHO switches use this._

#### Collision Domains

These are setup by taking 2 devices that want to talk to each other & links together only the ports that are relevant so they can have point-to-point communication.

These result in no collisions on the network as a **Collision Domain** only has 2 machines.

These allow different ports to communicate at full speed _(without point-to-point, the **switch** would have to divide the signal over the number of ports leading to a weaker signal...)_.

These also make it harder to listen in on traffic on the network.

***

## Routers

These move data around large networks _(Wide Area Networks - WANs)_.

They work on _Layers 3 & 4_ of the OSI Model and some can also work on higher levels as well...

These are intelligent as they have to make decisions _(based on a list of criteria)_ about where to send data:

- **Hops**: _The number of nodes the packet has to pass through to get to the destination. The **router** will choose the least number of **hops**_
- **Network Traffic**: _The **router** will choose the route with least traffic...duh_
- **Network Throughput**: _The amount of data that can pass through the link in a set amount of time. The route which will take the least time to send the data through will be chosen_
- **Network Reliability**: _Most reliable route will be chosen (this kind of info is kept in a log)_

**Routers** collect all info to determine the best router & store this information in a table. When determing a neew route, the **router** will look back at this table to determine the best route chosen last time in an attempt to make a faster decision.

**Routers** are programmable _(like switches)_. A user can program:

- Interface configuration
- Which networks the **router** is connected to
- The criteria for what is (not) allowed through the **router**
- Multiple protocols into **router** so making it more flexible

***

## Access Points

***

**Access Points** are devices that allow computers to access the network.

They are commonly used in home environments so all computers in the house can gain access to the internet.

These can be wired or wirless. Wireless is much more common but wired will have better reliability.

### Wireless Access Points _(WAPs)_

These are used to give public access to the internet in many locations; libraries, restaurants, airports, hotels, et cetera...

They are a type of connectivity device. They are used to offer wireless access to the network. They can offer; _Authentication_, & _Encryption_. These combine the role of **switches** & **routers** and can be programmed only to limited extent.

***

## Modems

These _**typically**_ connect computers to the internet.

A _switch_ can be used to connect all computers on the network together. The _switch_ can then be connected to the _modem_ so all computers connected to the _switch_ can access the internet. Switches only allow hardline connections, it does not have any wireless interfaces! _Routers_ can connect to the internet on their own **without** a _modem_.

***

Just to break internet connectivity down...devices on a network can be connecte via _Switch_ or a _Hub_. Either of these can be connected _(physically)_ to a _Modem_ and then any devices connected to the _Hub_ or _Switch_ can access the internet.

Nowadays, _Routers_ will have a _Switch_ built-in to them and, seeing as they can access the internet without a _Modem_, any device connected to a _Router (that has their RJ45 Ethernet active)_ can access the internet. _Routers_, nowadays, also have _WAPs_ built-in to them so provide Wifi as well.






