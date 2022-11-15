from datetime import datetime


def is_valid_input(raw_data: dict) -> bool:
    """
    Evaluates raw transaction data

    :param raw_data: dictionary of transation data of a single purchase
    :return: True if data is consistent, False if data is corrupted
    """

    is_data_missing_b = is_data_missing(raw_data)
    is_dtypes_consistent_b = is_dtypes_consistent(raw_data)
    is_dates_consistent_b = is_dates_consistent(raw_data.get('signup_time'), raw_data.get('purchase_time'))
    is_True = [is_data_missing_b, is_dtypes_consistent_b, is_dates_consistent_b]

    return all(is_True)


def is_data_missing(raw_data: dict) -> bool:
    """
    Tests for missing data

    :param raw_data: original data dict

    :return: True if all values are present, else False
    """
    all_values = False
    if raw_data.get('signup_time'):
        if raw_data.get('purchase_time'):
            if raw_data.get('purchase_value'):
                if raw_data.get('device_id'):
                    if raw_data.get('source'):
                        if raw_data.get('browser'):
                            if raw_data.get('sex'):
                                if raw_data.get('age'):
                                    if raw_data.get('ip_address'):
                                        all_values = True
    return all_values


def is_dtypes_consistent(raw_data: dict) -> bool:
    """

    :param raw_data: original data dict
    :return: True if all values are present, else False
    """
    consistent_dtypes = False
    if isinstance(raw_data.get('signup_time', datetime(2015, 1, 1, 1, 1, 1)), datetime):
        if isinstance(raw_data.get('purchase_time', datetime(2015, 1, 1, 1, 1, 1)), datetime):
            if isinstance(raw_data.get('purchase_value', 0), int):
                if isinstance(raw_data.get('device_id', 'ABCDEFGH'), str):
                    if isinstance(raw_data.get('source', 'ABC'), str):
                        if isinstance(raw_data.get('browser', 'ABC'), str):
                            if isinstance(raw_data.get('sex', 'M'), str):
                                if isinstance(raw_data.get('age', 0), int):
                                    if isinstance(raw_data.get('ip_address', '1234'), str):
                                        consistent_dtypes = True
    return consistent_dtypes


def is_dates_consistent(dt_signup: datetime, dt_purchase: datetime) -> bool:
    """
    Tests for consistency of timestamps of a transaction
    :param dt_signup: timestamp of signup for specific transaction
    :param dt_purchase: timestamp of purchase for specific transaction
    :return: True if timestamps are consistent, else False
    """

    consistent_dates = False
    if int((dt_purchase - dt_signup).total_seconds()) >= 0:
        consistent_dates = True
    return consistent_dates
