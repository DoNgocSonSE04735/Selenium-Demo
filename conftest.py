import pytest
from drivers.web import get_driver
from pages.actions.login_action import LoginAction
from pages.actions.common_action import CommonAction
from pages.actions.homepage_action import HomePageAction

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def login_action(driver):
    return LoginAction(driver)

@pytest.fixture
def common_action(driver):
    return CommonAction(driver)

@pytest.fixture
def homepage_action(driver):
    return HomePageAction(driver)