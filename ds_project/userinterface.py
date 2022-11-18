from flask import Flask,render_template,request
from datetime import datetime, timedelta
import requests
import json

from config import *

app = Flask(__name__,template_folder='templates', static_folder='static')

@app.route("/", methods=['GET', 'POST'])
def INDEX():
    if request.method == 'POST':
        res_response = ''
        res=''
        data ={
        'signup_time':request.form['signup_time'],
        'purchase_time':request.form['purchase_time'],
        'purchase_value':int(request.form['purchase_value']),
        'device_id':request.form['device_id'],
        'source':request.form['source'],
        'browser':request.form['browser'],
        'sex':request.form['sex'],
        'age':int(request.form['age']),
        'ip_address':request.form['ip_address']
        }
        print('------userinterface ----------')
        print(data)
        res = requests.post(userapi_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        #res = requests.post('http://0.0.0.0:8000/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
    
        print(res.text)
        res_response=res.json()
        print(res_response)
        response = {
        "status" : "received data from userinterface"
        }
        return render_template("response.html",response=res_response)
   
    date_now = datetime.now()
    substract_date = datetime.now() + timedelta(days=-1) 
    current_date = date_now.strftime("%d/%m/%Y %H:%M:%S")
    entry_date=substract_date.strftime("%d/%m/%Y %H:%M:%S")
    data ={
        'yourname':'John Travolta',
        'signup_time':entry_date,
        'purchase_time':current_date,
        'purchase_value':'100',
        'device_id':'UFFGHIJHOJQRY',
        'source':'Ads',
        'browser':'Chrome',
        'sex':'M',
        'age':'43',
        'ip_address':'3019254031'
        }

    return render_template("index.html",form_data = data)


if __name__=='__main__':
    #app.run(debug=True, port=80,host='0.0.0.0')
    app.run(debug=debug_mode, port=userinterface_port,host=userinterface_host)