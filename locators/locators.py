from selenium.webdriver.common.by import By


class BasicPageLocators:
    p1 = (By.XPATH, "//p[@id='para1']")
    p2 = (By.XPATH, "//p[@id='para2']")


class ElementAttributesPageLocators:
    p1 = (By.XPATH, "//p[contains(text(),'This paragraph has attributes')]")
    p2_button = (By.XPATH, "//button[contains(text(),'Add Another Attribute')]")
    p2 = (By.XPATH, "(//p[contains(text(),'This paragraph has dynamic attributes')])[1]")
    p3 = (By.XPATH, "(//p[contains(text(),'This paragraph has dynamic attributes')])[2]")
