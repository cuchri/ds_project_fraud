UserInterface
=============

This interface is base on Flask application.

Userinterface has 3 parts
    1. HTML Dispaly
        - Entry form to fill out

    2. Forward data
        - Send data from submit form

    2. Response
        - Display result of fraud (Yes or Not)

@app.route("/", methods=['GET', 'POST'])
****************************************
def INDEX():

    Functional POST data from HTML formular.
    Running with FastAPI.

    **Parameters**:
        'signup_time':request.form['signup_time'],
        'purchase_time':request.form['purchase_time'],
        'purchase_value':int(request.form['purchase_value']),
        'device_id':request.form['device_id'],
        'source':request.form['source'],
        'browser':request.form['browser'],
        'sex':request.form['sex'],
        'age':int(request.form['age']),
        'ip_address':request.form['ip_address']

    **Returns**: render_template("response.html",response=res_response)