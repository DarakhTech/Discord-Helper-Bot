import random
import hashlib
import aiohttp
import bs4


async def hash(ctx, *, message: str):
    await ctx.channel.purge(limit=1)
    await send_message(ctx.channel.id, message, encode_text(message), ctx.bot)
    
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
            f"""The hash for {message}\n{hashstr}\n{title_text}\n```/update
            {{
                "Name of Company": "",
                "Job Title": "",
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