import allure
import pytest
from pages.JsAlertPage import JsAlertsPage

URL = "https://testpages.eviltester.com/styled/alerts/alert-test.html"


class Test:
    @allure.title("JS Alert page test")
    def test_1(self, driver):
        page = JsAlertsPage(driver=driver, url=URL)
        page.open()
        page.assert_page_title("Test Page For JavaScript Alerts")
        page.first_button_test()
        page.second_button_test()
        page.third_button_test()
