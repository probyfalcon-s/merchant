import allure
import pytest

from ..config.settings import ADMIN_URL, AUTH_URL
from ..data.test_data import TEST_DATA, TEST_DATA_USER, TEST_DATA_COMMISSION
from ..pages.commission_page import CreateCommissionPage
from ..pages.personal_account_page import PersonalAccountPage



# @pytest.mark.usefixtures("custom_page")
# class TestCreateCommission:
@pytest.mark.skip(reason="Тест временно отключен - отключена функциональность")
@allure.title("Создание комиссии - тип транзакция")
@pytest.mark.tcms('1285')
def test_create_commission(custom_page):
    login_page = PersonalAccountPage(custom_page)
    commission_page = CreateCommissionPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    login_page.click_link_commissions()

    commission_page.click_create_commission()

    commission_page.click_dropdown_menu_type()
    commission_page.click_dropdown_menu_transaction()
    commission_page.click_dropdown_menu_network_tax()
    commission_page.enter_amount_commission(TEST_DATA_COMMISSION['amount_commission'])
    commission_page.click_create_commission_end()


@allure.title("Создание комиссии - тип пользователь")
@pytest.mark.tcms('2430')
def test_create_commission_for_user(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)
    commission_page = CreateCommissionPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()

    switch_to_russian()
    login_page.click_link_commissions()

    commission_page.click_create_commission()

    #commission_page.click_dropdown_menu_type_user() #убрали тип комиссии
    commission_page.click_dropdown_menu_commission_user()
    commission_page.click_dropdown_menu_network_tax()
    commission_page.enter_amount_commission(TEST_DATA_COMMISSION['amount_commission'])
    # commission_page.click_create_commission_end()

@pytest.mark.skip(reason="Тест временно отключен - отключена фунциональность")
@allure.title("Создание комиссии - тип адрес")
@pytest.mark.tcms('2299')
def test_create_commission_for_address(custom_page):
    login_page = PersonalAccountPage(custom_page)
    commission_page = CreateCommissionPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()
    login_page.click_link_commissions()

    commission_page.click_create_commission()

    commission_page.click_dropdown_menu_type_address()
    commission_page.click_dropdown_menu_network_tax()
    commission_page.click_dropdown_menu_address_commission()
    commission_page.enter_amount_commission(TEST_DATA_COMMISSION['amount_commission'])
    commission_page.click_create_commission_end()

