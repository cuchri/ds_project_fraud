from ..model.customer_validation import get_customer_hist, is_existing_customer, is_fraudulent_customer
import pandas as pd
import pytest
import os
import sys
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent
cust_hist_path = f"{BASE_PATH}/test_customer_hist.csv"


@pytest.fixture
def df_customer_hist():
    """Returns a test df of customer history"""
    data = {
        'device_id': ['ABCDEFGH', 'BCDEFGHI'],
        'is_fraudulent_customer': [True, False]
    }
    return pd.DataFrame.from_dict(data).astype({'device_id': object})


def test_get_customer_hist():
    assert isinstance(get_customer_hist(cust_hist_path), pd.DataFrame) == True
    #assert isinstance(get_customer_hist('tests/test_customer_hist.csv'), pd.DataFrame) == True


def test_is_existing_customer(df_customer_hist):
    # The use cases:
    """New customer"""
    assert is_existing_customer('ZYXWVUT', df_customer_hist) == False

    """Already existing customer"""
    assert is_existing_customer('ABCDEFGH', df_customer_hist) == True

    assert is_existing_customer('BCDEFGHI', df_customer_hist) == True


def test_is_fraudulent_customer(df_customer_hist):
    # The use cases:
    """New customer"""
    assert is_fraudulent_customer('ZYXWVUT', False, df_customer_hist) == False

    assert is_fraudulent_customer('ABCDEFGH', False, df_customer_hist) == False

    """Already existing customer"""
    assert is_fraudulent_customer('ABCDEFGH', True, df_customer_hist) == True

    assert is_fraudulent_customer('BCDEFGHI', True, df_customer_hist) == False

