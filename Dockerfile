#
# Dockerfile : Fraud version2
# Image : Include all folders, files and scripts 
# Container :to be integrated in Docker-compose
#
# Christoph & Philippe DATASCIENTEST Fraud project@2022
# 


FROM python:3.9

COPY /data /ds_project_fraud/data
COPY /model /ds_project_fraud/model
COPY /static /ds_project_fraud/static
COPY /templates /ds_project_fraud/templates
COPY /tests /ds_project_fraud/tests

COPY /config.py /ds_project_fraud/config.py
COPY /userinterface.py /ds_project_fraud/userinterface.py
COPY /userapi.py /ds_project_fraud/userapi.py
COPY /modelapi.py /ds_project_fraud/modelapi.py
COPY /dataapi.py /ds_project_fraud/dataapi.py

COPY /__init__.py /ds_project_fraud/__init__.py

ADD requirements.txt ./ds_project_fraud

RUN apt-get update  && pip install -r ./ds_project_fraud/requirements.txt && pip install python-multipart

EXPOSE 80/TCP
EXPOSE 8000/tcp
EXPOSE 8001/TCP
EXPOSE 8002/TCP

WORKDIR /ds_project_fraud
