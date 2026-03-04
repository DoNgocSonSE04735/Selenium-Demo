from pages.locators.homepage_locator import HomePageLocator
from keywords.actions.web_kw import WebKeywords

class HomePageAction(WebKeywords, HomePageLocator):

    def verify_login_successful(self):
        self.verify_element_is_visible(self.BTN_LOGOUT)