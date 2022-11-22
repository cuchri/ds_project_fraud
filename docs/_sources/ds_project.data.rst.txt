DataAPI
=======

This interface is base on Fastapi application.

Dataapi has 2 parts
    1. Receive data from modelapi
    2. Store data in csv format

@app.get('/', tags=['home'])
****************************
    async def root():
        """Functional check of API.
        """
    **Parameters:**
        No parameters


    **Response**
        greetings


@app.post('/store_data', tags=['store data'])
*********************************************
    async def write_csv(data: Data):
        """New transaction data are stored to csv.

    **Parameters:**
        d = {}
        d.update({'signup_time': data.signup_time})
        d.update({'purchase_time': data.purchase_time})
        d.update({'purchase_value': data.purchase_value})
        d.update({'device_id': data.device_id})
        d.update({'source': data.source})
        d.update({'browser': data.browser})
        d.update({'sex': data.sex})
        d.update({'age': data.age})
        d.update({'ip_address': data.ip_address})
        d.update({'is_classified_fraud': data.is_classified_fraud})

    **Response**
        True or False
