import pytest
import json
import allure
from playwright.sync_api import APIRequestContext

'''commissions - usdt'''

def create_commission_user(api_request_context: APIRequestContext, access_token: str):
    """Вспомогательная функция для создания транзакции комиссии"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
            "object_type_id": 1,
            "type": "user",
            "network": "bsc",
            "amount": 0.001
        }

    with allure.step("Отправка запроса на создание транзакции"):
        print(f"\nОтправляем payload: {json.dumps(payload, indent=2)}")

        response = api_request_context.post(
            "/api/v1/commissions/user",
            headers=headers,
            data=json.dumps(payload)
        )

        print(f"Статус ответа: {response.status}")
        print(f"Тело ответа: {response.text()}")

        return response


@allure.title("Создание транзакции комиссии")
@allure.description("Проверка успешного создания комиссии с токеном USDT")
def test_create_deposit_transaction_success(api_request_context: APIRequestContext, access_token: str):
    """Тест проверяет успешное создание транзакции депозита"""

    with allure.step("Создание и проверка комиссии"):
        response = create_commission_user(api_request_context, access_token)

        assert response.status == 201, f"Ожидаем 201, получили {response.status}"
        response_text = response.text()
