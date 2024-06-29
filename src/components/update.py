from discord.ext import commands
from src.components.sheets import update_sheet

class UpdateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def update(self, ctx, *, message: str):
        await update_sheet(ctx.channel.id, message, self.bot)
