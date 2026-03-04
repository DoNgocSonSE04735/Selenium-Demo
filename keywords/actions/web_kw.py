from keywords.base import BasePage
import logging

class WebKeywords(BasePage):
    def go_to(self, url):
        """ Navigate to url """
        self.driver.get(url)
    
    def wait_for_element_visible(self, locator, timeout=10):
        """ Wait element with timeout """
        return self.wait(self.driver, timeout).until(
            self.wait_ec.visibility_of_element_located(locator)
        )
    
    def is_element_enabled(self, locator):
        return self.driver.find_element(*locator).is_enabled()

    def click(self, locator):
        """ Click element """
        logging.info(f"Click on element: {locator}")
        self.wait_for_element_visible(locator)
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        """ Input element """
        logging.info(f"Click on element: {locator}")
        self.wait_for_element_visible(locator)
        self.driver.find_element(*locator).send_keys(text)

    def verify_element_is_visible(self, locator, message = ""):
        """ Verify Element is visble"""
        try:
            element = self.wait_for_element_visible(locator)
            assert element.is_displayed(), \
                f"{message} | Element is not visible"
        except Exception as e:
            raise AssertionError(
                f"{message} | Element not visible. Error: {str(e)}"
            )
        
    def verify_element_is_false(self, bool):
        """ Verify Element is False"""
        try:
            assert bool is False, \
                f"Element is not false"
        except Exception as e:
            raise AssertionError(
                f"Element not false. Error: {str(e)}"
            )