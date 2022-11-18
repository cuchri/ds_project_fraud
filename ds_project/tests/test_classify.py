from ..model.classify import process_transaction, classify_transaction
from datetime import datetime
import pytest


cust_hist_path = 'ds_project/tests/test_customer_hist.csv'
#cust_hist_path = 'tests/test_customer_hist.csv'


@pytest.fixture
def trns_dict_good_existingcust_nofraud():
    """Returns a test df of customer history"""
    trns_dict = {
        'raw': {
            'signup_time': datetime(2015, 4, 28, 21, 13, 25),
            'purchase_time': datetime(2015, 4, 28, 21, 13, 30),
            'purchase_value': 34,
            'device_id': 'AAALBGNHHVMKG',
            'source': 'SEO',
            'browser': 'Chrome',
            'sex': 'M',
            'age': 39,
            'ip_address': '732758368.8'
        }
    }
    return trns_dict


@pytest.fixture
def trns_dict_good_existingcust_isfraud():
    """Returns a test df of customer history"""
    trns_dict = {
        'raw': {
            'signup_time': datetime(2015, 4, 28, 21, 13, 25),
            'purchase_time': datetime(2015, 4, 28, 21, 13, 30),
            'purchase_value': 34,
            'device_id': 'AAAXXOZJRZRAO',
            'source': 'SEO',
            'browser': 'Chrome',
            'sex': 'M',
            'age': 39,
            'ip_address': '732758368.8'
        }
    }
    return trns_dict


@pytest.fixture
def trns_dict_good_newcust():
    """Returns a test df of customer history"""
    trns_dict = {
        'raw': {
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
    }
    return trns_dict

@pytest.fixture
def trns_dict_bad():
    """Returns a test df of customer history"""
    trns_dict = {
        'raw': {
            'signup_time': datetime(2015, 4, 28, 21, 13, 30),
            'purchase_time': datetime(2015, 4, 28, 21, 13, 25),
            'purchase_value': 34,
            'device_id': 'QVPSPJUOCKZAR',
            'source': 'SEO',
            'browser': 'Chrome',
            'sex': '',
            'age': 39,
            'ip_address': '732758368.8'
        }
    }
    return trns_dict


#process_transaction
def test_process_transaction_on_good_input_existingcust_nofraud(trns_dict_good_existingcust_nofraud):
    d = trns_dict_good_existingcust_nofraud
    process_transaction(d, cust_hist_path)
    assert d.get('is_valid_input') == True
    assert d.get('is_existing_customer') == True
    assert d.get('is_fraudulent_customer') == False
    assert d.get('feature').get('cnt_purchase') == 2
    assert d.get('feature').get('sec_since_signup') == 5
    assert d.get('feature').get('sec_since_last_purchase') == 3605


def test_process_transaction_on_good_input_existingcust_isfraud(trns_dict_good_existingcust_isfraud):
    d = trns_dict_good_existingcust_isfraud
    process_transaction(d, cust_hist_path)
    assert d.get('is_valid_input') == True
    assert d.get('is_existing_customer') == True
    assert d.get('is_fraudulent_customer') == True
    assert d.get('feature').get('cnt_purchase') == 10
    assert d.get('feature').get('sec_since_signup') == 5
    assert d.get('feature').get('sec_since_last_purchase') == 3605


def test_process_transaction_on_good_input_newcust(trns_dict_good_newcust):
    d = trns_dict_good_newcust
    process_transaction(d, cust_hist_path)
    assert d.get('is_valid_input') == True
    assert d.get('is_existing_customer') == False
    assert d.get('is_fraudulent_customer') == False
    assert d.get('feature').get('cnt_purchase') == 1
    assert d.get('feature').get('sec_since_signup') == 5
    assert d.get('feature').get('sec_since_last_purchase') == 0


def test_process_transaction_on_bad_input(trns_dict_bad):
    with pytest.raises(Exception):
        d = trns_dict_bad
        process_transaction(d, cust_hist_path)


