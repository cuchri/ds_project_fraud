
#/Projects/Datascientest/Examens/Fraud/phase2/html
# uvicorn main:app --reload --host 192.168.0.35
from fastapi import FastAPI
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timedelta
from .schemas import WebForm

app = FastAPI()

#BaseModel class in schemas.py.  
  
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory = "static"), name = "static")

@app.get("/form", response_class=HTMLResponse)
def index(request: Request):
    date_now= datetime.now()
    substract_date=datetime.now() + timedelta(days=-1) 
    entry_date=substract_date.strftime("%d/%m/%Y %H:%M ")
    data=[
        {'yourname':'John Travolta',
        'signup_time':entry_date,
        'purchase_time':'0',
        'purchase_value':'0',
        'device_id':'AANHQRSKUCHIC',
        'source':'Ads',
        'browser':'IE',
        'sex':'M',
        'age':'25',
        'ip_address':'4127598609'
        }
    ]
    context ={'request': request,'data':data}
    return templates.TemplateResponse("form.html",context)
                                      

@app.post('/form', response_class=HTMLResponse)
async def result(request: Request, form_data: WebForm = Depends(WebForm.as_form)):
    date_now= datetime.now()
    purchase_date=date_now.strftime("%d/%m/%Y %H:%M")
    form_data.purchase_time=purchase_date
    print(form_data)
    trns_dict="valide"
    if(trns_dict=="valide"):
        data=[{'message':'Your donate has been validated.  Thanks you','icon':'check.png'}]
    elif(trns_dict=="refuse"):
        data=[{'message':'Your donate isn\'t validated ! Fraud detected !','icon':'uncheck.png'}]
    else:
        data=[{'message':'Your donate can\'t be registred. Please try again....','icon':'info.png'}]
    context ={'request': request,'data':data}
    return templates.TemplateResponse("response.html",context)