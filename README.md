
# Mockup project for dataengineering certification @[![Datascientest](https://datascientest.com/de/wp-content/uploads/sites/8/2022/03/logo-2021-1.png)](https://github.com/DataScientest)


This project is developed as part of the dataengineering certification @ DataScientest. 
The project evaluates incoming transactions and classifies them into fraudulent and non-fraudulent transaction.
As starting point of, the following ressource was used: [fraud_transaction_data](https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/fraud.csv)



## Authors

- [@Christoph PUFFITSCH](https://github.com/cuchri)
- [@Philippe LERCH](https://github.com/philippelerch68)


## Process

![Processflow](https://raw.githubusercontent.com/cuchri/ds_project_fraud/ea8a80fac0751a10c188b33816bf0fc455750460/docs/source/processflow.png)

A donation is given by the user @Userinterface, the transaction data is passed by @Userapi to the @Modelapi where the `inputvalidation`, `customervalidation`, `fetureengineering` and finally the `classification` is performed. 
The prediction of the classification algorithm is returned by @Userapi and displayed in the @Userinterface.
Additionally raw transaction data as well as the classification result is sent to @Datapi and stored as .csv. 


## Deployment

To deploy this project run

```bash
  npm run deploy

  
```


## Tests

[Pytest](https://docs.pytest.org/) is used to define `unittests` on every part of the project. 
Additionally, an `integration test` is defined, that sends post requests to @Userapi and tests for the return status code.

The tests are run on every push/pull_request by [github actions](https://github.com/cuchri/ds_project_fraud/actions).
