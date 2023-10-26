import pytest
from selenium import webdriver
from tools.logger import WebDriverListener
from selenium.webdriver.support.events import EventFiringWebDriver


def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
        choices=("chrome", "firefox")
    )
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="Choose the mode: true or false",
        choices=("true", "false")
    )


@pytest.fixture(scope="session")
def driver(request):
    driver_name = request.config.getoption("driver")
    headless = request.config.getoption("headless")
    if driver_name == "chrome":
        opt = webdriver.ChromeOptions()
        if headless == "true":
            opt.add_argument("--headless")
        driver = EventFiringWebDriver(webdriver.Chrome(options=opt), WebDriverListener())
    elif driver_name == "firefox":
        opt = webdriver.FirefoxOptions()
        if headless == "true":
            opt.add_argument("--headless")
        driver = EventFiringWebDriver(webdriver.Firefox(options=opt), WebDriverListener())
    else:
        raise Exception(f"{driver_name} is not supported!")
    yield driver
    driver.quit()
