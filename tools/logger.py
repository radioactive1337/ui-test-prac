import logging
from selenium.webdriver.support.events import AbstractEventListener


class WebDriverListener(AbstractEventListener):

    def __init__(self):
        self.logger = logging.getLogger("selenium")
        self.logger.setLevel(logging.INFO)

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Opening {url}")

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for element by {by} {value}")

    def before_click(self, element, driver):
        if element.get_attribute('text') is None:
            if element.get_attribute('id') is None:
                self.logger.info(f"Clicking on {element.get_attribute('class')}")
            else:
                self.logger.info(f"Clicking on {element.get_attribute('id')}")

        else:
            self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def before_change_value_of(self, element, driver):
        if element.get_attribute('text') is None:
            if element.get_attribute('id') is None:
                self.logger.info(f"Changing element with class: {element.get_attribute('class')}")
            else:
                self.logger.info(f"Changing element with id: {element.get_attribute('id')}")
        else:
            self.logger.info(f"Changing element with text: {element.get_attribute('text')}")

    def before_quit(self, driver):
        self.logger.info("Driver quitting")

    def before_close(self, driver) -> None:
        self.logger.info("Closing tab/window")

    def on_exception(self, exception, driver):
        self.logger.info(exception)

    def before_execute_script(self, script, driver):
        self.logger.info(f"Executing script: {script}")
