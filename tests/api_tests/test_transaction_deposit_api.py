import pytest
import json
import allure
from playwright.sync_api import APIRequestContext

'''deposit - usdt'''

def create_deposit_transaction(api_request_context: APIRequestContext, access_token: str):
    """Вспомогательная функция для создания транзакции депозита"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "user_id": 67,
        "address_uuid": "0x136b8aAbf0046e5f54A2852cd989dEE881f9CC89",
        "token": "usdt",
        "type": "deposit",
        "client": "metamask",
        "amount": 0.01
    }

    with allure.step("Отправка запроса на создание транзакции"):
        print(f"\nОтправляем payload: {json.dumps(payload, indent=2)}")
        
        response = api_request_context.post(
            "/api/v1/transactions/deposit",
            headers=headers,
            data=json.dumps(payload)
        )

        print(f"Статус ответа: {response.status}")
        print(f"Тело ответа: {response.text()}")
        
        return response


@allure.title("Создание транзакции депозита")
@allure.description("Проверка успешного создания транзакции депозита с токеном USDT")
def test_create_deposit_transaction_success(api_request_context: APIRequestContext, access_token: str):
    """Тест проверяет успешное создание транзакции депозита"""

    with allure.step("Создание и проверка транзакции депозита"):
        response = create_deposit_transaction(api_request_context, access_token)

        assert response.status == 201, f"Ожидаем 201, получили {response.status}"
        response_text = response.text()


