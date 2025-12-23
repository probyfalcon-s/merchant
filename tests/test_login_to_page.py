import pytest
import allure
from ..config.settings import ADMIN_URL, AUTH_URL, TRANSACTIONS_URL, TAX_URL, ADDRESSES_URL
from ..data.test_data import TEST_DATA
from ..pages.personal_account_page import PersonalAccountPage
from ..config.settings import USERS_URL


@allure.title("Вход по логину и паролю")
async def test_login(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()

    custom_page.wait_for_url(ADMIN_URL, timeout=5000)
    assert ADMIN_URL in custom_page.url

@allure.title("Переход по страницам")
async def test_login_to_transfer_page(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)

    await custom_page.goto(AUTH_URL)

    await login_page.enter_email(TEST_DATA['login'])
    await login_page.enter_password(TEST_DATA['password'])
    await login_page.click_submit()
    await switch_to_russian()

    await login_page.click_link_users()
    await custom_page.wait_for_url(USERS_URL, timeout=5000)
    assert USERS_URL in custom_page.url

    await login_page.click_link_wallet()
    await custom_page.wait_for_url(ADDRESSES_URL, timeout=5000)
    assert ADDRESSES_URL in custom_page.url


    await login_page.click_link_transaction()
    await custom_page.wait_for_url(TRANSACTIONS_URL, timeout=5000)
    assert TRANSACTIONS_URL in custom_page.url

    await login_page.click_link_commissions()
    await custom_page.wait_for_url(TAX_URL, timeout=5000)
    assert TAX_URL in custom_page.url

    await login_page.click_link_information()
    await custom_page.wait_for_url(ADMIN_URL, timeout=5000)
    assert ADMIN_URL in custom_page.url