import pytest
from playwright.sync_api import APIRequestContext
import os
from dotenv import load_dotenv


load_dotenv()

@pytest.mark.skip(reason="Тест временно отключен")
def test_get_token_success(api_request_context: APIRequestContext):
    payload = {
        "email": os.getenv("DEV_USER_EMAIL"),
        "password": os.getenv("DEV_USER_PASSWORD")
    }

    response = api_request_context.post("/get-token", data=payload)
    assert response.status == 200, f"Ожидаем 200 код, получили {response.status}"

    response_json = response.json()
    print("Успешный ответ:", response_json)

    assert "token" in response_json or "access_token" in response_json, "Токен не найден"
    token = response_json.get("token") or response_json.get("access_token")
    assert isinstance(token, str) and len(token) > 10, "Неверный токен"

@pytest.mark.skip(reason="Тест временно отключен")
def test_get_token_invalid_credentials(api_request_context: APIRequestContext):
    payload = {
        "username": "wrong_user",
        "password": "wrong_pass"
    }

    response = api_request_context.post("/admin/get-token", data=payload)

    assert response.status == 401, f"Ожидаем 401 код, получили {response.status}"

    response_json = response.json()
    print("Ошибочный ответ:", response_json)

    assert response_json.get("error") is True
    assert response_json.get("message") == "Access Denied: Login or Password error"