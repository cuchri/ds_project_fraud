import datetime


def is_valid_input(raw_data: dict) -> bool:
    """
    Evaluates raw transaction data

    :param raw_data: dictionary of transation data of a single purchase
    :return: True if data is consistent, False if data is corrupted
    """

    is_data_missing_b = is_data_missing(raw_data)
    is_dtypes_consistent_b = is_dtypes_consistent(raw_data)
    is_dates_consistent_b = is_dates_consistent(raw_data)

    return all(is_data_missing_b,
               is_dtypes_consistent_b,
               is_dates_consistent_b)


def is_data_missing(raw_data: dict) -> bool:
    """
    Tests for missing data

    :param raw_data: original data dict

    :return: True if all values are present, else False
    """

    return True


def is_dtypes_consistent(raw_data: dict) -> bool:
    """

    :param raw_data: original data dict
    :return: True if all values are present, else False
    """

    return True


def is_dates_consistent(dt_signup: datetime, dt_purchase: datetime) -> bool:
    """
    Tests for consistency of timestamps of a transaction
    :param dt_signup: timestamp of signup for specific transaction
    :param dt_purchase: timestamp of purchase for specific transaction
    :return: True if timestamps are consistent, else False
    """

    return True
