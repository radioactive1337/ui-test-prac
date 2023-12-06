import allure
from pages.ElementAttributesPage import ElementAttributesPage

URL = "https://testpages.eviltester.com/styled/attributes-test.html"


class Test:
    @allure.title("Element Attributes page test")
    def test_1(self, driver):
        page = ElementAttributesPage(driver=driver, url=URL)
        page.open()
        page.assert_page_title("Test Page For Element Attributes")
        page.check_custom_attr_in_p1()
        page.first_check_dynamic_attrs_p2()
        page.second_check_dynamic_attrs_p2()
        page.check_all_attrs_p3()
