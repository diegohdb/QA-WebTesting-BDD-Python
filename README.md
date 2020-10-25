<h1 align="left">:computer: QA-WebTesting-BDD-Python  </h1>

Web testing project using BDD, Selenium and Python

## Introduction
This project contains an automated suite for the web application <a href="http://165.227.93.41/lojinha-web/"> Lojinha </a> present in the course Teste De Software Para Iniciantes (TSPI) instructed by <a href="https://www.juliodelima.com.br/"> Julio de Lima</a>. 

The structure was based on Page Object using BDD (Behave lib), Selenium and Python. The results generates the screenshot of failures and a report is generated in a friendly dashboard through <a href="https://pypi.org/project/allure-behave/">allure</a>.

The suite will cover the main web application user behavior, including login, product and component features with different scenarios. 

## Environment Setup
**Prerequisites:** 
* Python 3+ 
* pip3


1. Clone the project

2. Create and activate a virtualenv:
```
virtualenv --python=/usr/bin/python3.7 bdd_python 
```
```
source bdd_python/bin/activate
```

3. To install the required dependencies issue the below command in project root directory.
```
pip3 install -r requirements.txt
```

## How to run?

- Run the whole suite without generate a report:

Issue the below commands in project root directory :
```
behave ./features/
```

- Run specific feature: 

Issue the below commands in project root directory
```
behave features/products.feature
```

- Run the whole suite with report generation:

Issue the below commands in project root directory:
```
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
```
_A folder reports will be created with the results for each scenario in a JSON._


- Generate the dashboard with the results:
Issue the below commands in project root directory:
```
allure_behave serve reports/
```




## Author
<a target="_blank" href="https://github.com/diegohdb/diegohdb">👤 Diego Bezerra </a>

<a target="_blank" href="https://www.linkedin.com/in/diegohdb/">
  <img align="left" alt="LinkdeIN" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a target="_blank" href="https://www.instagram.com/diegohdb/">
  <img align="left" alt="Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
<a target="_blank" href="mailto:diegohdb@gmail.com">
  <img align="left" alt="Gmail" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/gmail.svg" />
</a>

