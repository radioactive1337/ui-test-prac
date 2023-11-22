from selenium.webdriver.common.by import By


class BasicPageLocators:
    p1 = (By.XPATH, "//p[@id='para1']")
    p2 = (By.XPATH, "//p[@id='para2']")


class ElementAttributesPageLocators:
    p1 = (By.XPATH, "//p[contains(text(),'This paragraph has attributes')]")
    p2_button = (By.XPATH, "//button[contains(text(),'Add Another Attribute')]")
    p2 = (By.XPATH, "(//p[contains(text(),'This paragraph has dynamic attributes')])[1]")
    p3 = (By.XPATH, "(//p[contains(text(),'This paragraph has dynamic attributes')])[2]")


class ExamplePageLocators:
    p1 = (By.XPATH, "//p[@id='para1']")
    p2 = (By.XPATH, "//p[@id='para2']")
    all_li = (By.XPATH, "//li")
    message = (By.XPATH, "//p[@id='message']")
    txt_input = (By.XPATH, "//input[@id='numentry']")
    submit = (By.XPATH, "//input[@id='submit-to-server']")
    alert_button = (By.XPATH, "//button[@id='show-as-alert']")
    para_button = (By.XPATH, "//button[@data-locator='process-in-para']")
    link_button = (By.XPATH, "//a[@id='clickable-link']")


class DynamicTablePageLocators:
    table_caption = (By.XPATH, "//caption")
    table = (By.XPATH, "//table")
    table_rows = (By.XPATH, "//tr")
    options = (By.XPATH, "//summary")
    table_input = (By.XPATH, "//textarea[@id='jsondata']")
    caption_input = (By.XPATH, "//input[@id='caption']")
    table_id_input = (By.XPATH, "//input[@id='tableid']")
    table_refresh = (By.XPATH, "//button[@id='refreshtable']")


class JsAlertsPageLocators:
    alert = (By.XPATH, "//input[@id='alertexamples']")
    confirm = (By.XPATH, "//input[@id='confirmexample']")
    confirm_out = (By.XPATH, "//p[@id='confirmreturn']")
    prompt = (By.XPATH, "//input[@id='promptexample']")
    prompt_out = (By.XPATH, "//p[@id='promptreturn']")
