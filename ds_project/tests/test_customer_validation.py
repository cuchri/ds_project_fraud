from ds_project.model.customer_validation import get_customer_hist, is_existing_customer, is_fraudulent_customer
import pandas as pd

data = {
    'device_id': ['ABCDEFGH']
}
df_customer_hist = pd.DataFrame.from_dict(data).astype({'device_id': object})


def test_is_existing_customer(df_customer_hist):
    # The use cases:
    """New customer"""
    assert is_existing_customer('ZYXWVUT', df_customer_hist) == False

    """Already existing customer"""
    assert is_existing_customer('ABCDEFGH', df_customer_hist) == True


def test_is_fraudulent_customer(df_customer_hist):
    # The use cases:
    """New customer"""
    assert cnt_purchase('ZYXWVUT', False, df_customer_hist) == False

    assert cnt_purchase('ABCDEFGH', False, df_customer_hist) == False

    """Already existing customer"""
    assert cnt_purchase('ABCDEFGH', True, df_customer_hist) == True

