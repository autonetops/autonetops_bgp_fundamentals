### Task 1: Configure eBGP Peering

In this task, you will configure external BGP (eBGP) between R1 in AS 100 and R3 in AS 200. Your goal is to establish a BGP neighbor relationship and advertise loopback interfaces so that each router can reach the other's networks.

#### Steps
1. On R1:
   - Configure BGP with AS 100.
   - Add R3 (192.168.13.3) as an eBGP neighbor.
   - Advertise loopback0 (1.1.1.1/32) and loopback1 (10.1.0.1/32) using a network statement.
2. On R3:
   - Configure BGP with AS 200.
   - Add R1 (192.168.13.1) as an eBGP neighbor.
   - Advertise loopback0 (3.3.3.3/32).
3. Verify the BGP neighbor status using `show ip bgp summary`.
4. Check the BGP table with `show ip bgp` to ensure routes are exchanged.
5. Test connectivity by pinging 3.3.3.3 from R1 and 1.1.1.1 from R3.

#### Deliverables
- BGP is up between R1 and R3.
- R1 can ping 3.3.3.3, and R3 can ping 1.1.1.1 and 10.1.0.1.

Run `autonetops task 1` to set up the initial state if needed.