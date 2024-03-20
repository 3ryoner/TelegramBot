from aiogram import Router
from aiogram import types, F
from aiogram.filters.command import Command
from aiogram.types import User, Message, ReplyKeyboardMarkup

from kb import main_kb
from repo import SubscriptionNotificationsRepo
from table import get_today_schedule, lessons, tests_exams

menu_router = Router()


# Function /start
@menu_router.message(Command("start"))
async def start(message: types.Message):
    first_mess = (
        f"{message.from_user.first_name}, hi!\n\nI'm Tfik! I'm a bot that will "
        f"help you remember your lesson at the university! I will send you a message (reminder) 5 minutes "
        f"before your lesson!\n\nChoose, the action:"
    )
    await message.answer(text=first_mess, reply_markup=main_kb())


# Table with actions
@menu_router.message(Command("actions"))
async def cmd_menu_action(message: types.Message):
    await message.answer(text="How can I help you?", reply_markup=main_kb())


# Bot do actions when user write function /week_schedule
@menu_router.message(Command("week_schedule"))
@menu_router.message(F.text == "Week schedule 📋📌")
async def week_schedule_button(message: types.Message):
    await message.answer(text=lessons, reply_markup=main_kb())


@menu_router.message(Command("daily_schedule"))
@menu_router.message(F.text == "Daily schedule ‼️")
async def week_schedule_button(message: types.Message):
    await message.answer(get_today_schedule(), reply_markup=main_kb())


# func /exams
# Button exams
@menu_router.message(Command("exams"))
@menu_router.message(F.text == "Dates of tests and exams ☠️")
async def week_schedule_button(message: types.Message):
    await message.answer(text=tests_exams, reply_markup=main_kb())


# func /turn_on
@menu_router.message(F.text == "I want to get notifications 🔔")
async def subscription_notifications(msg: Message, repo: SubscriptionNotificationsRepo):
    await repo.add_subscription(msg.from_user.id)
    await msg.answer("Notifications are enabled 🔔", reply_markup=main_kb())


@menu_router.message(F.text == "Disable notifications 🔕")
async def subscription_notifications(msg: Message, repo: SubscriptionNotificationsRepo):
    await repo.remove_subscription(msg.from_user.id)
    await msg.answer("Notifications are disabled 🔕", reply_markup=main_kb())
