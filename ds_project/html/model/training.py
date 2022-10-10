import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pickle

categorical_cols = ['source', 'browser', 'sex', 'was_fraudulent_customer']
numerical_cols = ['age', 'cnt_purchase', 'sec_since_signup', 'sec_since_last_purchase']

def apply_ohe(ohe, df, cols):
    """
    applies pretrained OneHotEncoder to defined columns of a DataFrame

    :param ohe: pretrained OneHotEncoder
    :param df: DataFrame, equivalent to the df that ohe was trained on
    :param cols: Columns, equivalent to the df that ohe was trained on

    :return: onehotencoded dataframe
    """
    cat_ohe = ohe.transform(df[cols])

    # create a Pandas DataFrame of the hot encoded columns
    ohe_df = pd.DataFrame(cat_ohe, columns=ohe.get_feature_names_out(input_features=cols))
    # concat with original data and drop original columns
    return pd.concat([df, ohe_df], axis=1).drop(columns=categorical_cols, axis=1)

def apply_scaler(scaler, df, cols):
    """
    applies pretrained Scaler to defined columns of a DataFrame

    :param scaler: pretrained Scaler
    :param df: DataFrame, equivalent to the df that scaler was trained on
    :param cols: Columns, equivalent to the df that scaler was trained on
    :return: scaled dataframe
    """
    num_scaler = scaler.transform(df[cols])

    # create a Pandas DataFrame of the scaled columns
    scaler_df = pd.DataFrame(num_scaler, columns=cols)
    # concat with original data and drop original columns
    return df.loc[:, ~df.columns.isin(cols)].merge(scaler_df, left_index=True, right_index=True)

###################################################################################################
###################################################################################################

def train_model(categorical_cols: list, numerical_cols: list):
    """
    read training data and fit preprocessing and model; store OneHotEncoder, Scaler and Model as pickle files
    :param categorical_cols:
    :param numerical_cols:
    """
    df_train = pd.read_csv('./../data/fraud_train.csv',
                           dtype={'is_fraud': 'object',
                                  'source': 'category',
                                  'browser': 'category',
                                  'sex': 'category',
                                  'was_fraudulent_customer': 'category',
                                  'age': int,
                                  'cnt_purchase': int,
                                  'sec_since_signup': int,
                                  'sec_since_last_purchase': int
                                  },
                           index_col=0
                           )

    ###################################################################################################
    # Instantiate the OneHotEncoder Object
    ohe = OneHotEncoder(handle_unknown='ignore', sparse= False)
    # Apply ohe on data
    ohe.fit(df_train[categorical_cols])
    df_train = apply_ohe(ohe, df_train, categorical_cols)

    ###################################################################################################
    # Instantiate the StandardScaler Object
    scaler = StandardScaler()
    # Apply ohe on data
    scaler.fit(df_train[numerical_cols])
    df_train = apply_scaler(scaler, df_train, numerical_cols)

    ###################################################################################################
    # split X,y
    X = df_train.loc[:, df_train.columns != 'is_fraud']
    y = df_train['is_fraud']

    # train decision tree model
    tree_model = DecisionTreeClassifier(max_depth = 4, criterion = 'entropy')
    tree_model.fit(X, y)

    ###################################################################################################
    # write preprocessing and model to disk
    pickle.dump(ohe, open('_ohe.sav', 'wb'))
    pickle.dump(scaler, open('_scaler.sav', 'wb'))
    pickle.dump(tree_model, open('_tree_model.sav', 'wb'))


