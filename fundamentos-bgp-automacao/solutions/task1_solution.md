R1:
router bgp 100
 neighbor 192.168.13.3 remote-as 200
 network 1.1.1.1 mask 255.255.255.255
 network 10.1.0.1 mask 255.255.255.255

R3:
router bgp 200
 neighbor 192.168.13.1 remote-as 100
 network 3.3.3.3 mask 255.255.255.255