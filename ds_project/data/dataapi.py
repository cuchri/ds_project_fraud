from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
import csv
import uvicorn
from config import *

app = FastAPI(
    title="Collect data of transaction",
    description="This API stores raw data and the scoring result of transaction data",
    version="1.0.1"
)

class Data(BaseModel):
    """Transaction data that is added to the database"""
    signup_time: datetime
    purchase_time: datetime
    purchase_value: int
    device_id: str
    source: str
    browser: str
    sex: str
    age: int
    ip_address: str
    is_classified_fraud: bool


@app.get('/', tags=['home'])
async def root():
    """Functional check of API.
    """
    return {'greetings': 'API is up and running!!!'}


@app.post('/store_data', tags=['store data'])
async def write_csv(data: Data):
    """New transaction data are stored to csv.
    """

    d = {}
    d.update({'signup_time': data.signup_time})
    d.update({'purchase_time': data.purchase_time})
    d.update({'purchase_value': data.purchase_value})
    d.update({'device_id': data.device_id})
    d.update({'source': data.source})
    d.update({'browser': data.browser})
    d.update({'sex': data.sex})
    d.update({'age': data.age})
    d.update({'ip_address': data.ip_address})
    d.update({'is_classified_fraud': data.is_classified_fraud})

    # write out to questions.csv
    with open('./data/trns_data.csv', 'a', newline='') as trns_data_csv_out:
        fieldnames = ['signup_time',
                      'purchase_time',
                      'purchase_value',
                      'device_id',
                      'source',
                      'browser',
                      'sex',
                      'age',
                      'ip_address',
                      'is_classified_fraud']
        csv_writer = csv.DictWriter(trns_data_csv_out, fieldnames=fieldnames)
        csv_writer.writerow(d)
    return d

if __name__ == "__main__":
    config = uvicorn.Config("dataapi:app", port=dataapi_port, host=datapi_host, log_level=log_level)
    server = uvicorn.Server(config)
    server.run()