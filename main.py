import asyncio

from aiogram import Dispatcher, Bot

from config import TOKEN
from handlers import menu_router
from repo import SubscriptionNotificationsRepo
from scheduler import scheduler, setup_schedule_notifications


# Starting the bot
async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    # init routers
    dp.include_routers(menu_router, )
    # init repo
    repo = SubscriptionNotificationsRepo()
    dp['repo'] = repo
    # setup and start scheduler
    setup_schedule_notifications(bot, repo)
    scheduler.start()
    # start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
