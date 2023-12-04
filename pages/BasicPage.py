import allure
from .BasePage import BasePage
from locators.locators import BasicPageLocators
from enums.global_enums import ErrorEnums


class BasicPage(BasePage):
    @allure.step("Checking the text in paragraph 1")
    def check_text_in_p1(self, expected_text):
        actual_text = self.get_element(BasicPageLocators.p1).text

        assert (expected_text in actual_text), \
            f"{ErrorEnums.TEXT_NOT_EQUAL.value} ({expected_text} : {actual_text})"

    @allure.step("Checking the text in paragraph 2")
    def check_text_in_p2(self, expected_text):
        actual_text = self.get_element(BasicPageLocators.p2).text

        assert (expected_text in actual_text), \
            f"{ErrorEnums.TEXT_NOT_EQUAL.value} ({expected_text} : {actual_text})"
