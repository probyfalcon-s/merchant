import pytest
import allure
from ..config.settings import ADMIN_URL, AUTH_URL, TRANSACTIONS_URL, TAX_URL, ADDRESSES_URL
from ..data.test_data import TEST_DATA
from ..pages.personal_account_page import PersonalAccountPage
from ..config.settings import USERS_URL

# autotests/tests/test_change_language.py::test_change_language

@allure.title("Вход по логину и паролю")
@pytest.mark.tcms('1060')
def test_change_language(custom_page, switch_to_russian):
    login_page = PersonalAccountPage(custom_page)

    custom_page.goto(AUTH_URL)

    login_page.enter_email(TEST_DATA['login'])
    login_page.enter_password(TEST_DATA['password'])
    login_page.click_submit()

    switch_to_russian()
    # custom_page.wait_for_url(ADMIN_URL, timeout=5000)
    # assert ADMIN_URL in custom_page.url