import pytest
import allure

from pages.BasicPage import BasicPage

URL = "https://testpages.eviltester.com/styled/basic-web-page-test.html"


class Test:
    @allure.title("Basic page test")
    def test_homepage_title(self, driver):
        page = BasicPage(driver=driver, url=URL)
        page.open()
        page.wait_for_page_to_load()
        assert page.get_title() == "Basic Web Page Title"
        page.verify_text_in_p1("A paragraph of text")
        page.verify_text_in_p2("Another paragraph of text")
