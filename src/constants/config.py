import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Constants like bot token and Google Sheets settings
BOT_TOKEN = os.getenv('BOT_TOKEN')
SHEET_NAME = os.getenv('SHEET_NAME')
WORKSHEET_NAME = os.getenv('WORKSHEET_NAME')

# Google Sheets credentials
GOOGLE_SHEETS_CREDENTIALS = {
    "type": os.getenv('GOOGLE_SHEETS_TYPE'),
    "project_id": os.getenv('GOOGLE_SHEETS_PROJECT_ID'),
    "private_key_id": os.getenv('GOOGLE_SHEETS_PRIVATE_KEY_ID'),
    "private_key": os.getenv('GOOGLE_SHEETS_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.getenv('GOOGLE_SHEETS_CLIENT_EMAIL'),
    "client_id": os.getenv('GOOGLE_SHEETS_CLIENT_ID'),
    "auth_uri": os.getenv('GOOGLE_SHEETS_AUTH_URI'),
    "token_uri": os.getenv('GOOGLE_SHEETS_TOKEN_URI'),
    "auth_provider_x509_cert_url": os.getenv('GOOGLE_SHEETS_AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url": os.getenv('GOOGLE_SHEETS_CLIENT_X509_CERT_URL'),
    "universe_domain": os.getenv('GOOGLE_SHEETS_UNIVERSE_DOMAIN')
}
