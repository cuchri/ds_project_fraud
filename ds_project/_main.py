import os
import sys

from fastapi import FastAPI
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

from datetime import datetime, timedelta
import pickle
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
print(BASE_PATH)
from html.schemas import WebForm

app = FastAPI()

templates = Jinja2Templates(directory=str(BASE_PATH / "./html/templates"))
app.mount("/html", StaticFiles(directory="html"), name="html")
app.mount("/data", StaticFiles(directory="data"), name="data")
app.mount("/model", StaticFiles(directory="model"), name="model")
app.mount("/static", StaticFiles(directory=str(BASE_PATH / "./html/static")), name="static")

# load preprocessing and model
ohe = pickle.load(open('model/_ohe.sav', 'rb'))
scaler = pickle.load(open('model/_scaler.sav', 'rb'))
model = pickle.load(open('model/_tree_model.sav', 'rb'))

from model.classify import process_transaction, classify_transaction

@app.get("/form", response_class=HTMLResponse)
def index(request: Request):
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
    
if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8000, host='0.0.0.0', log_level="debug")
    server = uvicorn.Server(config)
    server.run()