### Task 5: Modify the `/bgp/neighbors` Endpoint to Accept a Device IP

In this task, you will update the existing `/bgp/neighbors` endpoint to accept a `device_ip` parameter. This will allow the endpoint to retrieve BGP neighbor information from any device specified in the topology.

#### Steps
1. **Update the Endpoint**:
   - Modify the endpoint to `GET /bgp/neighbors/{device_ip}`.
   - Use the `device_ip` path parameter to specify which device's BGP neighbors to retrieve.
   - Check if the `device_ip` exists in the `topology` dictionary. If not, return a 404 error.

2. **Integrate with NAPALM**:
   - Use the device’s type and credentials from the `topology` dictionary to connect via NAPALM.
   - Fetch the BGP neighbor data using NAPALM’s `get_bgp_neighbors()` method.
   - Cache the retrieved BGP neighbor data in the `topology` dictionary under a new key, `"bgp_neighbors"`.

3. **Return the BGP Neighbor Data**:
   - Return the device IP and its BGP neighbor information in JSON format.

#### Starter Code
```python
from napalm import get_network_driver
from fastapi import HTTPException

# Your code here