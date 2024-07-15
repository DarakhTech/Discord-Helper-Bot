import random
import hashlib

async def hash(ctx, *, message: str):
    await send_message(ctx.channel.id, message, encode_text(message), ctx.bot)
    
async def send_message(channel_id, message, hashstr, bot):
    channel = bot.get_channel(channel_id)
    try:
        await channel.send(f"The hash for {message}\n{hashstr}")
    except Exception as e:
        await channel.send(f"An error occurred: {e}")


        
def encode_text(text):
    text = text.replace(" ", "")
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    encoded_string = sha256_hash[:20]
    return encoded_string