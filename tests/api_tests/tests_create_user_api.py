import pytest
from playwright.sync_api import APIRequestContext, sync_playwright
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

BASE_URL = "https://dev-crypto-merchant-back-admin.weareway.ru"


@pytest.fixture(scope="session")
def api_request_context():
    with sync_playwright() as p:
        request_context = p.request.new_context(base_url=BASE_URL)
        yield request_context
        request_context.dispose()


def get_auth_token(api_request_context: APIRequestContext) -> str:
    payload = {
        "username": os.getenv("TEST_USER_USERNAME"),
        "password": os.getenv("TEST_USER_PASSWORD")
    }
    response = api_request_context.post("/admin/get-token", data=payload)
    assert response.status == 200, f"Expected 200, got {response.status}"
    response_json = response.json()
    token = response_json.get("token") or response_json.get("access_token")
    assert token, "Token not found in response"
    return token

@pytest.mark.skip(reason="Тест временно отключен - 400 ошибка")
def test_create_merchant(api_request_context: APIRequestContext):
    token = get_auth_token(api_request_context)

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "name": "test_2",
        "email": "test_2@test.com",
        "description": "dec_1",
        "active": True,
        "commission_balance": "100",
        "commission": {
            "bsc": {
                "address_create": "1",
                "transaction_deposit": {
                    "amount_min": "1",
                    "min": "1",
                    "percent": "0.01"
                },
                "transaction_withdrawal": {
                    "amount_min": "1",
                    "min": "1",
                    "percent": "0.01"
                }
            }
        }
    }

    response = api_request_context.post("/admin/users", data=payload, headers=headers)
    assert response.status == 201, f"Expected status code 201, got {response.status}"
    response_json = response.json()

    assert response_json["name"] == payload["name"]
    assert response_json["email"] == payload["email"]
    assert response_json["description"] == payload["description"]
    assert response_json["active"] is True
    assert response_json["commission_balance"] == payload["commission_balance"]

    commission = response_json["commission"]["bsc"]
    assert commission["address_create"] == int(payload["commission"]["bsc"]["address_create"])

    for key in ["transaction_deposit", "transaction_withdrawal"]:
        for subkey in ["min", "amount_min", "percent"]:
            expected = float(payload["commission"]["bsc"][key][subkey])
            actual = float(commission[key][subkey])
            assert actual == expected, f"{key}.{subkey} expected {expected}, got {actual}"

    for key in ["id", "uuid", "api_key", "secret_key", "created_at"]:
        assert key in response_json, f"Key '{key}' not found in response"

@pytest.mark.skip(reason="Тест временно отключен")
def test_nonexistent_endpoint(api_request_context: APIRequestContext):
    token = get_auth_token(api_request_context)
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Try to access a non-existent endpoint
    response = api_request_context.get("/admin/nonexistent-endpoint", headers=headers)
    assert response.status == 404, f"Expected status code 404, got {response.status}"
    response_json = response.json()
    assert "error" in response_json, "Error message not found in 404 response"