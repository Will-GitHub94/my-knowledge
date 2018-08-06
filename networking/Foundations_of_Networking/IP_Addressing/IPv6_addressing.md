# IPv6 Addressing

Contents:

+ [Introducing IPv6](#introducing-ipv6)
+ [IPv6 Subnetting](#ipv6-subnetting)
+ [IPv6 Addressing Structure](#ipv6-addressing-structure)
+ [Reserved IPv6 Ranges](#reserved-ipv6-ranges)
+ [Gateways and Subnet Masks in Ipv6](#gateways-and-subnet-masks-in-ipv6)
+ [IPv6 Link Local, 6to4 Tunelling, & 4to6]()
+ [Dual IP Stacks](#dual-ip-stacks)

***

## Introducing IPv6

IPv6 was introduced as IPv4 was designed with a 32-bit-address system in mind. This only meant that there were only over 4 million _(4,294,967,286 to be exact)_ unique addresses

IPv6 is a 128-bit addressing system which, yeah... is a whole lot more and expressed as 3.4 * 10^38.

It's designed:
    + For efficient address allocation
    + To reflect topology of internet
    + To accomodate 64-bit MAC

Allows flexibility in designing:
    + Hierarchical addressing
    + Hierarchical routing

IPv6 is described in [RFC 3516](https://tools.ietf.org/html/rfc3516)

***

## IPv6 Subnetting

Internet Service Providers _(ISPs)_ normally allocate IPv6 addresses with minimum of /48 _(48-bit)_ prefix. However, [RFC 4291](https://tools.ietf.org/html/rfc4291) does recommend at least /64 _(**Note:** Loopback is an exception of /128 though)_

Examples of IPv6 addresses _(with prefix)_ are _3ffd:2093:c003::/48_ with a 48-bit prefix **or** _3ffd:2093:c003:0000::/64_ with a 64-bit prefix _(RFC recommendation)_.

### Site ID

The **Site ID** is the 16-bits that appear **AFTER** the prefix and gives over 65,000 _(again...to be exact @ 65,536)_ possible unique IDs.

This is added to the original prefix. Say the prefix was 64-bits, the new prefix would be calculated as:

```
64 + 16 = 80
```

The new prefix now leaves 48-bits for Host IDs _(so that's 281,474,976... - a very large number)_

***

## IPv6 Addressing Structure

The IPv6 address is 128-bits _(as mentioned)_ and broken down into 16-bit boundaries/sections.

Each of these sections is represented by a 4-digit hexadecimal number _(with each hex digit represented by 4-bits - i.e. F = 1111)_.

Each section is separated out with a colon _(:)_.

When written, the address can be simplified following these rules:
    + If the sections has more than 1 _(left-most)_ 0, then 0s can be removed
    _(i.e. 00c3 = c3)_
    + When removing leading 0s, at least 1 digit must be left
    _(i.e. 0000 **cannot** be null...has to be at least 1 digit so becomes 0)_

***

## Reserved IPv6 Ranges

### Unspecified IPv6 Address'

These are shown as; _0:0:0:0:0:0:0:0_ **or** _::_ and indicates the adsence of an address.

These are used as source address for packets to verify uniqueness of adress.

These are never assigned to an interface or used as a destination

### Loopback Address

Shown as; _0:0:0:0:0:0:0:1_ **or** _::1_

### Compatibility Address'

These are used to aid the migration from IPv4 to IPv6 and allow the coexistence of IPv4 & IPv6 host on same network.

#### IPv4-Compatible Address'

Shown as; _0:0:0:0:0:0:w.x.y.z_ **or** _::w.x.y.z_ _(the letters represent the **PUBLIC** IPv4 address where w.x make 1 boundary/section & y.z make the other)_.

These are only used by IPv6/IPv4 nodes to communicate using IPv6.

IPv6/IPv4 nodes support both IPv4 & IPv6 protocols _(Dual-IP stack node)_

IPv6 traffic is encapsulated with IPv4 header which makes it possible to send packet to it's destination using IPv4 infrastructure

#### IPv4-Mapped Address'

Shown as; _0:0:0:0:0:ffff:w.x.y.z_ **or** _::ffff:w.x.y.z_.

They represent IPv4-only node to IPv6 node and they are **never** used as a source or destination address for an IPv6 packet.

#### 6to4 Address'

Described in [RFC 3056](https://tools.ietf.org/html/rfc3056).

These communicate between 2 nodes that are both running IPv4 & IPv6 over an IPv4 routing infrastructure.

They are formed by combining 2002::/16 with 32 bits of the **public** IPv4 address of node which forms 48-bit prefix to define connection on IPv4 routing infrastructure.

**Tunnelling** is the process of establishing connection through public network. Connections look like point-to-point connection to devices on either end _(but it's really not...)_

#### ISATAP Address'

These are used between 2 nodes both running IPv4 & IPv6 over IPv4 routing infrastructure.

These use locally administered interface ID: _::0:5efe:w.x.y.z_ _(From w onwards, can be **ANY** UNICAST IPv4 address which includes either **public** or **private**)_.

The **Interface ID** can be combined with any valid 64-bit IPv6 address, including:
    + Link-local address prefix _(fe80::/64)_
    + Site-local prefixes
    + Global prefixes

#### Teredo Address'

Uses prefix _3ffe:831f::/32_.

These represent the host when using auto tunelling mechanisms.

These addresses are used to encode IPv4 address of Teredo server _(after the first 32-bits)_

***

## IPv6 Link Local, 6to4 tunelling, & 4to6

### Ipv6 Global Unicast Address'

These:
    + Are equivalent to **public** IPv4 address'
    + Are globally routable
    + Are reachable on IPv6 internet
    + Are defined in [RFC 3587](https://tools.ietf.org/html/rfc3587)

### IPv6 Link-local Address'

These:
    + Are used when communicating with neighbouring nodes on a single-link network
    _(Single-link - No router & limited to local segments)_
    + Are not able to communicate with hosts if they're on seperate links
    + Are equivalent to APIPA address'
    + Are required for Neighbour Discovery Process (NDP)
    _(Allows computer to discover all others directly connected to it...it's neighbours)_
    + Are auto-configured if no other address is on the network
    + Always begin with; _fe80_

IPv6 routers never forward link-local traffic beyond these address'

### IPv6 Site-local Address'

These:
    + Are equivalent to **private** IPv4 address'
    _(cannot be used to connect to internet directly)_
    + Are only assigned through address config
    _(**NOT** auto-configured)_
    + Always start with; _fec0::/10_

After 1st 10 bits, there is a 54-bit subnet identifier _(10 + 54 = /64...prefix)_

***

## Dual-IP Stacks

**Dual-IP Stacks** is a network that has both IPv4 & IPv6 enabled on the same node.

It is important to let routers know of this as routers are the 1st nodes to receive outside traffic.


