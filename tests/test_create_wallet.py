import pytest
import allure
from ..config.settings import AUTH_URL
from ..data.test_data import TEST_DATA
from ..pages.personal_account_page import PersonalAccountPage
from ..pages.wallet_page import CreateWalletPage



@allure.title("Создание кошелька")
def test_create_wallet(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    wallet_page = CreateWalletPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    login_page.click_link_wallet()

    wallet_page.click_create_wallet()

    wallet_page.click_dropdown_menu_user_wallet()
    wallet_page.click_dropdown_menu_type()
    wallet_page.click_dropdown_menu_network()

    wallet_page.click_create_wallet_end()


@allure.title("Создание кошелька AP")
def test_create_wallet_type_ap(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    wallet_page = CreateWalletPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    login_page.click_link_wallet()

    wallet_page.click_create_wallet()
    wallet_page.click_dropdown_menu_user_wallet()
    wallet_page.click_dropdown_menu_type_ap()
    wallet_page.click_dropdown_menu_network()

    wallet_page.click_create_wallet_end()

@allure.title("Создание кошелька AP по умолчанию, активен")
def test_create_wallet_type_ap_active_default(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    wallet_page = CreateWalletPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    login_page.click_link_wallet()

    wallet_page.click_create_wallet()

    wallet_page.click_dropdown_menu_user_wallet()
    wallet_page.click_dropdown_menu_type_ap()
    wallet_page.click_dropdown_menu_network()

    wallet_page.click_switch_default_wallet()
    wallet_page.click_switch_active_wallet()
    wallet_page.click_create_wallet_end()

@allure.title("Создание кошелька AP по умолчанию")
def test_create_wallet_type_ap_only_default(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    wallet_page = CreateWalletPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    login_page.click_link_wallet()

    wallet_page.click_create_wallet()

    wallet_page.click_dropdown_menu_user_wallet()
    wallet_page.click_dropdown_menu_type_ap()
    wallet_page.click_dropdown_menu_network()

    wallet_page.click_switch_default_wallet()
    wallet_page.click_create_wallet_end()

@allure.title("Создание кошелька AP по активен")
def test_create_wallet_type_ap_only_active(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    wallet_page = CreateWalletPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    login_page.click_link_wallet()

    wallet_page.click_create_wallet()

    wallet_page.click_dropdown_menu_user_wallet()
    wallet_page.click_dropdown_menu_type_ap()
    wallet_page.click_dropdown_menu_network()
    wallet_page.click_switch_active_wallet()
    wallet_page.click_create_wallet_end()