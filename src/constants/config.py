import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Constants like bot token and Google Sheets settings
BOT_TOKEN = os.getenv('BOT_TOKEN')
SHEET_NAME = os.getenv('SHEET_NAME')
WORKSHEET_NAME = os.getenv('WORKSHEET_NAME')
GOOGLE_SHEETS_CREDENTIALS_PATH = 'src/constants/token.json'