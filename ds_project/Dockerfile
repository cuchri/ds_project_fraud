#
# Dockerfile : Fraud version2
# Image : Include all folders, files and scripts 
# Container :to be integrated in Docker-compose
#
# Christoph & Philippe DATASCIENTEST Fraud project@2022
# 
# docker build -t philippelerch68/ifmodelapi:latest . 
# docker push philippelerch68/ifmodelapi:latest

FROM python:3.9

COPY /data /ds_project_fraud/data
COPY /model /ds_project_fraud/model

COPY /config.py /ds_project_fraud/config.py

COPY /modelapi.py /ds_project_fraud/modelapi.py

COPY /__init__.py /ds_project_fraud/__init__.py

ADD requirements.txt ./ds_project_fraud

RUN apt-get update  && pip install -r ./ds_project_fraud/requirements.txt && pip install python-multipart


EXPOSE 8001/TCP
EXPOSE 8002/TCP

WORKDIR /ds_project_fraud
