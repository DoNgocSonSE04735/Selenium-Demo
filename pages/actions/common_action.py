from keywords.actions.web_kw import WebKeywords
from pages.locators.common_locator import CommonLocator
class CommonAction(WebKeywords, CommonLocator):
    def navigate_to_url(self, url):
        self.go_to(url)

    def skip_warning(self):
        self.click(self.BTN_DETAILS)
        self.click(self.BTN_PROCEED_LINK)