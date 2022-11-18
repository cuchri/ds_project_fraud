from ..model.classify import process_transaction, classify_transaction
from datetime import datetime
import pytest

#34321,AAALBGNHHVMKG,0,1,2015-06-13 23:42:18
#97331,AAAXXOZJRZRAO,1,9,2015-01-28 10:39:35

@pytest.fixture
def trns_dict_good_existingcust_nofraud():
    """Returns a test df of customer history"""
    trns_dict = {
        'raw': {
            'signup_time': datetime(2015, 7, 28, 21, 13, 25),
            'purchase_time': datetime(2015, 7, 28, 21, 13, 30),
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
            'signup_time': datetime(2015, 7, 28, 21, 13, 25),
            'purchase_time': datetime(2015, 7, 28, 21, 13, 30),
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
            'signup_time': datetime(2015, 7, 28, 21, 13, 25),
            'purchase_time': datetime(2015, 7, 28, 21, 13, 30),
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
def test_process_transaction_on_good_input(trns_dict_good_existingcust_nofraud):
    process_transaction(trns_dict_good_existingcust_nofraud, cust_hist_path='ds_project/tests/test_customer_hist.csv')
    #process_transaction(trns_dict_good_existingcust_nofraud, cust_hist_path='tests/test_customer_hist.csv')
    assert trns_dict_good_existingcust_nofraud.get('is_valid_input') == True
    #assert trns_dict_good.get('is_existing_customer') == True
    #assert trns_dict_good.get('is_fraudulent_customer') == False
    #assert trns_dict_good.get('feature').get('cnt_purchase') == 2
    #assert trns_dict_good.get('feature').get('sec_since_signup') == 5
    #assert trns_dict_good.get('feature').get('sec_since_last_purchase') == 120

#def test_process_transaction_on_bad_input(trns_dict_bad):
#    process_transaction(trns_dict_bad, cust_hist_path='ds_project/tests/test_customer_hist.csv')
#    assert trns_dict_bad.get('is_valid_input') == False
#    assert ('is_existing_customer' in trns_dict_bad.keys()) == False
#    assert ('is_fraudulent_customer' in trns_dict_bad.keys()) == False
#    assert ('cnt_purchase' in trns_dict_bad.feature.keys()) == False
#    assert ('sec_since_signup' in trns_dict_bad.feature.keys()) == False
#    assert ('sec_since_last_purchase' in trns_dict_bad.feature.keys()) == False


    #
    # trns_dict['is_valid_input'] = is_valid_input(trns_dict.get('raw'))
    #
    # if trns_dict['is_valid_input']:
    #     # get historic customer information
    #     trns_dict['is_existing_customer'] = is_existing_customer(trns_dict.get('raw').get('device_id'),
    #                                                              customer_hist)
    #     trns_dict['is_fraudulent_customer'] = is_fraudulent_customer(trns_dict.get('raw').get('device_id'),
    #                                                                  trns_dict.get('is_existing_customer'),
    #                                                                  customer_hist)
    #
    #     # derive new customer specific features
    #     trns_dict['feature'] = {}
    #     trns_dict['feature']['cnt_purchase'] = cnt_purchase(trns_dict.get('raw').get('device_id'),
    #                                                         trns_dict.get('is_existing_customer'),
    #                                                         customer_hist)
    #     trns_dict['feature']['sec_since_signup'] = sec_since_signup(trns_dict.get('raw').get('signup_time'),
    #                                                                 trns_dict.get('raw').get('purchase_time'))
    #     trns_dict['feature']['sec_since_last_purchase'] = sec_since_last_purchase(trns_dict.get('raw').get('device_id'),
    #                                                                               trns_dict.get('raw').get(
    #                                                                                   'purchase_time'),
    #                                                                               trns_dict.get('is_existing_customer'),
    #                                                                               customer_hist)