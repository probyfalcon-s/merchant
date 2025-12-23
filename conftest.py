import pytest
from .pages.personal_account_page import PersonalAccountPage
import allure
from playwright.sync_api import APIRequestContext, sync_playwright
from playwright.async_api import async_playwright, APIRequestContext
import os
from dotenv import load_dotenv


load_dotenv()


# Существующие фикстуры
@pytest.fixture
def switch_to_russian(custom_page):
    def _switch():
        login_page = PersonalAccountPage(custom_page)
        login_page.click_button_down()
        login_page.click_link_language()
        login_page.click_link_language_russian()
    return _switch


BASE_URL = 'https://'
#back fixture офф для front тестов
@pytest.fixture(scope="session")
async def api_request_context():
    """
    Фикстура для создания контекста API запросов.
    Используется для всех тестов, требующих отправки HTTP запросов.
    """
    async with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url=BASE_URL,
            extra_http_headers={
                "accept": "application/json",
                "Content-Type": "application/json"
            }
        )
        yield request_context
        request_context.dispose()

@pytest.fixture(scope="session")
def access_token(api_request_context: APIRequestContext):
    """
    Фикстура для получения токена доступа.
    Использует api_request_context для отправки запроса аутентификации.
    """
    with allure.step("Получение токена доступа"):
        payload = {
            "email": os.getenv("DEV_USER_MAINNET_EMAIL"), #dev EMAIL
            "password": os.getenv("DEV_USER_MAINNET_PASSWORD") #dev password
        }
        response = api_request_context.post("/get-token", data=payload)
        assert response.status == 200, f"Ожидаем 200, получили {response.status}"
        response_json = response.json()
        print(f"Ответ от сервера при получении токена: {response_json}")
        token = response_json.get("token") or response_json.get("access_token")
        assert token, "Токен не найден"
        assert isinstance(token, str) and len(token) > 10, "Неверный формат токена"
        return token

@pytest.fixture(scope="function") #front fixture
async def custom_page(playwright):
    browser = await playwright.chromium.launch(args=["--no-sandbox"], headless=True, slow_mo=500) #True - ф/р, False - б/р
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()
    await browser.close()

