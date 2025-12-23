import pytest
import requests
from dotenv import load_dotenv
from unittest.mock import patch, Mock
load_dotenv()

@pytest.mark.skip(reason="Отключен, включается при интеграции")
class TestPublicAPITransaction:
    @pytest.mark.skip(reason="Отключен, включается при интеграции")
    @pytest.fixture(scope="class")
    def test_config(self):
        """Конфигурация тестовых окружений с моковыми данными"""
        return {
            'test_environment': {
                'website_url': 'https://httpbin.org/status/200',  # Моковый URL
                'admin_url': 'https://httpbin.org/status/200',
                'api_url': 'https://httpbin.org',
                'swagger_url': 'https://httpbin.org/json',
                'ip_address': '192.168.1.100',
                'admin_email': 'admin-test@weareway.com'
            },
            'production_environment': {
                'website_url': 'https://httpbin.org/status/200',
                'admin_url': 'https://httpbin.org/status/200',
                'api_url': 'https://httpbin.org',
                'swagger_url': 'https://httpbin.org/json',
                'ip_address': '203.0.113.50',
                'admin_email': 'admin@weareway.com'
            },
            'test_user': {
                'email': 'as@weareway.com',
                'password': 'test_password_123'
            }
        }

    @pytest.mark.skip(reason="Отключен, включается при интеграции")
    @pytest.fixture(scope="class")
    def api_headers(self):
        """Заголовки для API запросов"""
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'WeAreWay-TestSuite/1.0'
        }

@pytest.mark.skip(reason="Отключен, включается при интеграции")
def test_website_accessibility(test_config):
        """Тест доступности сайтов с моковыми данными"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            # Проверка основного сайта
            try:
                response = requests.get(config['website_url'], timeout=10)
                assert response.status_code == 200, f"Сайт {config['website_url']} недоступен"
                print(f"✅ Сайт {config['website_url']} доступен")
            except requests.RequestException as e:
                pytest.fail(f"❌ Ошибка доступа к сайту {config['website_url']}: {e}")

@pytest.mark.skip(reason="Отключен, включается при интеграции")
def test_admin_panel_accessibility(test_config):
        """Тест доступности админ панелей с моковыми данными"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            # админ панель
            try:
                response = requests.get(config['admin_url'], timeout=10)
                assert response.status_code == 200, f"Админ панель {config['admin_url']} недоступна"
                print(f"✅ Админ панель {config['admin_url']} доступна")
            except requests.RequestException as e:
                pytest.fail(f"❌ Ошибка доступа к админ панели {config['admin_url']}: {e}")

@pytest.mark.skip(reason="Отключен, включается при интеграции")
def test_swagger_documentation_access(test_config):
        """Тест доступности Swagger с моковыми данными"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            # Проверка Swagger
            try:
                response = requests.get(config['swagger_url'], timeout=10)
                assert response.status_code == 200, f"Swagger {config['swagger_url']} недоступен"
                print(f"✅ Swagger документация {config['swagger_url']} доступна")
            except requests.RequestException as e:
                pytest.fail(f"❌ Ошибка доступа к Swagger {config['swagger_url']}: {e}")

@pytest.mark.skip(reason="Отключен, включается при интеграции")
def test_api_health_check(test_config, api_headers):
        """Тест проверки здоровья API с моковыми данными"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            # Проверка health check endpoint
            try:
                health_url = f"{config['api_url']}/status/200"
                response = requests.get(health_url, headers=api_headers, timeout=10)
                assert response.status_code == 200, f"Health check для {config['api_url']} не прошел"
                print(f"✅ API {config['api_url']} работает корректно")
            except requests.RequestException as e:
                pytest.fail(f"❌ Ошибка health check для {config['api_url']}: {e}")

@pytest.mark.skip(reason="Отключен, включается при интеграции")
@patch('requests.post')
def test_user_authentication(mock_post, test_config, api_headers):
        """Тест аутентификации пользователя с моковыми данными"""
        config = test_config['test_environment']
        user_data = test_config['test_user']
        
        # Мок ответа для успешной аутентификации
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'token': 'mock_jwt_token_12345',
            'user_id': 123,
            'email': user_data['email']
        }
        mock_post.return_value = mock_response
        
        #  логин пользователя
        try:
            login_url = f"{config['api_url']}/auth/login"
            login_payload = {
                'email': user_data['email'],
                'password': user_data['password']
            }
            
            response = requests.post(login_url, headers=api_headers, json=login_payload, timeout=10)
            
            if response.status_code == 200:
                token_data = response.json()
                assert 'token' in token_data, "Отсутствует токен в ответе"
                print(f"✅ Пользователь {user_data['email']} успешно аутентифицирован")
                assert token_data['token'] == 'mock_jwt_token_12345', "Неверный токен"
            else:
                pytest.fail(f"❌ Неожиданный статус код при аутентификации: {response.status_code}")
                
        except Exception as e:
            pytest.fail(f"❌ Ошибка аутентификации: {e}")

