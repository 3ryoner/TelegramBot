import asyncio

from aiogram import Bot
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from repo import SubscriptionNotificationsRepo


def setup_schedule_notifications(bot: Bot, repo: SubscriptionNotificationsRepo):
    day_of_week_subjects = {
        'tue': [
            ("PPI (cvicenie)", dict(hour=9, minute=5)),
            ("ZSI (prednaska)", dict(hour=10, minute=45)),
            ("Programovanie (cvicenie)", dict(hour=13, minute=25)),
        ],
        'wed': [
            ("Programovanie (prednaska)", dict(hour=8, minute=10)),
            ("Matematika 2 (prednaska)", dict(hour=9, minute=50)),
            ("PPI (prednaska)", dict(hour=15, minute=5)),
        ],
        'thu': [
            ("Matematika 2 (cvicenie)", dict(hour=8, minute=10)),
            ("Fyzika 1 (cvicenie)", dict(hour=9, minute=50)),
            ("ZSI (cvicenie)", dict(hour=13, minute=25)),
        ]
    }
    for day_of_week in day_of_week_subjects:
        for subject, triger_kwargs in day_of_week_subjects[day_of_week]:
            scheduler.add_job(send_notifications, 'cron', args=(f'Hey ! You will have {subject} in 5 minutes !!!', ), kwargs=dict(bot=bot, repo=repo), day_of_week=day_of_week, **triger_kwargs)

async def send_notifications(text: str, bot: Bot, repo: SubscriptionNotificationsRepo):
    subscriptions_ids = await repo.get_subscriptions()
    for chat_id in subscriptions_ids:
        try:
            await bot.send_message(chat_id, text)
            await asyncio.sleep(0.25)
        except Exception as e:
            await asyncio.sleep(0.5)
            # Обработка ошибок при отправке уведомления
            print(f"Ошибка при отправке уведомления: {e}")


scheduler = AsyncIOScheduler()
