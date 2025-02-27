
#### Solution (`tasks/solutions/task4_solution.md`)

```python
from fastapi import FastAPI, UploadFile, HTTPException
import yaml

app = FastAPI()
topology = {}  # Global dictionary to store topology data

@app.post("/topology")
async def upload_topology(file: UploadFile):
    if not file.filename.endswith(".yaml") and not file.filename.endswith(".yml"):
        raise HTTPException(status_code=400, detail="Only YAML files are allowed")
    content = await file.read()
    try:
        data = yaml.safe_load(content)
        if "devices" not in data or not isinstance(data["devices"], list):
            raise ValueError("YAML must contain a 'devices' list")
        # Store each device's details in the topology dictionary
        for device in data["devices"]:
            topology[device["ip"]] = {
                "type": device["type"],
                "username": device["username"],
                "password": device["password"]
            }
        return {"message": "Topology uploaded successfully", "devices": list(topology.keys())}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid YAML: {str(e)}")