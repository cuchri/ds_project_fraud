import os
import sys
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import requests
from config import *
from datetime import datetime, timedelta
import pickle
from pathlib import Path
from model.classify import process_transaction, classify_transaction, store_data

#BASE_PATH = Path(__file__).resolve().parent
#print(BASE_PATH)

app = FastAPI()

app.mount("/data", StaticFiles(directory="data"), name="data")
app.mount("/model", StaticFiles(directory="model"), name="model")


# load preprocessing and model
ohe = pickle.load(open('model/_ohe.sav', 'rb'))
scaler = pickle.load(open('model/_scaler.sav', 'rb'))
model = pickle.load(open('model/_tree_model.sav', 'rb'))

@app.post("/")
async def result(info: Request):
    """Functional Get data from userinterface.py and apply format.
    """
    data = await info.json()
    
    # classify transaction data
    trns_dict = {
        'raw': {
            'signup_time': datetime.strptime(data['signup_time'], '%d/%m/%Y %H:%M:%S'),
            'purchase_time': datetime.strptime(data['purchase_time'], '%d/%m/%Y %H:%M:%S'),
            'purchase_value': data['purchase_value'],
            'device_id': data['device_id'],
            'source': data['source'],
            'browser': data['browser'],
            'sex':data['sex'],
            'age': data['age'],
            'ip_address': data['ip_address']
        }
    }

 
    trns_dict = process_transaction(trns_dict)
    trns_dict = classify_transaction(trns_dict, ohe, scaler, model)
    trns_dict = store_data(trns_dict, url= store_data_url)

    """ Determine which response to send on userinterface.py 
        Fraud (Y/N)  or another response on server problem connection)
    """
     
    if not trns_dict['result']['is_classified_fraud']:
        response = {'status': 'Your donation has been validated.  Thank you', 'icon': 'check.png'}
    elif trns_dict['result']['is_classified_fraud']:
        response = {'status': 'Your donation isn\'t validated ! Fraud detected !', 'icon': 'uncheck.png'}
    else:
        response = {'status': 'Your donation can\'t be registered. Please try again....', 'icon': 'info.png'}
        
    return response
 
    
if __name__ == "__main__":
    config = uvicorn.Config("modelapi:app", port=modelapi_port, host=modelapi_host, log_level=log_level)
    server = uvicorn.Server(config)
    server.run()