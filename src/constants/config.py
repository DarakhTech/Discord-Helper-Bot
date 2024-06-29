import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants like bot token and Google Sheets settings
BOT_TOKEN = os.getenv('BOT_TOKEN')
GOOGLE_SHEETS_CREDENTIALS_PATH = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
SHEET_NAME = os.getenv('SHEET_NAME')
WORKSHEET_NAME = os.getenv('WORKSHEET_NAME')
