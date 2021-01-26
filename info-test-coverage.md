# Testing Coverage

Testing is vital to the success of your code. Without properly testing your code, you will never know if the code works as it should, now or in the future when the codebase changes. Without testing you may not even know that there are problems at all until your end users complain about it - which is obviously not ideal.

## Using Coverage

Code coverage describes how much source code has been tested. It shows which parts of your code are being exercised by tests and which are not. It’s an important part of testing applications, so it’s strongly recommended to check the coverage of your tests.

## django-coverage

A test coverage reporting tool that utilizes Ned Batchelder’s excellent `coverage.py` to show how much of your code is exercised with your tests. Coverage can help offer suggestions on what should be tested helping you to increase the percent of code covered by tests.

<https://pypi.org/project/django-coverage/>

## Install

    pip install coverage

## Utility

    coverage --version
    coverage help

## Running Tests with Coverage

    coverage run manage.py test store

## Specifying tests to run

### Run the specified module

    coverage run manage.py test app1

### Run the specified class

    coverage run manage.py test app1.tests.models

### Run the specified method

    coverage run manage.py test app1.tests.models.TestNew

## Obmit venv or other files from test results

    coverage run --omit='*/venv/*' manage.py test store.tests

## See Results

    coverage report
    coverage html
