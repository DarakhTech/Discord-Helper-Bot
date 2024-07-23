import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from src.constants import config
import datetime

# Define the scope for Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Use the credentials from the JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name(config.GOOGLE_SHEETS_CREDENTIALS_PATH, scope)
client = gspread.authorize(creds)

async def update(ctx, *, message: str):
    await update_sheet(ctx, ctx.channel.id, message, ctx.bot)
    
async def update_sheet(ctx, channel_id, message, bot):
    date = datetime.datetime.now()
    if not client:
        channel = bot.get_channel(channel_id)
        await channel.send("Google Sheets client not initialized. Credentials are missing.")
        return
    
    channel = bot.get_channel(channel_id)
    
    # Parse the JSON message
    try:
        message = message.replace('`','')
        data = json.loads(message)
        required_fields = ["Name of Company", "Job Title", "Job ID", "Link", "Status", "Location"]
        
        # Check if all required fields are present
        if not all(field in data for field in required_fields):
            await channel.send("Invalid JSON data. Ensure all required fields are present.")
            return
        
        # Append data to Google Sheets
        worksheet = client.open(config.SHEET_NAME).worksheet(config.WORKSHEET_NAME)
        row = [data["Name of Company"], data["Job Title"], data["Job ID"], data["Link"], data["Status"], data["Location"], date.strftime("%d %B") ]
        worksheet.append_row(row)
        await ctx.channel.purge(limit=2)
        await channel.send(
            f"""## {data["Name of Company"]} ```Title:{data["Job Title"]}\nID:{data["Job ID"]}```{data["Link"]}"""
        )
        
    except json.JSONDecodeError:
        await channel.send("Invalid JSON format.")
    except gspread.exceptions.APIError as e:
        await channel.send(f"Google Sheets API error: {e}")
    except Exception as e:
        await channel.send(f"An error occurred: {e}")
