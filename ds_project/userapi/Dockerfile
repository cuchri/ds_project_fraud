#
# Dockerfile : Fraud phase2
# Image : Include all folders and files 
# userinterface
#
# Christoph & Philippe DATASCIENTEST Fraud project@2022
# 

FROM python:3.9

COPY ./templates /ds_project_fraud/templates
COPY ./static /ds_project_fraud/static
COPY ./model /ds_project_fraud/model
COPY ./userapi.py /ds_project_fraud/userapi.py

ADD ./requirements.txt ./ds_project_fraud

RUN apt-get update  && pip install -r ./ds_project_fraud/requirements.txt && pip install python-multipart

EXPOSE 80/TCP

WORKDIR /ds_project_fraud

#CMD uvicorn  /ds_project_fraud/userinterface:app --host 0.0.0.0
CMD [ "python",".userapi.py" ]