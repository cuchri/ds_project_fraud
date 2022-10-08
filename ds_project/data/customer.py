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
                                parse_dates='purchase_time',
                           )
    return customer_hist


