ModelAPI
========

This interface is base on Fastapi application.

Userapi has 3 parts
    1. Receive data from userapi.
    2. Apply machine learning fraud detection algorithms.
    3. Send result to dataapi.
    4. Send back result to userapi response (fraud -> yes or not ).

@app.post("/")
**************
async def result(info: Request):
    Functional get data from userapi.py and apply format.

    **Parameters:**
        trns_dict = {
            'raw': {
                'signup_time': datetime.strptime(data['signup_time'], '%d/%m/%Y %H:%M:%S'),
                'purchase_time': datetime.strptime(data['purchase_time'], '%d/%m/%Y %H:%M:%S'),
                'purchase_value': data['purchase_value'],
                'device_id': data['device_id'],
                'source': data['source'],
                'browser': data['browser'],
                'sex':data['sex'],
                'age': data['age'],
                'ip_address': data['ip_address']
            }
        }
        process_transaction(trns_dict)
        classify_transaction(trns_dict, ohe, scaler, model)
        store_data(trns_dict, url= store_data_url)

    **Response**
        Determine which response should be send userapi.py
        Fraud (Y/N)  or another response on server problem connection)
        trns_dict['result']['is_classified_fraud']

	**Returns:** trns_dict['result']['is_classified_fraud']


ds\_project.modelapi module
---------------------------

.. automodule:: ds_project.modelapi
   :members:
   :undoc-members:
   :show-inheritance:

ds\_project.model.classify module
---------------------------------

.. automodule:: ds_project.model.classify
   :members:
   :undoc-members:
   :show-inheritance:

ds\_project.model.customer\_validation module
---------------------------------------------

.. automodule:: ds_project.model.customer_validation
   :members:
   :undoc-members:
   :show-inheritance:

ds\_project.model.feature\_engineering module
---------------------------------------------

.. automodule:: ds_project.model.feature_engineering
   :members:
   :undoc-members:
   :show-inheritance:

ds\_project.model.input\_validation module
------------------------------------------

.. automodule:: ds_project.model.input_validation
   :members:
   :undoc-members:
   :show-inheritance:
