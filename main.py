import asyncio
import datetime
from table import *

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import CallbackQuery


bot = Bot(token="7187636386:AAF251aM6bl5pjzZQqFJbblJATcEFL_rHHY")
dp = Dispatcher()
scheduler = AsyncIOScheduler()
scheduler.start()


# Function /start
@dp.message(Command("start"))
async def start(message: types.Message):
    first_mess = (
        f"{message.from_user.first_name}, hi!\n\nI'm Tfik! I'm a bot that will "
        f"help you remember your lesson at the university! I will send you a message (reminder) 5 minutes "
        f"before your lesson!\n\nChoose, the action:"
    )
    await message.answer(text=first_mess, reply_markup=await main_kb())


# Table with actions
@dp.message(Command("actions"))
async def cmd_menu_action(message: types.Message):
    await message.answer(text="How can I help you?", reply_markup=await main_kb())


@dp.message(F.user == "Week schedule 📋📌")
async def week_schedule_button(message: types.Message):
    await message.answer(text=lessons, reply_markup=await main_kb())


# Bot do actions when user write function /week_schedule
@dp.message(Command("week_schedule"))
async def week_schedule_cmd(message: types.Message):
    await message.answer(text=lessons, reply_markup=await main_kb())


@dp.message(F.text == "Daily schedule ‼️")
async def week_schedule_button(message: types.Message):
    today = datetime.datetime.now().weekday()

    if today == 0:
        await message.answer(text=monday, reply_markup=await main_kb())

    elif today == 1:
        await message.answer(text=tuesday, reply_markup=await main_kb())

    elif today == 2:
        await message.answer(text=wednesday, reply_markup=await main_kb())

    elif today == 3:
        await message.answer(text=thursday, reply_markup=await main_kb())

    elif today == 4:
        await message.answer(text=friday, reply_markup=await main_kb())

    elif today == 5:
        await message.answer(text=saturday, reply_markup=await main_kb())

    elif today == 6:
        await message.answer(text=sunday, reply_markup=await main_kb())


# Bot do actions when user write function /daily_schedule
@dp.message(Command("daily_schedule"))
async def daily_schedule_cmd(message: types.Message):
    today = datetime.datetime.now().weekday()

    if today == 0:
        await message.answer(text=monday, reply_markup=await main_kb())

    elif today == 1:
        await message.answer(text=tuesday, reply_markup=await main_kb())

    elif today == 2:
        await message.answer(text=wednesday, reply_markup=await main_kb())

    elif today == 3:
        await message.answer(text=thursday, reply_markup=await main_kb())

    elif today == 4:
        await message.answer(text=friday, reply_markup=await main_kb())

    elif today == 5:
        await message.answer(text=saturday, reply_markup=await main_kb())

    elif today == 6:
        await message.answer(text=sunday, reply_markup=await main_kb())


# Button exams
@dp.message(F.text == "Dates of tests and exams ☠️")
async def week_schedule_button(message: types.Message):
    await message.answer(text=tests_exams, reply_markup=await main_kb())


# func /exams
@dp.message(Command("exams"))
async def week_schedule_cmd(message: types.Message):
    await message.answer(text=tests_exams, reply_markup=await main_kb())


# func /turn_on
@dp.callback_query(F.data == "turn_on")
async def turn_on_cmd(callback: CallbackQuery):
    await toggle_notifications(callback, True)


# func /turn_off
@dp.callback_query(F.data == "turn_off")
async def turn_off_cmd(callback: CallbackQuery):
    await toggle_notifications(callback, True)


async def toggle_notifications(callback_query: CallbackQuery, enable: bool):
    if enable:
        await schedule_notifications(callback_query)
        await callback_query.answer(text="Notifications are enabled 🔔", show_alert=True)
    else:
        await stop_notifications()
        await callback_query.answer(text="Notifications are disabled 🔕", show_alert=True)


# Starting the bot
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
