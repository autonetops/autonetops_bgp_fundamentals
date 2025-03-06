
#### Solution (`tasks/solutions/task4_solution.md`)

```python

#### SOLUCAO ###
from fastapi import FastAPI, HTTPException
import yaml

app = FastAPI()

@app.get("/topology")
async def get_topology():
    try:
        with open('topology.yaml', 'r') as file:
            topology = yaml.safe_load(file)
        if "devices" not in topology or not isinstance(topology["devices"], list):
            raise ValueError("YAML must contain a 'devices' list")
        return topology
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid YAML: {str(e)}")