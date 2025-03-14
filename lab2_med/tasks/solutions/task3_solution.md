R2:

ip prefix-list NET3 permit 3.3.3.3/32
ip prefix-list NET33 permit 33.3.3.3/32
!
route-map MED permit 10
  match ip address prefix-list NET3
  set metric 50
!
route-map MED permit 20
  match ip address prefix-list NET33
  set metric 100
!
route-map MED permit 100
!
clear ip bgp * out

R4:
ip prefix-list NET3 permit 3.3.3.3/32
ip prefix-list NET33 permit 33.3.3.3/32
!
route-map MED permit 10
  match ip address prefix-list NET3
  set metric 100
!
route-map MED permit 20
  match ip address prefix-list NET33
  set metric 50
!
route-map MED permit 100
!
router bgp 200
  neighbor 192.168.14.1 route-map MED out
!
clear ip bgp * out