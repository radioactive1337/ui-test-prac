from .BasePage import BasePage
from locators.locators import BasicPageLocators


class BasicPage(BasePage):
    def verify_text_in_p1(self, expected_text):
        actual_text = self.get_element(BasicPageLocators.p1).text
        assert (expected_text in actual_text), f"Expected result:{expected_text} \t Actual result:{actual_text}"

    def verify_text_in_p2(self, expected_text):
        actual_text = self.get_element(BasicPageLocators.p2).text
        assert (expected_text in actual_text), f"Expected result:{expected_text} \t Actual result:{actual_text}"
