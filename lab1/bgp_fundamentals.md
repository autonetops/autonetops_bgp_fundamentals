Overview
This lab introduces students to the Border Gateway Protocol (BGP), a critical protocol for inter-domain routing on the internet. Using Cisco IOL (IOS on Linux) images in a Containerlab environment, students will configure a multi-router topology to explore external BGP (eBGP), internal BGP (iBGP), and key BGP concepts like the next-hop-self attribute. The lab includes a troubleshooting challenge to reinforce learning and a network automation task using FastAPI and NAPALM to retrieve BGP neighbor information, showcasing modern networking practices. The lab is designed to be engaging, practical, and a perfect showcase for your advertising purposes.

Topology
The lab uses a three-router topology to demonstrate both eBGP and iBGP interactions:

R1 (AS 100): A Cisco IOL router acting as the gateway between AS 100 and AS 200.
R2 (AS 100): A Cisco IOL router internal to AS 100, connected only to R1.
R3 (AS 200): A Cisco IOL router in a different autonomous system, connected to R1.
Connections
R1 eth1 <-> R3 eth1: eBGP peering between AS 100 and AS 200.
R1 eth2 <-> R2 eth1: iBGP peering within AS 100.
IP Addressing
Each router has a loopback0 interface for identification and route advertisement:

R1: 1.1.1.1/32 (Loopback0), 10.1.0.1/32 (Loopback1)
R2: 2.2.2.2/32 (Loopback0), 10.2.0.1/32 (Loopback2)
R3: 3.3.3.3/32 (Loopback0)
Physical interfaces will use the following IP addresses:

R1 eth1: 192.168.13.1/24
R3 eth1: 192.168.13.3/24
R1 eth2: 192.168.12.1/24
R2 eth1: 192.168.12.2/24
This topology allows students to explore how routes propagate across AS boundaries (eBGP) and within an AS (iBGP), with a focus on the next-hop-self attribute to ensure route reachability.