import pytest
from web3 import Web3
from web3.exceptions import Web3RPCError
import time
import os
from dotenv import load_dotenv


load_dotenv()

'''mainnet - usdt - кошелек 0xCC9316F79e6d8a8f5610723C40FD3f6574202336'''

# === Константы ===
MAINNET_RPC = "https://bsc-dataseed.nariox.org"
PRIVATE_KEY = os.getenv("WEB3_PRIVATE_KEY")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")
RECIPIENT_ADDRESS = os.getenv("RECIPIENT_ADDRESS") #куда account_1
# RECIPIENT_ADDRESS = "0xd84aBdBEe2723ce55AbADF93EC19e22477D7E8eB" #AP mainnet prod
USDT_CONTRACT_ADDRESS = "0x55d398326f99059fF775485246999027B3197955"  # mainnet USDT

ERC20_ABI = [{
    "constant": False,
    "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
    "name": "transfer",
    "outputs": [{"name": "", "type": "bool"}],
    "type": "function"
}]

def test_send_usdt_transaction():
    web3 = Web3(Web3.HTTPProvider(MAINNET_RPC))
    assert web3.is_connected(), "❌ Нет подключения к BNB mainnet"

    sender = web3.to_checksum_address(SENDER_ADDRESS)
    recipient = web3.to_checksum_address(RECIPIENT_ADDRESS)
    token_contract = web3.eth.contract(address=web3.to_checksum_address(USDT_CONTRACT_ADDRESS), abi=ERC20_ABI)

    amount = 0.1 #кол-во USDT
    decimals = 6  # ⚠️  точность, зависит от USDT (либо 6 на mainnet)
    amount_wei = int(amount * 10**decimals)

    nonce = web3.eth.get_transaction_count(sender, 'pending')

    base_gas_price = web3.to_wei('10', 'gwei')
    max_gas_price = web3.to_wei('50', 'gwei')
    step_gas_price = web3.to_wei('2', 'gwei')

    while base_gas_price <= max_gas_price:
        try:
            tx = token_contract.functions.transfer(
                recipient,
                amount_wei
            ).build_transaction({
                'from': sender,
                'nonce': nonce,
                'gas': 40000,
                'gasPrice': base_gas_price,
                'chainId': 56
            })

            signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

            print(f"✅ USDT транзакция отправлена: {web3.to_hex(tx_hash)}")
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)

            assert receipt.status == 1, "❌ Транзакция завершилась с ошибкой"
            break

        except Web3RPCError as e:
            msg = str(e)
            if 'underpriced' in msg or 'already known' in msg:
                print(f"⚠️ {msg} — увеличиваем gasPrice...")
                base_gas_price += step_gas_price
                time.sleep(1)
            else:
                pytest.fail(f"❌ RPC ошибка: {msg}")

        except Exception as ex:
            pytest.fail(f"❌ Ошибка при отправке: {ex}")