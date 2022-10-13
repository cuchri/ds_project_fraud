"""
main.py
====================================
The core module of DS_project fraud
"""

from fastapi import FastAPI
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timedelta

import pickle
from pathlib import Path
import os

BASE_PATH = Path(__file__).resolve().parent
#print(BASE_PATH)

app = FastAPI()

# BaseModel class in schemas.py.

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/../data", StaticFiles(directory="data"), name="data")
app.mount("/../model", StaticFiles(directory="model"), name="model")

# load preprocessing and model
ohe = pickle.load(open('model/_ohe.sav', 'rb'))
scaler = pickle.load(open('model/_scaler.sav', 'rb'))
model = pickle.load(open('model/_tree_model.sav', 'rb'))

from model.classify import process_transaction, classify_transaction
from html.schemas import *
from html import templates

@app.get("/form", response_class=HTMLResponse)
async def index(request: Request):
    """
    Entry point to api in order to simulate an real purchase / donation situation
    :param request: simulates a transaction - fills form with predefined transaction data
    :return: prefilled form
    """
    print("------------ START ------GET-----------------------")
    #substract_date = datetime.now() + timedelta(days=-1)
    substract_date = datetime.now()
    entry_date = substract_date.strftime("%d/%m/%Y %H:%M:%S")
    data = [
        {'yourname': 'John Travolta',
         'signup_time': entry_date,
         'purchase_time': '0',
         'purchase_value': '0',
         'device_id': 'AAAXXOZJRZRAO',
         'source': 'Ads',
         'browser': 'FireFox',
         'sex': 'F',
         'age': '36',
         'ip_address': '1377849233'
         }
    ]
    context = {'request': request, 'data': data}
    return templates.TemplateResponse("/form.html", context)


@app.post('/form', response_class=HTMLResponse)
async def result(request: Request, form_data: WebForm = Depends(WebForm.as_form)):
    """
    Processes the data from the form - calls data preprocessing and applies the model
    :param request: simulates a transaction that calls the model
    :param form_data: transaction data
    :return response:
    """
    date_now = datetime.now()
    purchase_date = date_now.strftime("%d/%m/%Y %H:%M:%S")
    form_data.purchase_time = purchase_date
    print("------------ START ------POST ANALYSE--------------")
    print('formdata: ', form_data)

    # classify transaction data
    trns_dict = {
        'raw': {
            'signup_time': datetime.strptime(form_data.signup_time, '%d/%m/%Y %H:%M:%S'),
            'purchase_time': datetime.strptime(form_data.purchase_time, '%d/%m/%Y %H:%M:%S'),
            'purchase_value': form_data.purchase_value,
            'device_id': form_data.device_id,
            'source': form_data.source,
            'browser': form_data.browser,
            'sex': form_data.sex,
            'age': form_data.age,
            'ip_address': form_data.ip_address
        }
    }
    print('preprocessing start')
    trns_dict = process_transaction(trns_dict)
    print('classify start')
    trns_dict = classify_transaction(trns_dict, ohe, scaler, model)
    print('trns_dict: ', trns_dict)
    print("------------ END POST ANALYSE -------------------")
    print("------------ DISPLAY FRAUD OR NOT ---------------")
    print("------------ END OF SEQUENCE --------------------")
    if not trns_dict['result']['is_classified_fraud']:
        data = [{'message': 'Your donation has been validated.  Thank you', 'icon': 'check.png'}]
    elif trns_dict['result']['is_classified_fraud']:
        data = [{'message': 'Your donation isn\'t validated ! Fraud detected !', 'icon': 'uncheck.png'}]
    else:
        data = [{'message': 'Your donation can\'t be registered. Please try again....', 'icon': 'info.png'}]
    context = {'request': request, 'data': data}
    return templates.TemplateResponse("response.html", context)
