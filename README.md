
# Mockup project for dataengineering certification @[![Datascientest](https://datascientest.com/de/wp-content/uploads/sites/8/2022/03/logo-2021-1.png)](https://github.com/DataScientest)


This project is developed as part of the dataengineering certification @ DataScientest. 
The project evaluates incoming transactions and classifies them into fraudulent and non-fraudulent transaction.
As starting point of, the following ressource was used: [fraud_transaction_data](https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/fraud.csv)

For a detailed description of used modules and functions see the [documentation](https://cuchri.github.io/ds_project_fraud/)


## Authors

- [@Christoph PUFFITSCH](https://github.com/cuchri)
- [@Philippe LERCH](https://github.com/philippelerch68)


## Process

![Processflow](https://raw.githubusercontent.com/cuchri/ds_project_fraud/ea8a80fac0751a10c188b33816bf0fc455750460/docs/source/processflow.png)

A donation is given by the user @Userinterface, the transaction data is passed by @Userapi to the @Modelapi where the `inputvalidation`, `customervalidation`, `fetureengineering` and finally the `classification` is performed. 
The prediction of the classification algorithm is returned by @Userapi and displayed in the @Userinterface.
Additionally raw transaction data as well as the classification result is sent to @Datapi and stored as .csv. 


## Deployment

To deploy this project, first install docker (+compose) and copy the file `ds_project/docker-compose.yml` on your host machine. Then run the following commands

```bash
  docker network create --subnet 172.30.0.0/16 --gateway 172.30.0.1 fraud_network_ip
  
  docker-compose up -d
```

To test the apis, run the following curl commands from your host machine.

```bash
  # Fraud detected
  curl -X POST -H 'accept: application/json' -d '{ "signup_time": "28/04/2015 21:13:25", "purchase_time": "28/04/2015 21:13:30","purchase_value": 34,"device_id": "AAAXXOZJRZRAO", "source": "SEO","browser": "Chrome","sex": "M", "age": 39, "ip_address": "732758368.8" }' http://localhost:8000/
  
  # No fraud detected
  curl -X POST -H 'accept: application/json' -d '{ "signup_time": "11/08/2015 13:13:25", "purchase_time": "11/08/2015 13:13:48","purchase_value": 78,"device_id": "QVPSPJUOCKXYZ", "source": "SEO","browser": "Chrome","sex": "F", "age": 25, "ip_address": "73486318684" }' http://localhost:8000/
```


## Tests

[Pytest](https://docs.pytest.org/) is used to define `unittests` on every part of the project. 
Additionally, an `integration test` is defined, that sends post requests to @Userapi and tests for the return status code.

The tests are run on every push/pull_request by [github actions](https://github.com/cuchri/ds_project_fraud/actions).

To run tests without github, the repository must be cloned on your host machine and then run

```bash
  python3 -m pytest
```
