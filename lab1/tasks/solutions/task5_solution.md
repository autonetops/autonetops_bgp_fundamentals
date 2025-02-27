
#### Solution (`tasks/solutions/task5_solution.md`)

```python
from napalm import get_network_driver
from fastapi import HTTPException

@app.get("/bgp/neighbors/{device_ip}")
async def get_bgp_neighbors(device_ip: str):
    if device_ip not in topology:
        raise HTTPException(status_code=404, detail="Device not found in topology")
    device_info = topology[device_ip]
    driver = get_network_driver(device_info["type"])
    try:
        with driver(
            hostname=device_ip,
            username=device_info["username"],
            password=device_info["password"]
        ) as device:
            bgp_data = device.get_bgp_neighbors()
            # Cache the BGP data in the topology
            topology[device_ip]["bgp_neighbors"] = bgp_data
            return {"device_ip": device_ip, "bgp_neighbors": bgp_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve BGP neighbors: {str(e)}")