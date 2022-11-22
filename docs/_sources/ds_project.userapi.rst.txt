UserAPI
=======

This interface is base on Fastapi application.

Userapi has 3 parts
    1. Receive data from userinterface.
    2. Send response from modelapi to userinterface.
    3. Receive data from modelapi who is transmitted to userinterface.

@app.post("/")
***************
async def result(info: Request):

    Functional POST data from HTML formular.
    Running with FastAPI.

    **Parameters:**
        data: incoming from userinterface
        res: modelapi_url, data=json.dumps(data), headers=

    **Returns:** render_template("response.html",response=res_response)