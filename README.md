# aqa-academy-python-2024

# Coding rules

## Excluded folders

1. .venv folder - this is my virtual enviroment, how to install: https://docs.python.org/3/library/venv.html
2. Reports

In order to avoid conflicts during git push


## Dep updates

1. major libs version needs to be revisited once per month

## How to

1. Setup your env
    - create venv into .venv folder
    - Install deps from requirements.txt file

2. Before commit
    - run black tool - https://black.readthedocs.io/en/stable/usage_and_configuration/index.html
    - rum flake8 tool - https://flake8.pycqa.org/en/latest/index.html#quickstart
    - run isort tool - https://pycqa.github.io/isort/index.html

3. Run the tests
    - Execute 'pytest . -s -v' command staying in the root of the framework
    - To form a report execute 'pytest . -s -v --html=reports/report.html --self-contained-html' command

4. UI tests
    - library Selenium - https://www.selenium.dev/documentation/webdriver/getting_started/install_library/
    - library Webdriver Manager - https://pypi.org/project/webdriver-manager/ 

5. API tests
    - library requests - https://requests.readthedocs.io/en/latest/

## Structure of the framework

1. tests - folder for tests
2. reports - folder to store local reports
3. src/applications - folder for system under tests abstractions
4. src/config - folder for configuration of framework
5. src/heleprs - folder for single-use functions, etc