### Task 2: Configure iBGP with Next-Hop-Self

Now, configure internal BGP (iBGP) between R1 and R2 within AS 100. Since R2 is not directly connected to R3, R1 must share AS 200 routes with R2. You'll use the next-hop-self feature to make this work.

#### Steps
1. On R1:
   - Add R2 (2.2.2.2) as an iBGP neighbor using loopback addresses for stability.
   - Enable `next-hop-self` for the R2 neighbor.
   - Update the routing table to include R2's loopback (static route or IGP).
2. On R2:
   - Configure BGP with AS 100.
   - Add R1 (1.1.1.1) as an iBGP neighbor using loopback addresses.
   - Advertise loopback0 (2.2.2.2/32) and loopback2 (10.2.0.1/32).
   - Add a static route to reach 1.1.1.1 via 192.168.12.1.
3. Verify with `show ip bgp` on R2 that it sees 3.3.3.3/32 from R1.
4. Test by pinging 3.3.3.3 from R2.

#### Hint
Without `next-hop-self`, R2 won't know how to reach R3's next-hop IP (192.168.13.3). This is a key BGP concept!

#### Deliverables
- iBGP is up between R1 and R2.
- R2 can ping 3.3.3.3.