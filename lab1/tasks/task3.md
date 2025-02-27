### Task 3: Troubleshoot BGP

Something’s wrong! R2 cannot see the 10.1.0.0/24 prefix from R1, even though R1 is advertising it to R3. Investigate and fix the issue.

#### Steps
1. Check the BGP table on R2 (`show ip bgp`)—is 10.1.0.1/32 present?
2. On R1, examine the BGP configuration (`show run | section bgp`).
3. Look for filters, policies, or missing commands that might block the advertisement to R2.
4. Fix the issue and verify that R2 now sees 10.1.0.1/32.
5. Test by pinging 10.1.0.1 from R2.

#### Hint
Compare what R3 sees versus R2. Is R1 treating its neighbors differently?

#### Deliverables
- R2’s BGP table includes 10.1.0.1/32.
- Successful ping from R2 to 10.1.0.1.