import os

SMTP_HOST = 'localhost'
SMTP_PORT = 8025
SMTP_TIMEOUT = 5

EMAIL_FROM = 'master@dundie.com'

ROOT_PATH = os.path.dirname(__file__)
DATABASE_PATH = os.path.join(ROOT_PATH, '..', 'assets', 'database.DB')
SQL_CONN_STRING: str = f'sqlite:///{DATABASE_PATH}'
DATEFMT: str = '%d/%m/%Y %H:%M:%S'