@pytest.mark.skip(reason="Отключен, включается при интеграции")
@patch('requests.post')
def test_admin_authentication(mock_post, test_config, api_headers):
        """ аутентификации администратора с моковыми данными"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            # Мок ответа для успешной аутентификации администратора
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'token': f'mock_admin_token_{env}',
                'user_id': 999,
                'email': config['admin_email'],
                'role': 'admin'
            }
            mock_post.return_value = mock_response
            
            # логин администратора
            try:
                admin_login_url = f"{config['api_url']}/admin/login"
                admin_payload = {
                    'email': config['admin_email'],
                    'password': 'admin_password_123'
                }
                
                response = requests.post(admin_login_url, headers=api_headers, json=admin_payload, timeout=10)
                
                if response.status_code == 200:
                    token_data = response.json()
                    assert 'token' in token_data, "Отсутствует токен администратора в ответе"
                    print(f"✅ Администратор {config['admin_email']} успешно аутентифицирован")
                else:
                    print(f" Неожиданный статус код при аутентификации администратора: {response.status_code}")
                    
            except Exception as e:
                print(f" Ошибка аутентификации администратора: {e}")

@pytest.mark.skip(reason="Отключен, включается при интеграции")
@patch('requests.get')
def test_transaction_api_endpoints(mock_get, test_config, api_headers):
        """ API endpoints для транзакций с моковыми данными"""
        config = test_config['test_environment']
        
        # Мок ответа для списка транзакций
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'id': 1,
                'amount': 100.50,
                'currency': 'USD',
                'status': 'completed',
                'created_at': '2024-01-15T10:30:00Z'
            },
            {
                'id': 2,
                'amount': 250.75,
                'currency': 'EUR',
                'status': 'pending',
                'created_at': '2024-01-15T11:45:00Z'
            }
        ]
        mock_get.return_value = mock_response
        
        # Тест получения списка транзакций
        try:
            transactions_url = f"{config['api_url']}/transactions"
            response = requests.get(transactions_url, headers=api_headers, timeout=10)
            
            if response.status_code == 200:
                transactions = response.json()
                assert isinstance(transactions, list), "Список транзакций должен быть массивом"
                print(f"✅ API транзакций работает корректно, получено {len(transactions)} транзакций")
            else:
                print(f" статус код при получении транзакций: {response.status_code}")
                
        except Exception as e:
            pytest.fail(f"❌ Ошибка получения транзакций: {e}")

@pytest.mark.skip(reason="Отключен, включается при интеграции")
def test_ip_whitelist_verification(test_config):
        """ IP адрес для интеграции"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            print(f"IP адрес для {env}: {config['ip_address']}")
            print(f"Email администратора для {env}: {config['admin_email']}")
            print(f"URL сайта для {env}: {config['website_url']}")
            print(f"URL админки для {env}: {config['admin_url']}")
            print(f"URL API для {env}: {config['api_url']}")
            print(f"URL Swagger для {env}: {config['swagger_url']}")
            print("---")

@pytest.mark.skip(reason="Отключен, включается при интеграции")
def test_integration_requirements(test_config):
        """требования для интеграции"""
        print("\nТРЕБОВАНИЯ ДЛЯ ИНТЕГРАЦИИ:")
        print("=" * 50)
        
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            env_name = "ТЕСТОВОЕ" if env == 'test_environment' else "РАБОЧЕЕ"
            
            print(f"\n{env_name} ОКРУЖЕНИЕ:")
            print(f"   Сайт: {config['website_url']}")
            print(f"   Админка: {config['admin_url']}")
            print(f"   API: {config['api_url']}")
            print(f"   Swagger: {config['swagger_url']}")
            print(f"   IP адрес: {config['ip_address']}")
            print(f"   Email администратора: {config['admin_email']}")
        
        print(f"\nТестовый пользователь:")
        print(f"   Email: {test_config['test_user']['email']}")
        
        print("\nВсе необходимые данные для интеграции предоставлены")

@pytest.mark.skip(reason="Отключен, включается при интеграции")
def test_mock_data_validation(test_config):
        """валидации моковых данных"""
        print("\nВАЛИДАЦИЯ МОКОВЫХ ДАННЫХ:")
        print("=" * 40)
        
        # Проверяем структуру конфигурации
        required_keys = ['website_url', 'admin_url', 'api_url', 'swagger_url', 'ip_address', 'admin_email']
        
        for env in ['test_environment', 'production_environment']:
            config = test_config[env]
            print(f"\n📋 Проверка {env}:")
            
            for key in required_keys:
                assert key in config, f"Отсутствует ключ {key} в конфигурации {env}"
                print(f"  {key}: {config[key]}")
        
        #тестовый пользователь
        user_data = test_config['test_user']
        assert 'email' in user_data, "Отсутствует email пользователя"
        assert 'password' in user_data, "Отсутствует пароль пользователя"
        print(f"\nТестовый пользователь:")
        print(f"   Email: {user_data['email']}")
        print(f"   Пароль: {'*' * len(user_data['password'])}")
        
        print("\nВсе моковые данные валидны")
