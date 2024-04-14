import asyncio

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from repo import SubscriptionNotificationsRepo
from table import day_of_week_subjects


def setup_schedule_notifications(bot: Bot, repo: SubscriptionNotificationsRepo):
    for day_of_week in day_of_week_subjects:
        for subject, trigger_kwargs in day_of_week_subjects[day_of_week]:
            scheduler.add_job(
                send_notifications,
                trigger='cron',
                args=(f'Hey ! You will have {subject} in 5 minutes ‼️‼️‼️',),
                kwargs=dict(bot=bot, repo=repo),
                day_of_week=day_of_week,
                **trigger_kwargs
            )


async def send_notifications(text: str, bot: Bot, repo: SubscriptionNotificationsRepo):
    try:
        subscriptions_ids = await repo.get_subscriptions()
        for chat_id in subscriptions_ids:
            await bot.send_message(chat_id, text)
    except Exception as e:
        print(f"Error sending notification: {e}")


scheduler = AsyncIOScheduler(timezone="Europe/Bratislava")
