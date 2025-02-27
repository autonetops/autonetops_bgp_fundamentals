
**Solution** (`tasks/solutions/task4_solution.md`):
```python
from fastapi import FastAPI
from napalm import get_network_driver

app = FastAPI()

@app.get("/bgp/neighbors")
async def get_bgp_neighbors():
    driver = get_network_driver("ios")
    device = driver("192.168.13.1", "admin", "cisco")
    device.open()
    bgp_data = device.get_bgp_neighbors()
    device.close()
    return bgp_data["global"]["peers"]