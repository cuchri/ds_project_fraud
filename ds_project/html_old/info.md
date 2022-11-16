CTRL+SHIF +V  for preview
<pre>
html
    ├── attack.py  <-- injection loop  request function.
    ├── info.md
    ├── __init__.py
    ├── main.py    <--- Starting point uvicorn FastApi
    ├── schemas.py  ---> data model for Post
    ├── static
    │   ├── check.png
    │   ├── info.png
    │   ├── jquery-3.5.0.min.js
    │   ├── styles.css
    │   ├── support.png
    │   └── uncheck.png
    └── templates
        ├── form.html  <-- Get to view form and on Post on submit
        ├── __init__.py
        └── response.html <-- Result of post. (form)
        
</pre>

class dict(BaseModel):
    trns_id
    signup_time
    purchase_time
    purchase_value: int
    device_id
    source
	
class web (BaselModel):
	signup_time
    purchase_time
    purchase_value: int
    device_id
    source
	browser
	sex
	age: int
	ip_address
	
{
"signup_time": "01/01/2015  04:25:23",
"purchase_time": "01/01/2015  04:25:24",
"purchase_value": 57,
"device_id": "AAAXXOZJRZRAO",
"source":"Ads",
"browser": "FireFox",
"sex": "FireFox",
"age": 36,
"ip_address": "82.32.79.145"
}


conversion: Should we converting ?
1377849233  --> 82.32.79.145



