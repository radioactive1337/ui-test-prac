# ui-test-prac

## Description

UI framework for the practice of modules such as selenium, allure and other tools \
[Example of the allure report is shown here](https://radioactive1337.github.io/ui-test-prac/)

## Project structure

| Name     | Desc                |
|:---------|:--------------------|
| locators | storage of locators |
| pages    | page_objects for UI |
| tests    | UI tests            |
| tools    | smth helpful        |

## Installation

Clone project

~~~bash
git clone https://github.com/radioactive1337/ui-test-prac.git
~~~

~~~bash
cd ui-test-practice
~~~

Install requirements

~~~bash
pip install -r requirements.txt
~~~

## Usage

Run all tests with allure (with pre-installed Allure)

~~~bash
pytest --alluredir=allurereport
~~~

Create report page

~~~bash
allure serve allurereport
~~~
