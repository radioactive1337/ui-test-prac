import allure

from enums.global_enums import ErrorEnums
from .BasePage import BasePage
from locators.locators import ExamplePageLocators


class ExamplePage(BasePage):
    @allure.step("Checking text in paragraphs 1, 2")
    def check_paragraphs_text(self):
        act_p1 = self.get_element(ExamplePageLocators.p1).text
        act_p2 = self.get_element(ExamplePageLocators.p2).text
        exp_val1 = "A paragraph of text"
        exp_val2 = "text"

        assert (exp_val1 in act_p1), \
            f"{ErrorEnums.TEXT_NOT_EQUAL.value} ({exp_val1} : {act_p1})"

        assert (exp_val2 in act_p2), \
            f"{ErrorEnums.TEXT_NOT_EQUAL.value} ({exp_val2} : {act_p2})"

    @allure.step("Checking text list items")
    def check_list_items(self):
        for n, item in enumerate(self.get_elements(ExamplePageLocators.all_li), 1):
            exp_txt = f"List Item {n}"
            act_txt = item.text

            assert (exp_txt in act_txt), \
                f"{ErrorEnums.TEXT_NOT_EQUAL.value} ({exp_txt} : {act_txt})"

    @allure.step("Checking 'Show as para' button")
    def check_para_button(self, input_val, exp_res):
        self.fill_input(ExamplePageLocators.txt_input, input_val)
        self.click_element(ExamplePageLocators.para_button)
        self.wait(0.5)
        act_res = self.get_element(ExamplePageLocators.message).text

        assert (exp_res in act_res), \
            f"{ErrorEnums.TEXT_NOT_EQUAL.value} ({exp_res} : {act_res})"

    @allure.step("Checking 'Show as alert' button")
    def check_alert_button(self, input_val, exp_text):
        self.fill_input(ExamplePageLocators.txt_input, input_val)
        self.click_element(ExamplePageLocators.alert_button)
        a = self.driver.switch_to.alert
        act_text = a.text

        assert (exp_text in act_text), \
            f"{ErrorEnums.TEXT_NOT_EQUAL.value} ({exp_text} : {act_text})"

        a.accept()

    @allure.step("Checking 'Show From Link' button")
    def check_link_button(self):
        self.click_element(ExamplePageLocators.link_button)
        expected_message = "one, two, three, four, five, six, seven, eight, nine"
        actual_message = self.get_element(ExamplePageLocators.message).text

        assert (expected_message in actual_message), \
            f"{ErrorEnums.TEXT_NOT_EQUAL.value} ({expected_message} : {actual_message})"

    @allure.step("Checking 'Process On Server' button")
    def check_submit_button(self, input_val, output_val):
        self.fill_input(ExamplePageLocators.txt_input, input_val)
        self.click_element(ExamplePageLocators.submit)
        expected_url = f"https://testpages.eviltester.com/styled/webdriver-example-page?number-entry={input_val}"
        actual_url = self.get_url()
        actual_message = self.get_element(ExamplePageLocators.message).text
        expected_message = output_val

        assert (expected_url in actual_url), \
            f"{ErrorEnums.URL_NOT_EQUAL.value} ({expected_url} : {actual_url})"

        assert (expected_message in actual_message), \
            f"{ErrorEnums.TEXT_NOT_EQUAL.value} ({expected_message} : {actual_message})"
