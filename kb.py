from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def kb_for_start():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="Yes!",
        callback_data="actions"
    )

    return keyboard.adjust(1).as_markup(resize_keyboard=True, one_time_keyboard=True)


def main_kb():
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(
        KeyboardButton(text="Week schedule 📋📌"),
        KeyboardButton(text="Daily schedule ‼️"),
        KeyboardButton(text="Dates of tests and exams ☠️"),
        KeyboardButton(text="I want to get notifications 🔔"),
        KeyboardButton(text="Support the author 💵😊")
    )
    return keyboard.adjust(2, 1, 2).as_markup(resize_keyboard=True, one_time_keyboard=True)
