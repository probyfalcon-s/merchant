import json
import allure
import pytest
from playwright.sync_api import APIRequestContext

'''withdraw - usdt'''

@pytest.mark.skip(reason="Отключен, включается при массовом переводе")
def create_withdrawal_transaction(api_request_context: APIRequestContext, access_token: str):
    """Вспомогательная функция для создания транзакции вывода"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        # "user_id": 57, #stage
        "user_id": 67, #dev
        "address_uuid": "0x1552255c99DDC0Fa8e9329F5016782BDCB18f135", #address dev X wallet id 67
        # "address_uuid": "0x000c79569D831523f0b3f0F1f041dECF5605C37a",  # address stage X wallet id 57
        "token": "usdt",
        "type": "withdrawal",
        "address_client": "0xCC9316F79e6d8a8f5610723C40FD3f6574202336",
        "client": "metamask_test",
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


@pytest.mark.skip(reason="Отключен, включается при массовом переводе")
@allure.title("Создание транзакции вывода")
@allure.description("Проверка успешного создания транзакции депозита с токеном USDT")
def test_create_withdrawal_transaction_success(api_request_context: APIRequestContext, access_token: str):
    """Тест проверяет успешное создание транзакции вывода"""

    with allure.step("Создание и проверка транзакции вывода"):
        response = create_withdrawal_transaction(api_request_context, access_token)

        assert response.status == 201, f"Ожидаем 201, получили {response.status}"
        response_text = response.text()


