from .input_validation import is_valid_input
from .customer_validation import get_customer_hist, is_existing_customer, is_fraudulent_customer
from .feature_engineering import cnt_purchase, sec_since_signup, sec_since_last_purchase
from .training import apply_ohe, apply_scaler, categorical_cols, numerical_cols

import pandas as pd
import pickle


def process_transaction(trns_dict: dict) -> dict:
    """
    Evaluates webshop transactions

    :param trns_dict: raw transaction dictionary
    :return trns_dict: enhanced transaction dictionary
    """
    # TODO replace customer_hist by load of csv
    # customer_hist = get_customer_hist('customer_hist.csv')
    customer_hist = pd.DataFrame([['AAALBGNHHVMKG', '0', 1, '2015-06-13 23:42:18'],
                                  ['AAAWIHVCQELTP', '0', 1, '2015-03-29 00:39:07']],
                                 columns=['device_id', 'is_fraudulent_customer', 'cnt_purchase', 'purchase_time'])

    trns_dict['is_valid_input'] = is_valid_input(trns_dict)

    if trns_dict['is_valid_input']:
        # get historic customer information
        trns_dict['is_existing_customer'] = is_existing_customer(trns_dict.get('raw').get('device_id'),
                                                                 customer_hist)
        trns_dict['is_fraudulent_customer'] = is_fraudulent_customer(trns_dict.get('raw').get('device_id'),
                                                                     trns_dict.get('is_existing_customer'),
                                                                     customer_hist)

        # derive new customer specific features
        trns_dict['feature'] = {}
        trns_dict['feature']['cnt_purchase'] = cnt_purchase(trns_dict.get('raw').get('device_id'),
                                                            trns_dict.get('is_existing_customer'),
                                                            customer_hist)
        trns_dict['feature']['sec_since_signup'] = sec_since_signup(trns_dict.get('raw').get('signup_time'),
                                                                    trns_dict.get('raw').get('purchase_time'))
        trns_dict['feature']['sec_since_last_purchase'] = sec_since_last_purchase(trns_dict.get('raw').get('device_id'),
                                                                                  trns_dict.get('raw').get(
                                                                                      'purchase_time'),
                                                                                  trns_dict.get('is_existing_customer'),
                                                                                  customer_hist)
    return trns_dict


def classify_transaction(trns_dict: dict, ohe, scaler, model) -> dict:
    """
    Applies the classification model on the individual transaction

    :param trns_dict: raw transaction dictionary
    :return: trns_dict: enhanced transaction dictionary
    """

    trns_dict['result'] = {}

    if trns_dict['is_fraudulent_customer']:
        # model is not applied -> transaction is labeled as fraud
        trns_dict['result']['is_classified_fraud'] = True

    else:
        # apply preprocessing
        data = [[trns_dict.get('raw').get('source'),
                 trns_dict.get('raw').get('browser'),
                 trns_dict.get('raw').get('sex'),
                 str(int(True == trns_dict.get('is_fraudulent_customer'))),
                 trns_dict.get('raw').get('age'),
                 trns_dict.get('feature').get('cnt_purchase'),
                 trns_dict.get('feature').get('sec_since_signup'),
                 trns_dict.get('feature').get('sec_since_last_purchase')
                 ]]

        cols = [
            'source', 'browser', 'sex', 'was_fraudulent_customer', 'age', 'cnt_purchase',
            'sec_since_signup', 'sec_since_last_purchase'
        ]

        df_trns = pd.DataFrame(data, columns=cols)
        print(df_trns)
        print(df_trns.info())
        df_trns = apply_ohe(ohe, df_trns, categorical_cols)
        df_trns = apply_scaler(scaler, df_trns, numerical_cols)

        # apply model
        classify_trns = model.predict(df_trns)
        if classify_trns[0] == '1':
            trns_dict['result']['is_classified_fraud'] = True
        else:
            trns_dict['result']['is_classified_fraud'] = False

    return trns_dict
