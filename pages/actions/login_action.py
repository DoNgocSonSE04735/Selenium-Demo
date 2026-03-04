import logging
from pages.locators.login_locator import LoginLocator
from keywords.actions.web_kw import WebKeywords

class LoginAction(WebKeywords, LoginLocator):
     
    def input_username(self, username):
        self.input_text(self.INPUT_USERNAME, username)

    def input_password(self, password):
        self.input_text(self.INPUT_PASSWORD, password)

    def click_on_login_button(self):
        self.click(self.BTN_LOGIN)

    def verify_login_page_loads_successfully(self):
        self.verify_element_is_visible(self.INPUT_USERNAME)

    def verify_error_message_is_visible(self, msg):
        self.verify_element_is_visible(self.build_dynamic_locator(self.TXT_ERROR_MSG, text = msg))

    def verify_forgot_password_is_visible(self):
        self.verify_element_is_visible(self.LINK_FORGOT_PASSWORD)

    def verify_login_button_is_disabled(self):
        check = self.is_element_enabled(self.BTN_LOGIN)
        logging.info(f"check:  {check}" )
        self.verify_element_is_false(check)