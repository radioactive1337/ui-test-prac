import allure

from pages.BasicPage import BasicPage

URL = "https://testpages.eviltester.com/styled/basic-web-page-test.html"


class Test:
    @allure.title("Basic page test")
    def test_1(self, driver):
        page = BasicPage(driver=driver, url=URL)
        page.open()
        assert page.get_title() == "Basic Web Page Title", "Error in page title"
        page.check_text_in_p1("A paragraph of text")
        page.check_text_in_p2("Another paragraph of text")
