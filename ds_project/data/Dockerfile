#
# Dockerfile : Fraud version2
# Image : Include all folders, files and scripts 
# Container :to be integrated in Docker-compose
#
# Christoph & Philippe DATASCIENTEST Fraud project@2022
# 
# docker build -t philippelerch68/ifdataapi:latest . 
# docker push philippelerch68/ifdataapi:latest

FROM python:3.9

COPY /data_raw /ds_project_fraud/data/data_raw
COPY /config.py /ds_project_fraud/data/config.py

COPY /dataapi.py /ds_project_fraud/data/dataapi.py

COPY /customer_hist.csv /ds_project_fraud/data/customer_hist.csv
COPY /fraud_raw.csv /ds_project_fraud/data/fraud_raw.csv
COPY /fraud_test_raw.csv /ds_project_fraud/data/fraud_test_raw.csv
COPY /fraud_train_raw.csv /ds_project_fraud/data/fraud_train_raw.csv
COPY /fraud_train.csv /ds_project_fraud/data/fraud_train.csv
COPY /prepare_raw_data.py /ds_project_fraud/data/prepare_raw_data.py
COPY /trns_data.csv /ds_project_fraud/data/trns_data.csv

COPY /__init__.py /ds_project_fraud/data/__init__.py

ADD requirements.txt ./ds_project_fraud/data

RUN apt-get update  && pip install -r ./ds_project_fraud/data/requirements.txt && pip install python-multipart


#EXPOSE 8001/TCP
EXPOSE 8002/TCP

WORKDIR /ds_project_fraud/data
