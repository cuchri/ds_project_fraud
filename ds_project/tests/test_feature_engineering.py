from ds_project.model.feature_engineering import cnt_purchase, sec_since_signup, sec_since_last_purchase
import pandas as pd
import numpy as np
from datetime import datetime


data = {
    'device_id': ['ABCDEFGH'],
    'dt_purchase': '2015-04-28 21:13:25',
    'cnt_purchase': [int(2)]
}
df_customer_hist = pd.DataFrame.from_dict(data).astype({'device_id': object, 'cnt_purchase':int})


def test_cnt_purchase(df_customer_hist):
    # The use cases:
    """New customer"""
    assert cnt_purchase('ZYXWVUT', False, df_customer_hist) == 1

    assert cnt_purchase('ABCDEFGH', False, df_customer_hist) == 1

    """Already existing customer"""
    assert cnt_purchase('ABCDEFGH', True, df_customer_hist) == 2


def test_sec_since_signup():
    # The use cases:
    """dt_signup == dt_purchase"""
    assert sec_since_signup(datetime(2015, 4, 28, 21, 13, 25), datetime(2015, 4, 28, 21, 13, 25)) == 0
    """dt_signup < dt_purchase"""
    assert sec_since_signup(datetime(2015, 4, 28, 21, 13, 25), datetime(2015, 4, 28, 21, 13, 30)) == 5

    # The edge cases:
    """dt_signup > dt_purchase"""
    assert sec_since_signup(datetime(2015, 4, 28, 21, 13, 30), datetime(2015, 4, 28, 21, 13, 25)) == 0


def test_sec_since_last_purchase():
    # The use cases:
    """New customer"""
    assert sec_since_last_purchase('ZYXWVUT', datetime(2015, 4, 28, 21, 13, 30), False, df_customer_hist) == 0

    assert sec_since_last_purchase('ABCDEFGH', datetime(2015, 4, 28, 21, 13, 30), False, df_customer_hist) == 0

    """Already existing customer"""
    assert sec_since_last_purchase('ABCDEFGH', datetime(2015, 4, 28, 21, 13, 30), True, df_customer_hist) == 5
