import random

work_pause_tasks = {}

async def wp(ctx, action: str, time: int = None, scheduler=None, break_messages=None, bot=None):
    """Starts or ends work-pause reminders. Usage: /work_pause start {time in minutes} or /work_pause end"""
    default_time = 30
    if action == 'start':
        if time is None:
            time = default_time
        if ctx.author.id in work_pause_tasks:
            await ctx.send('Work-pause already active.')
            return
        work_pause_tasks[ctx.author.id] = scheduler.add_job(work_pause_reminder, 'interval', minutes=time, args=[ctx.channel.id, ctx.author.id, break_messages, bot])
        await ctx.channel.purge()  
        await ctx.send(f'Work-pause started. You will be reminded to take a break every {time} minutes.')
    elif action == 'end':
        if ctx.author.id not in work_pause_tasks:
            await ctx.send('No active work-pause found.')
            return
        work_pause_tasks[ctx.author.id].remove()
        del work_pause_tasks[ctx.author.id]
        await ctx.send('Work-pause ended.')

async def work_pause_reminder(channel_id, user_id, break_messages, bot):
    channel = bot.get_channel(channel_id)
    if channel:
        message = random.choice(break_messages)
        await channel.send(f'<@{user_id}> - {message}')
