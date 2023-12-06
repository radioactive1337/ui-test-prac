import allure
import pytest
from pages.ExamplePage import ExamplePage

URL = "https://testpages.eviltester.com/styled/webdriver-example-page"


class Test:
    @allure.title("Example page test")
    def test_1(self, driver):
        page = ExamplePage(driver=driver, url=URL)
        page.open()
        page.assert_page_title("Example Page Title")
        page.check_paragraphs_text()
        page.check_list_items()
        page.check_link_button()

    @pytest.mark.parametrize("input, output", [(123, "one, two, three"), (666, "six, six, six")])
    @allure.title("Example page buttons test - input: {input} output: {output}")
    def test_2(self, driver, input, output):
        page = ExamplePage(driver=driver, url=URL)
        page.open()
        page.check_para_button(input_val=input, exp_res=output)

    @pytest.mark.parametrize("input, output", [(321, "three, two, one"), (111, "one, one, one")])
    @allure.title("Example page buttons test - input: {input} output: {output}")
    def test_3(self, driver, input, output):
        page = ExamplePage(driver=driver, url=URL)
        page.open()
        page.check_alert_button(input_val=input, exp_text=output)

    @pytest.mark.parametrize("input, output", [(1337, "one, three, three, seven"), (777, "seven, seven, seven")])
    @allure.title("Example page buttons test - input: {input} output: {output}")
    def test_4(self, driver, input, output):
        page = ExamplePage(driver=driver, url=URL)
        page.open()
        page.check_submit_button(input_val=input, output_val=output)
