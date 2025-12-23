import os
from dotenv import load_dotenv


load_dotenv()

TEST_DATA = {
    'login': os.getenv('ADMIN_LOGIN'),
    'password': os.getenv('ADMIN_PASSWORD')
} #dev admin

TEST_DATA_CLIENT = {
    'login': os.getenv('DEV_USER_EMAIL'),
    'password': os.getenv('DEV_USER_PASSWORD')
} #dev user


TEST_DATA_USER = {
    'name': 'Alex_Biba_010',
    'description': 'description_81',
    'email': 'cok111@coo8k.com',
    'ip4': '183.87.275.18',
    'balance_commissions': '18'
}

TEST_DATA_WALLET = {
    'id_user': '1232',
    'address': '0xCC9316F79e6d8a8f5610723C40FD3f6574202336', #metamask второй кошелек, мало мани
    'secret_key': '56te34'
}


TEST_DATA_TRANSACTION = {
    'client': '1232',
    'amount': '0.001',
    'amount_usdt': '0.001',
    'address_client': '0x9bA77BE511BbA03B8A559C2C9bfAdb77119117f4' #metamask много мани
}


TEST_DATA_COMMISSION = {
    'amount_commission': '0.01'
}
