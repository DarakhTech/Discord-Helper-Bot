from datetime import datetime, timedelta

async def remind(ctx, time: str, *, message: str, scheduler, bot):
    """Sets a reminder. Usage: /remind HH:MM Message"""
    now = datetime.now()
    remind_time = datetime.strptime(time, '%H:%M').replace(year=now.year, month=now.month, day=now.day)
    if remind_time < now:
        remind_time += timedelta(days=1)
    scheduler.add_job(send_reminder, 'date', run_date=remind_time, args=[ctx.channel.id, message, bot])
    await ctx.send(f'Reminder set for {time}')

async def send_reminder(channel_id, message, bot):
    channel = bot.get_channel(channel_id)
    await channel.send(message)
