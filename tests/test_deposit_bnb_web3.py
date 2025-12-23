from web3 import Web3
from web3.exceptions import Web3RPCError
import time
import pytest
import os
from dotenv import load_dotenv


load_dotenv()

'''mainnet - bnb - кошелек 0xCC9316F79e6d8a8f5610723C40FD3f6574202336'''

class TestBNBDeposit:
    @pytest.fixture(scope="class")
    def web3_connection(self):
        """Установка подключения к BNB Mainnet"""
        web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.nariox.org"))
        assert web3.is_connected(), "Нет подключения к BNB Mainnet"
        return web3

    @pytest.fixture(scope="class")
    def transaction_params(self, web3_connection):
        """Установка параметров транзакции"""
        return {
            'private_key': os.getenv("WEB3_PRIVATE_KEY"),  # 🔐 Приватный ключ отправителя
            'sender_address': web3_connection.to_checksum_address(os.getenv("SENDER_ADDRESS")), #account main _metamask
            'recipient_address': web3_connection.to_checksum_address(os.getenv("RECIPIENT_ADDRESS")), #куда отправляем
            'value': web3_connection.to_wei(0.00001, 'ether'),  # Количество BNB для отправки
            'gas_limit': 40000,  # Лимит газа для обычного перевода
            'chain_id': 56,
            'base_gas_price': web3_connection.to_wei('10', 'gwei'),  # Базовая цена газа
            'max_gas_price': web3_connection.to_wei('50', 'gwei'),  # Максимальная цена газа
            'step_gas_price': web3_connection.to_wei('2', 'gwei')  # Шаг увеличения цены газа
        }


def test_bnb_deposit(self, web3_connection, transaction_params):
        """Тест депозита BNB"""
        web3 = web3_connection
        nonce = web3.eth.get_transaction_count(transaction_params['sender_address'], 'pending')
        base_gas_price = transaction_params['base_gas_price']
        
        while base_gas_price <= transaction_params['max_gas_price']:
            try:
                tx = {
                    'nonce': nonce,
                    'to': transaction_params['recipient_address'],
                    'value': transaction_params['value'],
                    'gas': transaction_params['gas_limit'],
                    'gasPrice': base_gas_price,
                    'chainId': transaction_params['chain_id']
                }

                # Подпись и отправка транзакции
                signed_tx = web3.eth.account.sign_transaction(tx, private_key=transaction_params['private_key'])
                tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
                
                # Ожидание получения квитанции транзакции
                tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
                
                print(f"✅ Транзакция отправлена: {web3.to_hex(tx_hash)}")
                
                # Проверка успешности транзакции
                assert tx_receipt['status'] == 1, "Транзакция не удалась"
                assert tx_receipt['to'].lower() == transaction_params['recipient_address'].lower(), "Неверный адрес получателя"
                assert tx_receipt['from'].lower() == transaction_params['sender_address'].lower(), "Неверный адрес отправителя"
                break

            except Web3RPCError as e:
                error_message = str(e)
                if 'underpriced' in error_message or 'already known' in error_message:
                    print(f"⚠️ {error_message} — увеличиваем цену газа...")
                    base_gas_price += transaction_params['step_gas_price']
                    time.sleep(1)
                else:
                    pytest.fail(f"❌ Ошибка RPC: {error_message}")

            except Exception as e:
                pytest.fail(f"❌ Неизвестная ошибка: {e}")