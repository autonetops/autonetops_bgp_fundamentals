R2:
ip prefix-list DENY_10_1 deny 10.1.0.0/24 le 32
ip prefix-list DENY_10_1 permit 0.0.0.0/0 le 32
router bgp 100
 ! ARISTA
  address-family ipv4
    neighbor 1.1.1.1 prefix-list DENY_10_1 in