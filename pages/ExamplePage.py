import allure
from .BasePage import BasePage
from locators.locators import ExamplePageLocators


class ExamplePage(BasePage):
    @allure.step("Checking text in paragraphs 1, 2")
    def check_paragraphs_text(self):
        assert ("A paragraph of text" in self.get_element(ExamplePageLocators.p1).text)
        assert ("Another paragraph of text" in self.get_element(ExamplePageLocators.p2).text)

    @allure.step("Checking text list items")
    def check_list_items(self):
        for n, item in enumerate(self.get_elements(ExamplePageLocators.all_li), 1):
            txt = f"List Item {n}"
            assert (txt in item.text), \
                f"Expected result: {txt} \t Actual result: {item.text}"

    @allure.step("Checking 'Show as para' button")
    def check_para_button(self, input_val, output_val):
        self.fill_input(ExamplePageLocators.txt_input, input_val)
        self.click_element(ExamplePageLocators.para_button)
        self.wait(1)
        result_message = self.get_element(ExamplePageLocators.message).text
        assert (output_val in result_message), \
            f"Expected result: {output_val} \t Actual result: {result_message}"

    @allure.step("Checking 'Show as alert' button")
    def check_alert_button(self, input_val, output_val):
        self.fill_input(ExamplePageLocators.txt_input, input_val)
        self.click_element(ExamplePageLocators.alert_button)
        a = self.driver.switch_to.alert
        assert (output_val in a.text), \
            f"Expected result: {output_val} \t Actual result: {a.text}"
        a.accept()

    @allure.step("Checking 'Show From Link' button")
    def check_link_button(self):
        self.click_element(ExamplePageLocators.link_button)
        expected_message = "one, two, three, four, five, six, seven, eight, nine"
        actual_message = self.get_element(ExamplePageLocators.message).text
        assert (expected_message in actual_message), \
            f"Expected result: {expected_message} \t Actual result: {actual_message}"

    @allure.step("Checking 'Process On Server' button")
    def check_submit_button(self, input_val, output_val):
        self.fill_input(ExamplePageLocators.txt_input, input_val)
        self.click_element(ExamplePageLocators.submit)
        expected_url = f"https://testpages.eviltester.com/styled/webdriver-example-page?number-entry={input_val}"
        actual_url = self.get_url()
        actual_message = self.get_element(ExamplePageLocators.message).text
        expected_message = output_val
        assert (expected_url in actual_url), \
            f"Expected result: {expected_url} \t Actual result: {actual_url}"
        assert (expected_message in actual_message), \
            f"Expected result: {expected_message} \t Actual result: {actual_message}"
