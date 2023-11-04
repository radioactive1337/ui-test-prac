import allure
import selenium.common
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = f"{url}"

    @allure.step("Get page title")
    def get_title(self):
        return self.driver.title

    @allure.step("Get page URL")
    def get_url(self):
        return self.driver.current_url

    @allure.step("Find element")
    def get_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    @allure.step("Find elements")
    def get_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    @allure.step("Get element attribute")
    def get_element_attribute(self, locator, attr):
        return self.get_element(locator).get_attribute(attr)

    @allure.step("Count elements")
    def get_elements_count(self, locator):
        return len(self.driver.get_elements(locator))

    @allure.step("Open the page")
    def open(self):
        self.driver.get(self.url)
        self.wait_for_page_to_load()

    @allure.step("Waiting for the page to load")
    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))

    @allure.step("Close current window/tab")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Explicit wait")
    def wait(self, time: float):
        sleep(time)

    @allure.step("Implicit wait")
    def wait_for(self, action):
        wait = WebDriverWait(self.driver, 10)
        action_waiting_for = wait.until(action)

    @allure.step("Click on the element")
    def click_element(self, locator):
        self.get_element(locator).click()

    @allure.step("Clear")
    def clear_cookies(self):
        self.driver.delete_all_cookies()

    @allure.step("Input text")
    def fill_input(self, locator, value):
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(value)

    @allure.step("Select value in dropdown list")
    def select_value(self, locator, value):
        Select(self.get_element(locator)).select_by_value(value)

    @allure.step("Refresh page")
    def refresh_page(self):
        self.driver.refresh()
        try:
            self.driver.switch_to.alert.accept()
        except Exception:
            pass
        self.driver.switch_to.default_content()

    @allure.step("Checking that the item is on the page")
    def verify_element_present(self, locator, time=5):
        try:
            self.get_element(locator, time)
            return True
        except selenium.common.TimeoutException:
            return False

    @allure.step("Scroll to top of page")
    def scroll_page_to_top(self):
        self.driver.execute_script("window.scrollTo(0,0);")

    @allure.step("Scroll to bottom of page")
    def scroll_page_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    @allure.step("Switch to main window/tab")
    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step("Switch to last window/tab")
    def switch_to_new_window(self):
        if len(self.driver.window_handles) == 1:
            raise Exception('New window not found')
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Screenshot")
    def take_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)
