import allure
import pytest
from playwright.async_api import expect

from ..config.settings import ADMIN_URL, AUTH_URL, USERS_URL
from ..data.test_data import TEST_DATA, TEST_DATA_USER
from ..pages.personal_account_page import PersonalAccountPage
from ..pages.users_page import CreateUserPage



@allure.epic("User Management")
@allure.feature("User Creation")
@allure.story("Create New User")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    user_page = CreateUserPage(custom_page)

    # Login to application
    custom_page.goto(AUTH_URL)
    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    # Navigate to users page
    login_page.click_link_users()

    # Create new user
    user_page.click_create_user()
    user_page.enter_name_input(TEST_DATA_USER['name'])
    user_page.enter_description_input(TEST_DATA_USER['description'])
    user_page.enter_create_email_user_input(TEST_DATA_USER['email'])
    user_page.enter_ip4_input(TEST_DATA_USER['ip4'])
    user_page.click_next_button_user()
    user_page.click_create_button_user_end()

    # Verify success message
    with allure.step("Verify success message"):
        success_message = custom_page.locator('div.ant-notification-notice-message')



