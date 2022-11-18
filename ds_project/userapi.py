import json
import requests
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from config import *


app = FastAPI()

class info(BaseModel):
    signup_time: str
    purchase_value: int
    purchase_time: str
    device_id: str
    source: str
    browser: str
    sex: str
    age: int
    ip_address: str   

   
@app.post("/")
async def result(info: Request):
    data = await info.json()
    res = requests.post(modelapi_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    response=res.json()
    return response
    

if __name__ == "__main__":
    config = uvicorn.Config("userapi:app", port=userapi_port, host=userapi_host, log_level=log_level)
    server = uvicorn.Server(config)
    server.run()
    
