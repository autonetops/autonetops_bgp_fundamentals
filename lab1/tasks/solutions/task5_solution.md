
#### Solution (`tasks/solutions/task5_solution.md`)

```python
from napalm import get_network_driver
from fastapi import HTTPException

@app.get("/bgp/neighbors/{device_name}")
async def get_bgp_neighbors(device_name: str):
    # Load the topology from YAML
    try:
        with open('topology.yaml', 'r') as file:
            topology = yaml.safe_load(file)
        if "devices" not in topology or not isinstance(topology["devices"], list):
            raise ValueError("YAML must contain a 'devices' list")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid YAML: {str(e)}")

    # Find the device in the topology
    device = list(filter(lambda dev: dev["name"] == device_name, topology["devices"]))
    if not device:
        raise HTTPException(status_code=404, detail="Device not found in topology")
    
    device_info = device[0]

    # Connect to the device and get BGP neighbors
    driver = get_network_driver(device_info["type"])
    try:
        with driver(
            hostname=device_info["ip"],
            username=device_info["username"],
            password=device_info["password"]
        ) as device:
            bgp_data = device.get_bgp_neighbors()
            return {"device_name": device_name, "bgp_neighbors": bgp_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve BGP neighbors: {str(e)}")
```