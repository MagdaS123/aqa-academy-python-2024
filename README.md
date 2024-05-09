# aqa-academy-python-2024

# Coding rules

# Excluded folders
1. .venv folder - this is my virtual enviroment, how to install: https://docs.python.org/3/library/venv.html
2. Reports
In order to avoid conflicts during git push


# Dep updates
1. major libs version needs to be revisited once per month

# How to

1. Setup your env
    1.1 create venv into .venv folder
    1.2 Install deps from requirements.txt file

2. Before commit
    2.1 run black tool - https://black.readthedocs.io/en/stable/usage_and_configuration/index.html
    2.2 rum flake8 tool - https://flake8.pycqa.org/en/latest/index.html#quickstart
    2.3 run isort tool - https://pycqa.github.io/isort/index.html

3. Run the tests
    3.1. Execute 'pytest . -s -v' command staying in the root of the framework
    3.2. To form a report execute 'pytest . -s -v --html=reports/report.html --self-contained-html' command

# Structure of the framework

1. tests - folder for tests
2. reports - folder to store local reports
3. src/applications - folder for system under tests abstractions
4. src/config - folder for configuration of framework
5. src/heleprs - folder for single-use functions, etc