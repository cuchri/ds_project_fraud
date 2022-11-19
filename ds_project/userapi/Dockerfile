#
# Dockerfile : Fraud version2
# Image : Include all folders, files and scripts 
# Container :to be integrated in Docker-compose
#
# Christoph & Philippe DATASCIENTEST Fraud project@2022
# docker build -t philippelerch68/ifuserapi:latest . 
# docker push philippelerch68/ifuserapi:latest



FROM python:3.9

COPY /config.py /ds_project_fraud/config.py
COPY /userapi.py /ds_project_fraud/userapi.py
COPY /__init__.py /ds_project_fraud/__init__.py

ADD requirements.txt ./ds_project_fraud

RUN apt-get update  && pip install -r ./ds_project_fraud/requirements.txt && pip install python-multipart

EXPOSE 8000/TCP
#EXPOSE 8001/tcp

WORKDIR /ds_project_fraud
