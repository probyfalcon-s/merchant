Запуск автотестов производится по URL
https://
предусловие: запускать с vpn (доступ у DevOps)
pip3 install -r requirements.txt - установить зависимости
установка Kiwi TCMS - pip install tcms-api или pip install git+https://github.com/kiwitcms/tcms-api.git
-запуск 
PYTHONPATH=$(pwd) pytest tests/

-запуск тестов с выводом статусов PASSED/ERROR/FAILED
PYTHONPATH=$(pwd) python3 -m pytest tests/ -v

-запуск только UI тестов
PYTHONPATH=$(pwd) python3 -m pytest tests/ -v --ignore=autotests/tests/api_tests/

- запуск только тестов API
PYTHONPATH=$(pwd) python3 -m pytest tests/api_tests/ -v

- запуск отдельных тестов 
pytest tests/test_deposit_bnb_web3.py -v 
-запуск двух тестов по очереди 
pytest tests/test_deposit_bnb_web3.py tests/ap_tests/test_get_token.py -v
pytest tests/api_tests/test_transaction_deposit_api.py tests/test_deposit_usdt_web3.py -v
pytest tests/api_tests/test_create_commission_api.py tests/test_deposit_usdt_web3.py -v 
pytest tests/api_tests/test_transaction_withdraw_api.py -v

TCMS Kiwi 
pytest tests/test_change_language.py::test_change_language -v --tcms


-allure
pytest tests/ --alluredir=allure_results - прогонка тестов с отчетов allure
allure serve allure_results - сформировать отчёт в формате веб-страницы
___
pages/ - основные и второстепенные методы
allure_results - отчеты в формате allure
config/settings - url адреса
data/test_data - тестовые данные для заполнения в поля

tests/test_dev - автотесты
-test_login - логирование на сайт
-test_transfer_pages - переход по всем страницам
-test_create_user - создание пользователя
-test_create_wallet - создание кошелька
-test_create_transaction - создание транзакции
-test_create_commission - создание комиссии
api_tests
тесты со стороны back

conftest - запуск браузера chrome (фикстура)
requirements.txt - установка зависимостей
readme - общий файл с описание всех модулей


запуск через docker 
# Через docker run
docker run --env-file .env your-image test

# Через docker-compose
docker-compose up