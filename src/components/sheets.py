import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from src.constants import config

# Define the scope and credentials for Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(config.GOOGLE_SHEETS_CREDENTIALS_PATH, scope)
client = gspread.authorize(creds)

async def update(ctx, *, message: str):
    await update_sheet(ctx.channel.id, message, ctx.bot)
    
async def update_sheet(channel_id, message, bot):
    channel = bot.get_channel(channel_id)
    
    # Parse the JSON message
    try:
        data = json.loads(message)
        required_fields = ["Name of Company", "Job Title", "Job ID", "Link", "Status", "Location"]
        
        # Check if all required fields are present
        if not all(field in data for field in required_fields):
            await channel.send("Invalid JSON data. Ensure all required fields are present.")
            return
        
        # Append data to Google Sheets
        worksheet = client.open(config.SHEET_NAME).worksheet(config.WORKSHEET_NAME)
        row = [data["Name of Company"], data["Job Title"], data["Job ID"], data["Link"], data["Status"], data["Location"]]
        worksheet.append_row(row)
        
        await channel.send("Data successfully appended to Google Sheet.")
    except json.JSONDecodeError:
        await channel.send("Invalid JSON format.")
    except Exception as e:
        await channel.send(f"An error occurred: {e}")
