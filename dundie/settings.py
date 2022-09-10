import os

SMTP_HOST = 'localhost'
SMTP_PORT = 8025
SMTP_TIMEOUT = 5

EMAIL_FROM: str = 'master@dundie.com'
API_BASE_URL: str = "https://economia.awesomeapi.com.br/json/last/USD-{currency}"
ROOT_PATH: str = os.path.dirname(__file__)
DATABASE_PATH: str = os.path.join(ROOT_PATH, '..', 'assets', 'database.db')
SQL_CONN_STRING: str = f'sqlite:///{DATABASE_PATH}'
DATEFMT: str = '%d/%m/%Y %H:%M:%S'
