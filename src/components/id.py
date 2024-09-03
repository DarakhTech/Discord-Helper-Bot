import random
import hashlib
import aiohttp
import bs4
from oauth2client.service_account import ServiceAccountCredentials
from src.constants import config
import datetime
import json
import gspread
import pandas as pd

# Define the scope for Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Use the credentials from the JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name(config.GOOGLE_SHEETS_CREDENTIALS_PATH, scope)
client = gspread.authorize(creds)

async def get_id(encoded_id):
    worksheet = client.open(config.SHEET_NAME).worksheet(config.WORKSHEET_NAME)
    records = worksheet.get_all_records()
    df = pd.DataFrame(records)
    if encoded_id in df['ID'].values:
        return False
    return True
    # try:
    #     sheet = client.open_by_key(config.SHEET_NAME).worksheet(config.WORKSHEET_NAME)
    #     records = sheet.get_all_records()
    #     print(records)
    #     df = pd.DataFrame(records)
    #     if encoded_id in df['ID'].values:
    #         return False
    #     return True
    # except Exception as e:
    #     print(f"An error occurred while checking ID: {e}")
    #     return False

async def hash(ctx, *, message: str):
    await ctx.channel.purge(limit=1)
    encoded_id = encode_text(message)
    if await get_id(encoded_id):
        await send_message(ctx.channel.id, message, encoded_id, ctx.bot)
    else:
        sent_message = await ctx.send(f"ID {encoded_id} already exists.")
        await sent_message.add_reaction('❌')

        

    
async def get_title(link):
    returnstr = ""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                response.raise_for_status()  # Ensure we handle HTTP errors
                html = bs4.BeautifulSoup(await response.text(), features="lxml")
                returnstr = html.title.text if html.title else "No title found"
    except aiohttp.ClientError as e:
        print(f"HTTP request error: {e}")
    except bs4.FeatureNotFound as e:
        print(f"BeautifulSoup feature error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return returnstr
    
async def send_message(channel_id, message, hashstr, bot):
    
    channel = bot.get_channel(channel_id)
    title_text = await get_title(message)
    try:
        await channel.send(
            f"""The hash for {message}\n{hashstr}\n```/update
            {{
                "Name of Company": "",
                "Job Title": "{title_text}",
                "Job ID": "{hashstr}",
                "Link": "{message}",
                "Status": "Looking",
                "Location": ""
            }}```"""
        )


    except Exception as e:
        await channel.send(f"An error occurred: {e}")


        
def encode_text(text):
    text = text.replace(" ", "")
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    encoded_string = sha256_hash[:20]
    return encoded_string