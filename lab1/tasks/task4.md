### Task 4: Implement a Topology Upload Endpoint

In this task, you will create a FastAPI endpoint that allows users to upload a YAML file containing network topology information. This endpoint will parse the YAML file and store the device details in a global dictionary for use in other tasks.

#### Steps
1. **Define the Endpoint**:
   - Create a `POST /topology` endpoint using FastAPI.
   - Use FastAPI's `UploadFile` to accept a YAML file.
   - Validate that the uploaded file is a YAML file (ends with `.yaml` or `.yml`).
   - Parse the YAML content and ensure it contains a `devices` list.
   - Store each device's details (IP, type, username, password) in a global dictionary called `topology`.

2. **Handle Errors**:
   - If the file is not a YAML file, return a 400 error with the message "Only YAML files are allowed".
   - If the YAML is invalid or does not contain a `devices` list, return a 400 error with an appropriate message.

3. **Return a Success Message**:
   - On successful upload, return a message confirming the upload and list the device IPs.

#### Starter Code
```python
from fastapi import FastAPI, UploadFile, HTTPException
import yaml

app = FastAPI()
topology = {}  # Global dictionary to store topology data

# Your code here