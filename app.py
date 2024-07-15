import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.constants import config
from src.components import events, reminder, work_pause, help, sheets, id

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Enable member intent

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    user = await bot.fetch_user('564861175997661184')
    if user:
        await user.send(f'Bot is ready. Logged in as {bot.user}')

# Register commands
bot.add_command(help.help_embed)

@bot.command()
async def remind(ctx, time: str, *, message: str):
    await events.remind(ctx, time, message=message, scheduler=AsyncIOScheduler(), bot=bot)

@bot.command()
async def add_event(ctx, date: str, time: str, *, event: str):
    await reminder.add_event(ctx, date, time, event=event, scheduler=AsyncIOScheduler(), bot=bot)

@bot.command()
async def wp(ctx, action: str, time: int = None):
    await work_pause.wp(ctx, action, time, scheduler=AsyncIOScheduler(), break_messages=[
        "Time for a quick 30-second break! Step away and stretch!",
        "Take a 30-second break to relax your mind. You deserve it!",
    ], bot=bot)

@bot.command()
async def update(ctx, *, message: str):
    await sheets.update(ctx, message=message)

async def id(ctx, *, message: str):
    await id.hash(ctx, message=message)


bot.run(config.BOT_TOKEN)
