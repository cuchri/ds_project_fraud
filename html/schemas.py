from fastapi import Form, File, UploadFile
from pydantic import BaseModel


class WebForm(BaseModel):
    signup_time: str
    purchase_value: int
    purchase_time: str
    device_id: str
    source: str
    browser: str
    sex: str
    age: int
    ip_address: str    
    
   

    @classmethod
    def as_form(
        cls,
        signup_time: str = Form(...),
        purchase_value: int = Form(...),
        purchase_time: str = Form(...),
        device_id: str = Form(...),
        source: str = Form(...),
        browser: str = Form(...),
        sex: str = Form(...),
        age: int = Form(...),
        ip_address: str = Form(...)
    ):
    
        return cls(
            signup_time = signup_time,
            purchase_value = purchase_value,
            purchase_time = purchase_time,
            device_id = device_id,
            source = source,
            browser = browser,
            sex = sex,
            age = age,
            ip_address = ip_address
        )