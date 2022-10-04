from ds_project.model.classify import process_transaction, classify_transaction
from ds_project.model.training import categorical_cols, numerical_cols

import pickle
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "app is running"}


@app.post("/upload_transaction/")
async def classify(trns_dict: dict):

    # load preprocessing and model
    ohe = pickle.load(open('./../model/_ohe.sav', 'rb'))
    scaler = pickle.load(open('./../model/_scaler.sav', 'rb'))
    model = pickle.load(open('./../model/_tree_model.sav', 'rb'))

    # classify transaction data
    trns_dict = process_transaction(trns_dict)
    trns_dict = classify_transaction(trns_dict, ohe, scaler, model, categorical_cols, numerical_cols)

    print(trns_dict)


    return trns_dict['result']['is_classified_fraud']

