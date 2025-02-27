R1:
ip route 2.2.2.2 255.255.255.255 192.168.12.2
router bgp 100
 neighbor 2.2.2.2 remote-as 100
 neighbor 2.2.2.2 update-source Loopback0
 neighbor 2.2.2.2 next-hop-self

R2:
ip route 1.1.1.1 255.255.255.255 192.168.12.1
router bgp 100
 neighbor 1.1.1.1 remote-as 100
 neighbor 1.1.1.1 update-source Loopback0
 network 2.2.2.2 mask 255.255.255.255
 network 10.2.0.1 mask 255.255.255.255