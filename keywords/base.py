from selenium.webdriver.common.webdriver import LocalWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver: LocalWebDriver = driver
        self.wait = WebDriverWait
        self.wait_ec = EC

    def build_dynamic_locator(self, locator, **kwargs):
        by, value = locator
        return (by, value.format(**kwargs))

    