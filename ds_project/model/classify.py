from .input_validation import is_valid_input
from .customer_validation import is_existing_customer, is_fraudulent_customer
from .feature_engineering import cnt_purchase, sec_since_signup, sec_since_last_purchase
from ..data.customer import customer_hist
from .training import apply_ohe, apply_scaler

import pandas as pd


def process_transaction(trns_dict: dict) -> dict:
    """
    Evaluates webshop transactions
    :param transaction_data: raw transaction dictionary
    :return transaction_data: enhanced transaction dictionary
    """

    trns_dict['is_valid_input'] = is_valid_input(trns_dict)

    if trns_dict['is_valid_input']:
        # get historic customer information
        trns_dict['is_existing_customer'] = is_existing_customer(trns_dict.get('raw').get('device_id'),
                                                                 customer_hist)
        trns_dict['is_fraudulent_customer'] = is_fraudulent_customer(trns_dict.get('raw').get('device_id'),
                                                                     trns_dict.get('is_existing_customer'),
                                                                     customer_hist)

        # derive new customer specific features
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


def classify_transaction(trns_dict: dict, ohe, scaler, model, categorical_cols, numerical_cols) -> dict:
    """
    Applies the classification model on the individual transaction
    :param trns_dict: raw transaction dictionary
    :param ohe: fitted OneHotEncoder
    :param scaler: fitted StandardScaler
    :param model: fitted Classification Model
    :param categorical_cols: list of categorical features to include in the model input
    :param numerical_cols: list of numerical features to include in the model input
    :return: transaction_data: enhanced transaction dictionary
    """

    if trns_dict['is_fraudulent_customer']:
        # model is not applied -> transaction is labeled as fraud
        trns_dict['result']['is_classified_fraud'] = True

    else:
        # apply preprocessing
        d = {
            'device_id': trns_dict.get('raw').get('device_id'),
            'source': trns_dict.get('raw').get('source'),
            'browser': trns_dict.get('raw').get('browser'),
            'sex': trns_dict.get('raw').get('sex'),
            'was_fraudulent_customer': trns_dict.get('is_fraudulent_customer'),
            'age': trns_dict.get('raw').get('age'),
            'cnt_purchase': trns_dict.get('feature').get('cnt_purchase'),
            'sec_since_signup': trns_dict.get('feature').get('sec_since_signup'),
            'sec_since_last_purchase': trns_dict.get('feature').get('sec_since_last_purchase')
        }
        df_trns = pd.DataFrame.from_dict(d)
        df_trns = apply_ohe(ohe, df_trns, categorical_cols)
        df_trns = apply_scaler(scaler, df_trns, numerical_cols)

        # apply model
        classify_trns = model.predict(df_trns)
        if classify_trns[0] == '1':
            trns_dict['result']['is_classified_fraud'] = True
        else:
            trns_dict['result']['is_classified_fraud'] = False

    return trns_dict
