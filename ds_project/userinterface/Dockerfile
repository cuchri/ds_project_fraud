#
# Dockerfile : Fraud version2
# Image : Include all folders, files and scripts 
# Container :to be integrated in Docker-compose
#
# Christoph & Philippe DATASCIENTEST Fraud project@2022
# docker build -t philippelerch68/ifuserinterface:latest . 
# docker push philippelerch68/ifuserinterface:latest



FROM python:3.9

COPY /static /ds_project_fraud/static
COPY /templates /ds_project_fraud/templates

COPY /config.py /ds_project_fraud/config.py
COPY /userinterface.py /ds_project_fraud/userinterface.py
COPY /__init__.py /ds_project_fraud/__init__.py

ADD requirements.txt ./ds_project_fraud

RUN apt-get update  && pip install -r ./ds_project_fraud/requirements.txt && pip install python-multipart

EXPOSE 80/TCP
EXPOSE 8000/tcp

WORKDIR /ds_project_fraud
