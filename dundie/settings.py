import os

SMTP_HOST = 'localhost'
SMTP_PORT = 8025
SMTP_TIMEOUT = 5
ROOT_PATH = os.path.dirname(__file__)
DATABASE_PATH = os.path.join(ROOT_PATH, '..', 'assets', 'database.json')
EMAIL_FROM = 'master@dundie.com'
