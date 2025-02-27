### Task 4: Network Automation with FastAPI and NAPALM

In this task, you’ll dive into network automation by completing a FastAPI endpoint that retrieves BGP neighbor information from R1. The lab includes a partially implemented FastAPI app with NAPALM integration.

#### Steps
1. Open the FastAPI app (assume it’s in `bgp_fundamentals/api/app.py`).
2. Find the `/bgp/neighbors` endpoint—it’s incomplete.
3. Use NAPALM’s `get_bgp_neighbors()` method to fetch BGP data from R1 (IP: 192.168.13.1, username/password provided in configs).
4. Return the data in JSON format.
5. Test by running the app (`uvicorn app:app`) and sending a GET request to `http://localhost:8000/bgp/neighbors`.

#### Starter Code
```python
from fastapi import FastAPI
from napalm import get_network_driver

app = FastAPI()

@app.get("/bgp/neighbors")
async def get_bgp_neighbors():
    # Your code here
    pass