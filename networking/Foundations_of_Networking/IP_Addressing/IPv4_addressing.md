# IPv4 Addressing

Contents:

+ [IPv4 Classful ranges](#ipv4-classful-ranges)
+ [Reserved IP ranges & loopback](#reserved-ip-ranges-&-loopback)
+ [IPv4 Subnetting](#ipv4-subnetting)
+ [Using IPv4 Classless addressing](#using-ipv4-classless-addressing)
+ [Comparing Private, Public, & IPv4 APIPA addressing](#comparing-private-public-apipa-addressing)

### IPv4 classful ranges

There are 5 ranges; *A*, *B*, *C*, *D*, & *E*

Ranges A - C are intended for general use<br>Ranges D & E are intended for specific/non-general use:

  + D meant for Multicast use
  + E meant for Experimental use

|                                | A          | B          | C          | D          | E          |
|:------------------------------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| **_1st Octet range_**          | 1 - 126*   | 128 - 191  | 192 - 223  | 224 - 239  | 240 - 254  |
| **_Bits defining class_**      | 0          | 10         | 110        | 1110       | 1111       |
| **_Bits defining Subnet Mask_**|8<br><small><i>(N.xx.xx.xx)</i></small>|16<br><small><i>(N.N.xx.xx)</i></small>|24<br><small><i>(N.N.N.xx)</i></small>|||
| **_Actual Subnet Mask_**       |255.0.0.0   |255.255.0.0 |255.255.255.0|           |            |
| **_Network IDs Available_**    |126<br><small><i>(2^7 - 2)</i></small>|16,382<br><small><i>(2^14 - 2)</i></small>|2,097,150<br><small><i>(2^21 - 2)</i></small>|||
| **_Host per Network Available_**|16,777,214<br><small><i>(2^24 - 2)</i></small>|65,534<br><small><i>(2^16 - 2)</i></small>|254<br><small><i>(2^8 - 2)</i></small>|||
| **_Starting IP Address_**      | 0.0.0.0    | 128.0.0.0  | 192.0.0.0  | 224.0.0.0  | 240.0.0.0  |
| **_Ending IP Address_**        | 127.255.255.255| 191.255.255.255|223.255.255.255|239.255.255.255|255.255.255.255|

_* = Class A includes 127.0.0.0 - 127.255.255.255 but they cannot be used as they are reserved for loopback & diagnostic functions_

**_Bits defining class_** represents the left-most binary bits of the IP.

For example...

&nbsp;&nbsp;&nbsp;&nbsp;In Class A, 8 bits define the Network ID & the 1st bit of those 8-bits is always off *(0)*.<br>&nbsp;&nbsp;&nbsp;&nbsp;This is why Class A only has 127 Network IDs (126 usable) as the max 8-bit value that you can have is...<br>&nbsp;&nbsp;&nbsp;&nbsp;*01111111 = 127*

***

### Reserved IP ranges & loopback

- **Reserved IP**: *IPs set asided by ICANN for specific use*
- **Loopback IP**: *Set of reserved IPs that serve specific function*
				   <small><i>(allow interface to send signal back to itself)</i></small>

**Reserved IP ranges**

| Address Start Range     | Address End Range     | Range Usage                   |
|:-----------------------:|:---------------------:|:-----------------------------:|
| 0.0.0.0                 | 0.255.255.255         | Reserved                      |
| 10.0.0.0                | 10.255.255.255        | Class A Private Address Block |
| 127.0.0.1               | 127.255.255.255       | Loopback Address Range        |
| 128.0.0.0               | 128.0.255.255         | Reserved                      |
| 169.254.0.0             | 169.254.255.255       | Microsoft APIPA Reserved Range|
| 172.16.0.0              | 172.31.255.255        | Class B Private Address Block |
| 191.255.0.0             | 191.255.255.255       | Reserved                      |
| 192.0.0.0               | 192.0.0.255           | Reserved                      |
| 192.168.0.0             | 192.168.255.255       | Class C Private Address Block |
| 223.255.255.0           | 223.255.255.255       | Reserved                      |

_By saying reserved for **Private Address Block** we mean that all address' for that class reside in those ranges.

For example,<br>
&nbsp;&nbsp;&nbsp;&nbsp;In a Class C network, the default gateway is either 192.168.0.1 or 192.168.2.1.<br>&nbsp;&nbsp;&nbsp;&nbsp;The devices within that network will be assigned IPs within the ranges of...<br>&nbsp;&nbsp;&nbsp;&nbsp;*192.168.0.0 - 192.168.255.255*

*255.255.255.255* = Broadcast
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small><i>(Last address of range)</i></small>

***

### IPv4 Subnetting

##### Rules of subnetting

1. Cannot use 1st IP in range for computer
  1.1. It has been reserved for the Network Address<br><small><i>(used to identify network on router)</i></small>
  1.2. Used to identify specific network
2. Cannot use last IP in range for computer
  2.1. It is the broadcast address
  2.2. Used to send messages that are intended for all devices on that network/subnet
3. When generating subnets, cannot use 1st/last IP ranges
  3.1. 1st range: Confused by computer with network addresses
  3.2. Last range: Confused by computer with broadcast addresses
4. Usually the job of the System Admin to determine subnet ranges to use

**N.B.:** *Network ID is where the series of 1's finishes from left to right of the Subnet Mask...*
```
11111111.11111111.11111111.00000000: First 3 Octets = Network ID
11111111.11111111.00000000.00000000: First 2 Octets = Network ID
11111111.11110000.00000000.00000000: First 1.5 Octets = Network ID
```

***

### Using IPv4 Classless addressing

+ Form of IP addressing that is currently used
+ Network portion of address determined by Subnet Mask
+ Use Classless Inter-Domain Routing (CIDR) notation to show IP & Subnet
<small><i>(preferred format for issuing IPs & appropriate Subnet that ICANN has been using since 1993)</i></small>
+ When the Internet Corporation for Assigned Names and Numbers (ICANN) issues an IP:
&nbsp;&nbsp;- 24-bits are for the Network
&nbsp;&nbsp;- 8-bits are for the Host

**CIDR notation**: w.x.y.z/a
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small><i>('a' is prefix length/number of bits for network... i.e. for a Class C network, the Subnet Mask is 255.255.255.0 so the "wack" is 24)</i></small>

| Number of hosts | Prefix Length/"wack" | Decimal Format<br>*(For Mask)*           |
|:---------------:|:--------------------:|:----------------------------------------:|
| 2 - 254         | /24                  | 255.255.**255**.0                        |
| 255 - 510       | /23                  | 255.255.**254**.0<br>*(-1 from /24 SM)*  |
| 511 - 1021      | /22                  | 255.255.**252**.0<br>*(-2 from /23 SM)*  |
| 1022 - 2046     | /21                  | 255.255.**248**.0<br>*(-4 from /22 SM)*  |
| 2047 - 4094     | /20                  | 255.255.**240**.0<br>*(-8 from /21 SM)*  |
| 4095 - 8190     | /19                  | 255.255.**224**.0<br>*(-16 from /20 SM)* |
| 8191 - 16382    | /18                  | 255.255.**192**.0<br>*(-32 from /19 SM)* |
| 16383 - 32766   | /17                  | 255.255.**128**.0<br>*(-64 from /18 SM)* |
| 32767 - 65534   | /16                  | 255.255.**0**.0<br>*(-128 from /17 SM)*  |

For the last few years, ICANN has been reluctant to issue any IP with prefix length of less that 24 as you will very quickly run out of IP addresses.

***

### Comparing Private, Public, & IPv4 APIPA addressing

##### Public addressing

+ Used when an interface **DOES** require direct access to the internet *(i.e. router)*
+ Needs to be registered with ICANN...otherwise cannot access the internet

##### Private addressing

+ Used when an interface does **NOT** require direct access to the internet
<small><i>(i.e. computers on a network will have PRIVATE address' & connect to the internet indirectly through the router which has a PUBLIC address</i></small>
+ Predefined Private IP ranges *(Class A, B, or C)*:
&nbsp;&nbsp;- Predefined by ICANN in RFC 1918
&nbsp;&nbsp;- Cannot be used for Public addressing
&nbsp;&nbsp;&nbsp;&nbsp;<small><i>(Not routable on the internet)</i></small>
&nbsp;&nbsp;- Use 1 of these for when building Private network

##### APIPA addressing

+ Created by Microsoft with Windows 9x or higher
+ Used when Windows computers are set to auto find an IP when DHCP is not available

***

### Default routes & gateway settings

##### Default Route/Default Gateway

+ Is the 'Gateway of last resort'...
+ Is the summarising route of all location not known of the local subnet
+ Offloads responsibility of knowing all possible locations to router
+ Provides "next hop" destination for all destination not located on local network
+ Can be configured automatically be DHCP or manually