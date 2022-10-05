import pandas as pd
from datetime import datetime


def cnt_purchase(device_id: str, is_existing_cust: bool, customer_hist: pd.DataFrame) -> int:
    """
    adding 1 to the number of historic purchases by a customer
    :param device_id: identifier of an individual customer
    :param is_existing_cust: True if customer has purchase history
    :param customer_hist: DataFrame of individual customer purchase history
    :return: cnt of puchases by customer
    """
    if is_existing_cust:
        return customer_hist[['device_id'] == device_id]['cnt_purchase'] + 1
    else:
        return 1


def sec_since_signup(dt_signup: datetime, dt_purchase: datetime) -> int:
    """
    derives the time elapsed between signup and purchase for current transaction
    :param dt_signup: timestamp of signup for specific transaction
    :param dt_purchase: timestamp of purchase for specific transaction
    :return: time elapsed in seconds
    """

    if dt_purchase == dt_signup:
        return 0
    else:
        return (dt_purchase - dt_signup).total_seconds()


def sec_since_last_purchase(device_id: str, dt_purchase: datetime, is_existing_cust: bool,
                            customer_hist: pd.DataFrame) -> int:
    """
    derives the time elapsed since the last purchase of a customer
    :param device_id: identifier of an individual customer
    :param dt_purchase: timestamp of purchase for specific transaction
    :param is_existing_cust: True if customer has purchase history
    :param customer_hist: DataFrame of individual customer purchase history
    :return: time elapsed in seconds
    """

    if not is_existing_cust:
        return 0
    else:
        dt_last_purchase = customer_hist[['device_id'] == device_id]['dt_last_purchase']
        return (dt_purchase - dt_last_purchase).total_seconds()


