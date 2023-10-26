import allure

from .BasePage import BasePage
from locators.locators import ElementAttributesPageLocators


class ElementAttributesPage(BasePage):
    @allure.step("Checking value of custom attribute in paragraph 1")
    def check_custom_attr_in_p1(self):
        expected_attr_val = "attrib in source at load"
        actual_attr_val = self.get_element_attribute(ElementAttributesPageLocators.p1,
                                                     "custom-attrib")
        assert (expected_attr_val in actual_attr_val), \
            f"Expected result:{expected_attr_val} \t Actual result:{actual_attr_val}"

    @allure.step("Checking value of dynamic attributes in paragraph 2 before clicking the button")
    def first_check_dynamic_attrs_p2(self):
        expected_attr1_val = "1"
        actual_attr1_val = self.get_element_attribute(ElementAttributesPageLocators.p2, "nextid")
        expected_attr2_val = None
        actual_attr2_val = self.get_element_attribute(ElementAttributesPageLocators.p2, "custom-1")
        assert (expected_attr1_val in actual_attr1_val), \
            f"Expected result:{expected_attr1_val} \t Actual result:{actual_attr1_val}"
        assert (expected_attr2_val == actual_attr2_val), \
            f"Expected result:{expected_attr2_val} \t Actual result:{actual_attr2_val}"

    @allure.step("Checking value of dynamic attributes in paragraph 2 after clicking the button")
    def second_check_dynamic_attrs_p2(self):
        self.click_element(ElementAttributesPageLocators.p2_button)
        expected_1 = "2"
        actual_1 = self.get_element_attribute(ElementAttributesPageLocators.p2, "nextid")
        expected_2 = "value-1"
        actual_2 = self.get_element_attribute(ElementAttributesPageLocators.p2, "custom-1")
        assert (expected_1 in actual_1), f"Expected result:{expected_1} \t Actual result:{actual_1}"
        assert (expected_2 == actual_2), f"Expected result:{expected_2} \t Actual result:{actual_2}"

    @allure.step("Checking attributes variability value in paragraph 3")
    def check_all_attrs_p3(self):
        expected_attr1_val = self.get_element_attribute(ElementAttributesPageLocators.p3, "name")
        expected_attr2_val = self.get_element_attribute(ElementAttributesPageLocators.p3, "data-count")
        expected_attr3_val = self.get_element_attribute(ElementAttributesPageLocators.p3, "data-dynamic")
        expected_attr4_val = self.get_element_attribute(ElementAttributesPageLocators.p3, "id")
        self.wait(3)
        expected_attr1_val_2 = self.get_element_attribute(ElementAttributesPageLocators.p3, "name")
        expected_attr2_val_2 = self.get_element_attribute(ElementAttributesPageLocators.p3, "data-count")
        expected_attr3_val_2 = self.get_element_attribute(ElementAttributesPageLocators.p3, "data-dynamic")
        expected_attr4_val_2 = self.get_element_attribute(ElementAttributesPageLocators.p3, "id")

        assert expected_attr1_val != expected_attr1_val_2, \
            f"Previous value:{expected_attr1_val} \t Actual value:{expected_attr1_val_2}"
        assert expected_attr2_val != expected_attr2_val_2, \
            f"Previous value:{expected_attr2_val} \t Actual value:{expected_attr2_val_2}"
        assert expected_attr3_val != expected_attr3_val_2, \
            f"Previous value:{expected_attr3_val} \t Actual value:{expected_attr3_val_2}"
        assert expected_attr4_val == expected_attr4_val_2, \
            f"Previous value:{expected_attr4_val} \t Actual value:{expected_attr4_val_2}"
