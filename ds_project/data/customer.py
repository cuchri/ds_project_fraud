import pandas as pd

customer_hist = pd.read_csv('./customer_hist.csv',
                            dtype={'device_id': object,
                              'is_fraudulent_customer': 'category',
                              'cnt_purchase': int,
                              },
                            parse_dates='purchase_time',
                       )