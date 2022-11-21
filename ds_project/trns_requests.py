import pandas as pd
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime

path = 'tests/sample_requests.csv'
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
                              #parse_dates=['signup_time', 'purchase_time'],
                              index_col=0
                              )

df_transactions = df_transactions.reset_index()  # make sure indexes pair with number of rows
print(df_transactions.head())

url = "http://localhost:8000/"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

for index, row in df_transactions.iterrows():
    d = row['signup_time']
    signup_time = d[8:10]+'/'+d[5:7]+'/'+d[0:4]+d[10:]
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
    #cdprint(data)
    resp = requests.post(url, headers=headers, data=data)
    print("index: ", index, 'status_code: ', resp.status_code)

#results of classification can be found in 'data/trns_data.csv'


