from fastapi import FastAPI, HTTPException
import yaml

app = FastAPI()
topology = {}  # Global dictionary to store topology data

@app.get("/topology")
async def get_topology():
    try:
        with open('topology.yaml', 'r') as file:
            data = yaml.safe_load(file)
        if "devices" not in data or not isinstance(data["devices"], list):
            raise ValueError("YAML must contain a 'devices' list")
        # Store each device's details in the topology dictionary
        topology = data["devices"]
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid YAML: {str(e)}")