import json
import allure
from playwright.sync_api import APIRequestContext

from autotests.conftest import access_token, api_request_context


def create_wallet_internal_x(api_request_context: APIRequestContext, access_token: str, active_status=True):
    """Вспомогательная функция для создания кошелька Х"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "user_id": 67,
        "network": "bsc",
        "type": "x",
        "direction": "internal",
        "active": active_status,
        "default": True
    }

    with allure.step("Отправка запроса на создание кошелька Х"):
        print(f"\nОтправляем payload: {json.dumps(payload, indent=2)}")

        response = api_request_context.post(
            "/api/v1/addresses",
            headers=headers,
            data=json.dumps(payload)
        )

        print(f"Статус ответа: {response.status}")
        print(f"Тело ответа: {response.text()}")

        return response


def create_wallet_internal_ap(api_request_context: APIRequestContext, access_token: str, active_status=True):
    """Вспомогательная функция для создания кошелька AP"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "user_id": 67,
        "network": "bsc",
        "type": "ap",
        "direction": "internal",
        "active": active_status,
        "default": True
    }

    with allure.step("Отправка запроса на создание кошелька AP"):
        print(f"\nОтправляем payload: {json.dumps(payload, indent=2)}")

        response = api_request_context.post(
            "/api/v1/addresses",
            headers=headers,
            data=json.dumps(payload)
        )

        print(f"Статус ответа: {response.status}")
        print(f"Тело ответа: {response.text()}")

        return response


def create_wallet_external_x_personal(api_request_context: APIRequestContext, access_token: str, active_status=True):
    """Вспомогательная функция для создания внешнего кошелька X"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "user_id": 67,
        "network": "bsc",
        "address": "0xae38A0b2743760d9246972d4BE37f93e5a35a3F4",
        "type": "x",
        "direction": "external",
        "active": active_status,
        "default": True
    }

    with allure.step("Отправка запроса на создание кошелька X личного кошелька"):
        print(f"\nОтправляем payload: {json.dumps(payload, indent=2)}")

        response = api_request_context.post(
            "/api/v1/addresses",
            headers=headers,
            data=json.dumps(payload)
        )

        print(f"Статус ответа: {response.status}")
        print(f"Тело ответа: {response.text()}")

        return response


class TestCreateWallets:
    """Класс для тестирования создания кошельков"""
    @allure.title("Создание кошелька Х")
    @allure.description("Проверка успешного создания кошелька Х")
    def test_create_wallet_internal_x_success(self, api_request_context: APIRequestContext, access_token: str):
        """Тест проверяет успешное создание транзакции кошелька Х"""

        with allure.step("Создание и проверка кошелька Х"):
            response = create_wallet_internal_x(api_request_context, access_token)

            assert response.status == 201, f"Ожидаем 201, получили {response.status}"
            response_text = response.text()


@allure.title("Создание кошелька AP")
@allure.description("Проверка успешного создания кошелька AP")
def test_create_wallet_internal_ap_success(api_request_context: APIRequestContext, access_token: str):
        """Тест проверяет успешное создание транзакции кошелька AP"""

        with allure.step("Создание и проверка кошелька AP"):
            response = create_wallet_internal_ap(api_request_context, access_token)

            assert response.status == 201, f"Ожидаем 201, получили {response.status}"
            response_text = response.text()


@allure.title("Создание кошелька Х личного кошелька")
@allure.description("Проверка успешного создания кошелька личного Х")
def test_create_wallet_external_x_personal_success(api_request_context: APIRequestContext, access_token: str):
        """Тест проверяет успешное создание кошелька Х личного"""

        with allure.step("Создание и проверка кошелька личного Х"):
            response = create_wallet_external_x_personal(api_request_context, access_token)

            assert response.status == 201, f"Ожидаем 201, получили {response.status}"
            response_text = response.text()




