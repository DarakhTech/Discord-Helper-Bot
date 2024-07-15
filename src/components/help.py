import discord
from discord.ext import commands

def get_commands_embed():
    embed = discord.Embed(
        title="Bot Commands",
        description="Here are the commands you can use with this bot:",
        color=discord.Color.blurple()
    )
    embed.add_field(
        name="/remind HH:MM Message",
        value="Sets a reminder at the specified time with the given message.",
        inline=False
    )
    embed.add_field(
        name="/add_event YYYY-MM-DD HH:MM Event",
        value="Schedules an event at the specified date and time with the given event description.",
        inline=False
    )
    embed.add_field(
        name="/wp start {time in minutes}",
        value="Starts work-pause reminders. You will be reminded to take a break every specified minutes.",
        inline=False
    )
    embed.add_field(
        name="/wp end",
        value="Ends the work-pause reminders.",
        inline=False
    )
    embed.add_field(
        name="/id message",
        value="Return HASH ID for the given message.",
        inline=False
    )
    embed.set_footer(text="Use these commands to interact with the bot.")
    return embed

@commands.command()
async def help_embed(ctx):
    embed = get_commands_embed()
    await ctx.send(embed=embed)
