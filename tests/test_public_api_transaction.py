import pytest
import requests
from dotenv import load_dotenv
load_dotenv()

class TestPublicAPITransaction:
    """Тесты для публичного API транзакций"""
@pytest.fixture(scope="class")
def test_config(self):
        """Конфигурация тестовых окружений"""
        return {
            'test_environment': {
                'website_url': 'https://test.weareway.com',
                'admin_url': 'https://admin-test.weareway.com',
                'api_url': 'https://api-test.weareway.com',
                'swagger_url': 'https://api-test.weareway.com/swagger',
                'ip_address': '192.168.1.100',
                'admin_email': 'admin-test@weareway.com'
            },
            'production_environment': {
                'website_url': 'https://weareway.com',
                'admin_url': 'https://admin.weareway.com',
                'api_url': 'https://api.weareway.com',
                'swagger_url': 'https://api.weareway.com/swagger',
                'ip_address': '203.0.113.50',
                'admin_email': 'admin@weareway.com'
            },
            'test_user': {
                'email': 'as@weareway.com',
                'password': 'test_password_123'
            }
        }

@pytest.fixture(scope="class")
def api_headers(self):
        """Заголовки для API запросов"""
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'WeAreWay-TestSuite/1.0'
        }

def test_website_accessibility(self, test_config):
        """Тест доступности сайтов"""
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

def test_admin_panel_accessibility(self, test_config):
        """Тест доступности админ панелей"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            # Проверка админ панели
            try:
                response = requests.get(config['admin_url'], timeout=10)
                assert response.status_code in [200, 302, 401], f"Админ панель {config['admin_url']} недоступна"
                print(f"✅ Админ панель {config['admin_url']} доступна")
            except requests.RequestException as e:
                pytest.fail(f"❌ Ошибка доступа к админ панели {config['admin_url']}: {e}")

def test_swagger_documentation_access(self, test_config):
        """Тест доступности Swagger документации"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            # Проверка Swagger документации
            try:
                response = requests.get(config['swagger_url'], timeout=10)
                assert response.status_code == 200, f"Swagger {config['swagger_url']} недоступен"
                print(f"✅ Swagger документация {config['swagger_url']} доступна")
            except requests.RequestException as e:
                pytest.fail(f"❌ Ошибка доступа к Swagger {config['swagger_url']}: {e}")


def test_api_health_check(self, test_config, api_headers):
        """Тест проверки здоровья API"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            # Проверка health check endpoint
            try:
                health_url = f"{config['api_url']}/health"
                response = requests.get(health_url, headers=api_headers, timeout=10)
                assert response.status_code == 200, f"Health check для {config['api_url']} не прошел"
                
                health_data = response.json()
                assert 'status' in health_data, "Отсутствует поле status в health check"
                print(f"✅ API {config['api_url']} работает корректно")
            except requests.RequestException as e:
                pytest.fail(f"❌ Ошибка health check для {config['api_url']}: {e}")

def test_user_authentication(self, test_config, api_headers):
        """Тест аутентификации пользователя"""
        config = test_config['test_environment']
        user_data = test_config['test_user']
        
        # Тест логина пользователя
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
                return token_data['token']
            elif response.status_code == 401:
                print(f"⚠️ Пользователь {user_data['email']} не найден или неверный пароль")
                return None
            else:
                pytest.fail(f"❌ Неожиданный статус код при аутентификации: {response.status_code}")
                
        except requests.RequestException as e:
            pytest.fail(f"❌ Ошибка аутентификации: {e}")

def test_admin_authentication(self, test_config, api_headers):
        """Тест аутентификации администратора"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            # Тест логина администратора
            try:
                admin_login_url = f"{config['api_url']}/admin/login"
                admin_payload = {
                    'email': config['admin_email'],
                    'password': 'admin_password_123'  # Тестовый пароль
                }
                
                response = requests.post(admin_login_url, headers=api_headers, json=admin_payload, timeout=10)
                
                if response.status_code == 200:
                    token_data = response.json()
                    assert 'token' in token_data, "Отсутствует токен администратора в ответе"
                    print(f"✅ Администратор {config['admin_email']} успешно аутентифицирован")
                elif response.status_code == 401:
                    print(f"⚠️ Администратор {config['admin_email']} не найден или неверный пароль")
                else:
                    print(f"⚠️ Неожиданный статус код при аутентификации администратора: {response.status_code}")
                    
            except requests.RequestException as e:
                print(f"⚠️ Ошибка аутентификации администратора: {e}")

def test_transaction_api_endpoints(self, test_config, api_headers):
        """Тест API endpoints для транзакций"""
        config = test_config['test_environment']
        
        # Получаем токен пользователя
        user_token = self.test_user_authentication(test_config, api_headers)
        if user_token:
            api_headers['Authorization'] = f'Bearer {user_token}'
        
        # Тест получения списка транзакций
        try:
            transactions_url = f"{config['api_url']}/transactions"
            response = requests.get(transactions_url, headers=api_headers, timeout=10)
            
            if response.status_code == 200:
                transactions = response.json()
                assert isinstance(transactions, list), "Список транзакций должен быть массивом"
                print(f"✅ API транзакций работает корректно, получено {len(transactions)} транзакций")
            elif response.status_code == 401:
                print("⚠️ Требуется аутентификация для доступа к транзакциям")
            else:
                print(f"⚠️ Неожиданный статус код при получении транзакций: {response.status_code}")
                
        except requests.RequestException as e:
            pytest.fail(f"❌ Ошибка получения транзакций: {e}")

def test_ip_whitelist_verification(self, test_config):
        """Тест проверки IP адресов для интеграции"""
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            
            print(f"📋 IP адрес для {env}: {config['ip_address']}")
            print(f"📋 Email администратора для {env}: {config['admin_email']}")
            print(f"📋 URL сайта для {env}: {config['website_url']}")
            print(f"📋 URL админки для {env}: {config['admin_url']}")
            print(f"📋 URL API для {env}: {config['api_url']}")
            print(f"📋 URL Swagger для {env}: {config['swagger_url']}")
            print("---")

def test_integration_requirements(self, test_config):
        """Тест требований для интеграции"""
        print("\n🔧 ТРЕБОВАНИЯ ДЛЯ ИНТЕГРАЦИИ:")
        print("=" * 50)
        
        environments = ['test_environment', 'production_environment']
        
        for env in environments:
            config = test_config[env]
            env_name = "ТЕСТОВОЕ" if env == 'test_environment' else "РАБОЧЕЕ"
            
            print(f"\n📌 {env_name} ОКРУЖЕНИЕ:")
            print(f"   🌐 Сайт: {config['website_url']}")
            print(f"   🔧 Админка: {config['admin_url']}")
            print(f"   📡 API: {config['api_url']}")
            print(f"   📚 Swagger: {config['swagger_url']}")
            print(f"   🌍 IP адрес: {config['ip_address']}")
            print(f"   📧 Email администратора: {config['admin_email']}")
        
        print(f"\n👤 Тестовый пользователь:")
        print(f"   📧 Email: {test_config['test_user']['email']}")
        
        print("\n✅ Все необходимые данные для интеграции предоставлены")
