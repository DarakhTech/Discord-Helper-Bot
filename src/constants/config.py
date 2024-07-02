import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants like bot token and Google Sheets settings
BOT_TOKEN = os.getenv('BOT_TOKEN')
SHEET_NAME = os.getenv('SHEET_NAME')
WORKSHEET_NAME = os.getenv('WORKSHEET_NAME')
GOOGLE_SHEETS_CREDENTIALS_PATH = 'src/constants/token.json'

# Add logging to check if the environment variables are loaded correctly
print(f"BOT_TOKEN: {BOT_TOKEN}")
print(f"SHEET_NAME: {SHEET_NAME}")
print(f"WORKSHEET_NAME: {WORKSHEET_NAME}")
print(f"Google Sheets Credentials Path: {GOOGLE_SHEETS_CREDENTIALS_PATH}")
