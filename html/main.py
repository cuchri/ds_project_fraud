
#/Projects/Datascientest/Examens/Fraud/phase2/html
# uvicorn main:app --reload --host 192.168.0.35
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class dict(BaseModel):
    trns_id: str
    signup_time: str
    purchase_time: str
    purchase_value: int
    device_id: str
    source: str
    
class web(BaseModel):
    signup_time: str
    purchase_time: str
    purchase_value: int
    device_id: str
    source: str
    browser: str
    sex: str
    age: int
    ip_address: str
    
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory = "static"), name = "static")

@app.get("/form/", response_class=HTMLResponse)
def index(request: Request):
    data=[
        {'yourname':'John Travolta',
        'signup_time':'15/06/2015  23:53:20',
        'purchase_time':'',
        'purchase_value':'',
        'device_id':'AANHQRSKUCHIC',
        'source':'',
        'browser':'',
        'sex':'',
        'age':'',
        'ip_address':'4127598609'
        }
    ]
    context ={'request': request,'data':data}
    return templates.TemplateResponse("form.html",context)
                                      



@app.post("/upload_web/")
async def upload_web(form: web):
    return {"message":form}