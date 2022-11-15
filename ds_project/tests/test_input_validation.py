from ..model.input_validation import is_valid_input, is_data_missing, is_dtypes_consistent, is_dates_consistent
from datetime import datetime
import pytest


@pytest.fixture
def trns_dict_good():
    """Returns a test df of customer history"""
    trns_dict_raw = {
            'signup_time': datetime(2015, 4, 28, 21, 13, 25),
            'purchase_time': datetime(2015, 4, 28, 21, 13, 30),
            'purchase_value': 34,
            'device_id': 'QVPSPJUOCKZAR',
            'source': 'SEO',
            'browser': 'Chrome',
            'sex': 'M',
            'age': 39,
            'ip_address': '732758368.8'
    }
    return trns_dict_raw


@pytest.fixture
def trns_dict_bad():
    """Returns a test df of customer history"""
    trns_dict_raw = {
            'signup_time': datetime(2015, 4, 28, 21, 13, 30),
            'purchase_time': datetime(2015, 4, 28, 21, 13, 25),
            'purchase_value': 34,
            'device_id': 1234,
            'source': 'SEO',
            'browser': 'Chrome',
            'age': 39,
            'ip_address': '732758368.8'
    }
    return trns_dict_raw

#is_valid_input
def test_is_valid_input_on_good_input(trns_dict_good):
    print(trns_dict_good)
    assert is_valid_input(trns_dict_good) == True

def test_is_valid_input_on_bad_input(trns_dict_bad):
    assert is_valid_input(trns_dict_bad) == False


#is_data_missing
def test_is_data_missing_on_good_input(trns_dict_good):
    assert is_data_missing(trns_dict_good) == True

def test_is_data_missing_on_bad_input(trns_dict_bad):
    assert is_data_missing(trns_dict_bad) == False


#is_dtypes_consistent
def test_is_dtypes_consistent_on_good_input(trns_dict_good):
    assert is_dtypes_consistent(trns_dict_good) == True

def test_is_dtypes_consistent_on_bad_input(trns_dict_bad):
    assert is_dtypes_consistent(trns_dict_bad) == False


#is_dates_consistent
def test_is_dates_consistent_on_good_input(trns_dict_good):
    assert is_dates_consistent(trns_dict_good['signup_time'], trns_dict_good['purchase_time']) == True

def test_is_dates_consistent_on_bad_input(trns_dict_bad):
    assert is_dates_consistent(trns_dict_bad['signup_time'], trns_dict_bad['purchase_time']) == False
