from datetime import datetime

async def add_event(ctx, date: str, time: str, *, event: str, scheduler, bot):
    """Adds an event to the calendar. Usage: /add_event YYYY-MM-DD HH:MM Event"""
    event_time = datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M')
    scheduler.add_job(send_event, 'date', run_date=event_time, args=[ctx.channel.id, event, bot])
    await ctx.send(f'Event "{event}" scheduled for {date} at {time}')

async def send_event(channel_id, event, bot):
    channel = bot.get_channel(channel_id)
    await channel.send(f'Event reminder: {event}')
