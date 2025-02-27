R1:
ip prefix-list DENY_10_1 deny 10.1.0.0/24
ip prefix-list DENY_10_1 permit 0.0.0.0/0 le 32
router bgp 100
 neighbor 2.2.2.2 prefix-list DENY_10_1 out

R1:
router bgp 100
 no neighbor 2.2.2.2 prefix-list DENY_10_1 out