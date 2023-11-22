import allure
from .BasePage import BasePage
from locators.locators import JsAlertsPageLocators
from selenium.webdriver.support import expected_conditions as EC


class JsAlertsPage(BasePage):
    @allure.step("First button workflow test")
    def first_button_test(self):
        self.click_element(JsAlertsPageLocators.alert)
        alert = self.wait_for(EC.alert_is_present())
        actual_alert_text = alert.text
        expected_alert_text = "I am an alert box!"
        assert (expected_alert_text in actual_alert_text), \
            f"Expected result: {expected_alert_text} \t Actual result: {actual_alert_text}"
        alert.accept()

    @allure.step("Second button workflow test")
    def second_button_test(self):
        self.click_element(JsAlertsPageLocators.confirm)
        confirm = self.wait_for(EC.alert_is_present())
        actual_confirm_text = confirm.text
        expected_confirm_text = "I am a confirm alert"
        assert (expected_confirm_text in actual_confirm_text), \
            f"Expected result: {expected_confirm_text} \t Actual result: {actual_confirm_text}"
        confirm.accept()
        actual_out_txt = self.get_element(JsAlertsPageLocators.confirm_out).text
        expected_out_txt = "true"
        assert (expected_out_txt in actual_out_txt), \
            f"Expected result: {expected_out_txt} \t Actual result: {actual_out_txt}"

    @allure.step("Third button workflow test")
    def third_button_test(self):
        self.click_element(JsAlertsPageLocators.prompt)
        prompt = self.wait_for(EC.alert_is_present())
        actual_prompt_text = prompt.text
        expected_prompt_text = "I prompt you"
        assert (expected_prompt_text in actual_prompt_text), \
            f"Expected result: {expected_prompt_text} \t Actual result: {actual_prompt_text}"
        prompt.send_keys("qwertyuiop[]")
        prompt.accept()
        actual_out_txt = self.get_element(JsAlertsPageLocators.prompt_out).text
        expected_out_txt = "qwertyuiop[]"
        assert (expected_out_txt in actual_out_txt), \
            f"Expected result: {expected_out_txt} \t Actual result: {actual_out_txt}"
