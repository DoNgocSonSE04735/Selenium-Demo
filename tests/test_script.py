import pytest, time
from utils.random_utils import RandomUtils
from test_data.data import data

@pytest.mark.smoke
def test_testcase1(login_action, common_action):
    common_action.navigate_to_url(data["url"])
    common_action.skip_warning()
    login_action.verify_login_page_loads_successfully()
    login_action.verify_forgot_password_is_visible()
    login_action.verify_login_button_is_disabled()

@pytest.mark.smoke
def test_testcase2(login_action, common_action, homepage_action):
    test_data = data["testcase_2"]
    common_action.navigate_to_url(data["url"])
    common_action.skip_warning()
    login_action.verify_forgot_password_is_visible()
    login_action.verify_login_button_is_disabled()
    login_action.input_username(test_data["username"])
    login_action.input_password(test_data["password"])
    login_action.click_on_login_button()
    homepage_action.verify_login_successful()

@pytest.mark.smoke
@pytest.mark.parametrize("test_data", data["testcase_3"])
def test_testcase3(login_action, common_action, test_data):
    common_action.navigate_to_url(data["url"])
    common_action.skip_warning()
    login_action.verify_forgot_password_is_visible()
    login_action.verify_login_button_is_disabled()
    login_action.input_username(test_data["username"])
    login_action.input_password(test_data["password"])
    login_action.click_on_login_button()
    login_action.verify_error_message_is_visible(test_data["error_message"])
    

custom_test_data = data["testcase_4"] + [
    {
        "username": RandomUtils._random_digits(256),
        "password": "12345",
        "error_message": "Incorrect credentials."
    },
    {
        "username": "sony1412",
        "password": RandomUtils._random_digits(101),
        "error_message": "Incorrect credentials."
    }
]
@pytest.mark.smoke
@pytest.mark.parametrize("test_data", custom_test_data)
def test_testcase4(login_action, common_action, test_data):
    common_action.navigate_to_url(data["url"])
    common_action.skip_warning()
    login_action.verify_forgot_password_is_visible()
    login_action.verify_login_button_is_disabled()
    login_action.input_username(test_data["username"])
    login_action.input_password(test_data["password"])
    login_action.click_on_login_button()
    login_action.verify_error_message_is_visible(test_data["error_message"])
