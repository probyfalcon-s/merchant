import pytest
import json
import allure
from playwright.sync_api import APIRequestContext

'''withdraw - usdt'''

def create_withdrawal_transaction(api_request_context: APIRequestContext, access_token: str):
    """Вспомогательная функция для создания транзакции вывода"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "user_id": 67,
        "address_uuid": "0x1552255c99DDC0Fa8e9329F5016782BDCB18f135",
        "token": "usdt",
        "type": "withdrawal",
        "address_client": "0xCC9316F79e6d8a8f5610723C40FD3f6574202336",
        "client": "metamask",
        "amount": 0.0001
    }


    with allure.step("Отправка запроса на создание транзакции депозита"):
        print(f"\nОтправляем payload: {json.dumps(payload, indent=2)}")

        response = api_request_context.post(
            "/api/v1/transactions/withdrawal",
            headers=headers,
            data=json.dumps(payload)
        )

        print(f"Статус ответа: {response.status}")
        print(f"Тело ответа: {response.text()}")

        return response


@allure.title("Создание транзакции вывода")
@allure.description("Проверка успешного создания транзакции депозита с токеном USDT")
def test_create_withdrawal_transaction_success(api_request_context: APIRequestContext, access_token: str):
    """Тест проверяет успешное создание транзакции вывода"""

    with allure.step("Создание и проверка транзакции вывода"):
        response = create_withdrawal_transaction(api_request_context, access_token)

        assert response.status == 201, f"Ожидаем 201, получили {response.status}"
        response_text = response.text()


