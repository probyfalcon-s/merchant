import pytest
import allure
from ..config.settings import ADMIN_URL, AUTH_URL, TRANSACTIONS_URL
from ..data.test_data import TEST_DATA, TEST_DATA_USER, TEST_DATA_COMMISSION, TEST_DATA_TRANSACTION
from ..pages.personal_account_page import PersonalAccountPage
from ..pages.transaction_page import CreateTransactionPage


@allure.title("Создание транзакции - with withdrawal - bnb token")
@pytest.mark.tcms('1443')
def test_create_transaction(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    transaction_page = CreateTransactionPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    login_page.click_link_transaction()

    transaction_page.click_create_transaction()

    transaction_page.click_dropdown_menu_user_transaction()
    transaction_page.click_dropdown_menu_network()
    transaction_page.click_dropdown_menu_type_transaction()
    transaction_page.click_dropdown_menu_token()
    transaction_page.click_dropdown_menu_address()

    transaction_page.enter_client_transaction_input(TEST_DATA_TRANSACTION['client'])
    transaction_page.enter_amount_transaction_input(TEST_DATA_TRANSACTION['amount'])
    transaction_page.enter_address_client_transaction_input(TEST_DATA_TRANSACTION['address_client'])
    transaction_page.click_create_transaction_end()

@allure.title("Создание транзакции - with deposit - bnb token")
@pytest.mark.tcms('2046')
def test_create_transaction_deposit(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    transaction_page = CreateTransactionPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    login_page.click_link_transaction()

    transaction_page.click_create_transaction()

    transaction_page.click_dropdown_menu_user_transaction()
    transaction_page.click_dropdown_menu_network()
    transaction_page.click_dropdown_menu_type_transaction_deposit()
    transaction_page.click_dropdown_menu_token()
    transaction_page.click_dropdown_menu_address()

    transaction_page.enter_client_transaction_input(TEST_DATA_TRANSACTION['client'])
    transaction_page.enter_amount_transaction_input(TEST_DATA_TRANSACTION['amount'])
    transaction_page.click_create_transaction_end()
    custom_page.wait_for_timeout(3000)


@allure.title("Создание транзакции - with deposit usdt ")
@pytest.mark.tcms('2660')
def test_create_transaction_deposit_usdt(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    transaction_page = CreateTransactionPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    login_page.click_link_transaction()

    transaction_page.click_create_transaction()

    transaction_page.click_dropdown_menu_user_transaction()
    transaction_page.click_dropdown_menu_network()
    transaction_page.click_dropdown_menu_type_transaction_deposit()
    transaction_page.click_dropdown_menu_token_usdt()
    transaction_page.click_dropdown_menu_address()

    transaction_page.enter_client_transaction_input(TEST_DATA_TRANSACTION['client'])
    transaction_page.enter_amount_transaction_input(TEST_DATA_TRANSACTION['amount_usdt'])
    transaction_page.click_create_transaction_end()

@allure.title("Создание транзакции - with withdrawal usdt")
@pytest.mark.tcms('2705')
def test_create_transaction_withdrawal_usdt(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    transaction_page = CreateTransactionPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    switch_to_russian()
    login_page.click_link_transaction()

    transaction_page.click_create_transaction()

    transaction_page.click_dropdown_menu_user_transaction()
    transaction_page.click_dropdown_menu_network()
    transaction_page.click_dropdown_menu_type_transaction()
    transaction_page.click_dropdown_menu_token_usdt()
    transaction_page.click_dropdown_menu_address()

    transaction_page.enter_client_transaction_input(TEST_DATA_TRANSACTION['client'])
    transaction_page.enter_amount_transaction_input(TEST_DATA_TRANSACTION['amount'])
    transaction_page.enter_address_client_transaction_input(TEST_DATA_TRANSACTION['address_client'])
    transaction_page.click_create_transaction_end()

