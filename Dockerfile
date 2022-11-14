#
# Dockerfile : Fraud version2
# Image : Include all folders and files 
# Container :to be integrated in Docker-compose
#
# Christoph & Philippe DATASCIENTEST Fraud project@2022
# 


FROM python:3.9

COPY ds_project/data /ds_project_fraud/data
COPY ds_project/html /ds_project_fraud/html
COPY ds_project/model /ds_project_fraud/model
COPY ds_project/main.py /ds_project_fraud/main.py
COPY ds_project/__init__.py /ds_project_fraud/__init__.py

ADD requirements.txt ./ds_project_fraud

RUN apt-get update  && pip install -r ./ds_project_fraud/requirements.txt && pip install python-multipart

EXPOSE 8000/tcp
EXPOSE 80/TCP

WORKDIR /ds_project_fraud

#CMD uvicorn  /ds_project_fraud/main:app --host 0.0.0.0
CMD [ "python","./main.py" ]