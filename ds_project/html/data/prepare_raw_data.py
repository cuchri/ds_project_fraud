import pandas as pd

# load data from web
df = pd.read_csv('https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/fraud.csv',
                 parse_dates=['signup_time', 'purchase_time'],
                 dtype={'ip_address': str,
                        'source': 'category',
                        'browser': 'category',
                        'sex': 'category',
                        'is_fraud': 'object'
                        },
                 )

# split train set
n80 = 120889

df_train_raw = df.iloc[:n80]
df_test_raw = df.iloc[n80:]

## train
# derive new columns out of device_id, signup_time and purchase_time
df_train = df_train_raw.copy()
df_train['sec_since_signup'] = (df_train['purchase_time'] - df_train['signup_time']).dt.total_seconds().fillna(0).astype(int)

df_train = df_train.sort_values(['device_id', 'purchase_time'], ascending=[True, True])
df_train['cnt_purchase'] = df_train.groupby('device_id').cumcount() + 1

df_train['sec_since_last_purchase'] = df_train.groupby(['device_id'])['purchase_time'].diff().dt.total_seconds().fillna(0).astype(int)

df_train['is_fraudulent'] = df_train.astype({'is_fraud': int}).groupby(['device_id'])['is_fraud'].cummax().astype("category")
df_train['is_fraudulent_customer'] = df_train.groupby(['device_id'])['is_fraudulent'].shift(0).fillna(0)
df_train['was_fraudulent_customer'] = df_train.groupby(['device_id'])['is_fraudulent'].shift(1).fillna(0)
df_train = df_train.drop('is_fraudulent', axis=1)

# create customer history out of train set
df_customer_hist = df_train[['device_id', 'is_fraudulent_customer', 'cnt_purchase', 'purchase_time']].groupby('device_id').tail(1).drop_duplicates().sort_values('device_id')

# based on the analysis of correlation, select the following features
cat_include = ['is_fraud', 'source', 'browser', 'sex', 'was_fraudulent_customer']
num_include = ['age', 'cnt_purchase', 'sec_since_signup', 'sec_since_last_purchase']
df_train = df_train[cat_include + num_include]


# write data to disk
df.to_csv('./fraud_raw.csv')
df_train_raw.to_csv('./fraud_train_raw.csv')
df_test_raw.to_csv('./fraud_test_raw.csv')
df_customer_hist.to_csv('./customer_hist.csv')
df_train.to_csv('./fraud_train.csv')
