import pandas as pd
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime


def test_integration_on_samplerequests():
    # read sample transaction data
    path = 'ds_project/data/sample_requests.csv'
    df_transactions = pd.read_csv(path,
                                  dtype={'user_id': object,
                                         'device_id': object,
                                         'purchase_value': int,
                                         'source': object,
                                         'browser': object,
                                         'sex': object,
                                         'age': int,
                                         'ip_address': object,
                                         'signup_time': object,
                                         'purchase_time': object
                                         },
                                  index_col=0
                                  )

    df_transactions = df_transactions.reset_index()  # make sure indexes pair with number of rows
    print(df_transactions.head())

    # set parameters
    url = "http://localhost:8000/"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"


    # The requests:
    for index, row in df_transactions.iterrows():
        d = row['signup_time']
        signup_time = d[8:10] + '/' + d[5:7] + '/' + d[0:4] + d[10:]
        d = row['purchase_time']
        purchase_time = d[8:10] + '/' + d[5:7] + '/' + d[0:4] + d[10:]
        data = f"""
               {{
               "signup_time": {'"'}{signup_time}{'"'}, 
               "purchase_time": {'"'}{purchase_time}{'"'}, 
               "purchase_value": {row['purchase_value']}, 
               "device_id": {'"'}{row['device_id']}{'"'}, 
               "source": {'"'}{row['source']}{'"'}, 
               "browser": {'"'}{row['browser']}{'"'}, 
               "sex": {'"'}{row['sex']}{'"'}, 
               "age": {row['age']}, 
               "ip_address": {'"'}{row['ip_address']}{'"'}
               }}
               """

        resp = requests.post(url, headers=headers, data=data)

        assert resp.status_code == 200
