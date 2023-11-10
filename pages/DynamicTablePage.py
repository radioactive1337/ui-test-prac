import json

import allure
from .BasePage import BasePage
from locators.locators import DynamicTablePageLocators


class DynamicTablePage(BasePage):
    @allure.step("Checking table content")
    def check_table_content(self, input_table_data, input_table_caption, input_table_id):
        self.click_element(DynamicTablePageLocators.options)
        self.fill_input(DynamicTablePageLocators.table_input, input_table_data)
        self.fill_input(DynamicTablePageLocators.caption_input, input_table_caption)
        self.fill_input(DynamicTablePageLocators.table_id_input, input_table_id)
        self.click_element(DynamicTablePageLocators.table_refresh)
        expected_caption = input_table_caption
        actual_caption = self.get_element(DynamicTablePageLocators.table_caption).text
        expected_id = input_table_id
        actual_id = self.get_element_attribute(DynamicTablePageLocators.table, "id")
        actual_table_data = self.get_elements(DynamicTablePageLocators.table_rows)
        expected_table_data = json.loads(input_table_data)
        keys = list(expected_table_data[0].keys())
        for i in range(1, len(actual_table_data)):
            act = actual_table_data[i].text
            exp = expected_table_data[i - 1]
            for key in keys:
                assert (str(exp[f"{key}"]) in act), f"exp = {exp} act = {act}"
        assert (expected_caption in actual_caption), \
            f"Expected result:{expected_caption} \t Actual result:{actual_caption}"
        assert (expected_id in actual_id), \
            f"Expected result:{expected_id} \t Actual result:{actual_id}"
