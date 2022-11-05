from .feature_engineering import cnt_purchase, sec_since_signup, sec_since_last_purchase
import pandas as pd
import numpy as np



data = {
    'device_id':['ABCDEFGH'],
    'cnt_purchase':[int(2)]
}
df_customer_hist = pd.DataFrame.from_dict(data).astype({'device_id': object, 'cnt_purchase':int})


def test_cnt_purchase(df_customer_hist):
    #The use cases:
    """New customer"""
    assert cnt_purchase('ZYXWVUT', False, df_customer_hist) == 1

    assert cnt_purchase('ABCDEFGH', False, df_customer_hist) == 1

    """Already existing customer"""
    assert cnt_purchase('ABCDEFGH', True, df_customer_hist) == 2


def test_sec_since_signup():



def test_sec_since_last_purchase():