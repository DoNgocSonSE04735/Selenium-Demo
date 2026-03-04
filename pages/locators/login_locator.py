from selenium.webdriver.common.by import By
class LoginLocator:
    INPUT_USERNAME = (By.NAME, "username")
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    BTN_LOGIN = (By.XPATH, "//button[contains(string(), 'Log In')]")
    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Forgot the password?']")
    TXT_ERROR_MSG = (By.XPATH, "//div[text()= '{text}']")
    