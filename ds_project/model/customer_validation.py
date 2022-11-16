import pandas as pd

def get_customer_hist(path) -> pd.DataFrame:
    """
    import table with customer purchase history

    :param path: path to the csv file
    :return: df
    """
    customer_hist = pd.read_csv(path,
                                dtype={'device_id': object,
                                  'is_fraudulent_customer': 'category',
                                  'cnt_purchase': int,
                                  },
                                parse_dates=['purchase_time'],
                                index_col=0
                           )
    return customer_hist


def is_existing_customer(device_id: str, customer_hist: pd.DataFrame) -> bool:
    """
    Lookup if device_id is present in customer history data

    :param device_id: identifyer of an individual customer
    :param customer_hist: DataFrame of individual customer purchase history

    :return: True if device_id is in DataFrame, else False
    """

    return device_id in customer_hist['device_id'].values


def is_fraudulent_customer(device_id: str, is_existing_cust: bool, customer_hist: pd.DataFrame) -> bool:
    """
        Lookup if a fraudulent transaction is found in customer history

        :param device_id: identifier of an individual customer
        :param is_existing_cust: True if customer has purchase history
        :param customer_hist: DataFrame of individual customer purchase history

        :return: True if device_id is in DataFrame, else False
    """

    if is_existing_cust:
        return customer_hist[customer_hist['device_id'] == device_id]['is_fraudulent_customer'].values[0]
    else:
        return False
