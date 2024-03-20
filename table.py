from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import Message

from main import scheduler


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
        KeyboardButton(text="Week schedule 📋📌", callback_data="week"),
        KeyboardButton(text="Daily schedule ‼️", callback_data="daily"),
        KeyboardButton(text="Dates of tests and exams ☠️", callback_data="exams"),
        KeyboardButton(text="I want to get notifications 🔔", callback_data="turn_on"),
        KeyboardButton(text="Disable notifications 🔕", callback_data="turn_off"),
        KeyboardButton(text="Support the author 💵😊", callback_data="donate")
    )
    return keyboard.adjust(2, 1, 2, 1).as_markup(resize_keyboard=True, one_time_keyboard=True)


lessons = (
    f"UTOROK :\n\nPPI (cvicenie) ---> 09:10 - 10:40\nZSI (prednaska) ---> 10:50 - 12:20"
    f"\nProgramovanie (cvicenie) ---> 13:30 - 15:00"
    f"\n\nSTREDA :\n\nProgramovanie (prednaska) ---> 08:15 - 09:45\nMatematika 2 (prednaska) ---> 09:55- 11:25"
    f"\nFyzika 1 (prednaska) ---> 12:20 - 13:50\nPPI (prednaska) ---> 15:10 - 16:40"
    f"\n\nSTVRTOK :\n\nMatematika 2 (cvicenie) ---> 08:15 - 09:45\nFyzika 1 (cvicenie) ---> 09:55 - 11:25"
    f"\nZSI (cvicenie) ---> 13:30 - 15:00"
)

monday = (
    f"PONDELOK :"
    f"\n\nV tento deň nie sú žiadne lekcie ani cvičenia 🥳🎉"
)

tuesday = (
    f"UTOROK :"
    f"\n\nPPI (cvicenie) ---> 9:10 - 10:40\n\nZSI (prednaska) ---> 10:50 - 12:20"
    f"\n\nProgramovanie (cvicenie) ---> 13:30 - 15:00"
)

wednesday = (
    f"STREDA :"
    f"\n\nProgramovanie (prednaska) ---> 8:15 - 9:45\n\nMatematika 2 (prednaska) ---> 9:55- 11:25"
    f"\n\nFyzika 1 (prednaska) ---> 12:20 - 13:50\n\nPPI (prednaska) ---> 15:10 - 16:40"
)

thursday = (
    f"STVRTOK :"
    f"\n\nMatematika 2 (cvicenie) ---> 8:15 - 9:45\n\nFyzika 1 (cvicenie) ---> 9:55 - 11:25"
    f"\n\nZSI (cvicenie) ---> 13:30 - 15:00"
)

friday = (
    f"PIATOK :"
    f"\n\nV tento deň nie sú žiadne lekcie ani cvičenia 🥳🎉"
)

saturday = (
    f"SOBOTA :"
    f"\n\nV tento deň nie sú žiadne lekcie ani cvičenia 🥳🎉"
)

sunday = (
    f"NEDELA :"
    f"\n\nV tento deň nie sú žiadne lekcie ani cvičenia 🥳🎉"
)

tests_exams = (
    f"Tests and exams :"
    f"\n\n(7. týždeň)  ZSI  --->  Test"
    f"\n(9. týždeň)  PPI  --->  Pisomka (10 bodov)"
    f"\n(9. týždeň)  Jazyk 2  --->  Test (v piatok 12.04.2024)"
    f"\n(10. týždeň)  Fizika 1  --->  Pisomka (10 bodov)"
)


async def schedule_notifications(message):
    scheduler.remove_all_jobs()
    await add_notification_jobs(message)


async def add_notification_jobs(message: Message):
    print("Adding notification jobs...")
    # Tuesday
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have PPI (cvicenie) in 5 minutes !!!'), day_of_week='tue',
                      hour=9, minute=5)
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have ZSI (prednaska) in 5 minutes !!!'), day_of_week='tue',
                      hour=10, minute=45)
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have Programovanie (cvicenie) in 5 minutes !!!'),
                      day_of_week='tue',
                      hour=13, minute=25)
    # Wednesday
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have Programovanie (prednaska) in 5 minutes !!!'),
                      day_of_week='wed',
                      hour=8, minute=10)
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have Matematika 2 (prednaska) in 5 minutes !!!'),
                      day_of_week='wed',
                      hour=9, minute=50)
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have Fyzika 1 (prednaska) in 5 minutes !!!'),
                      day_of_week='wed',
                      hour=15, minute=34)  # hour=12, minute=15
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have PPI (prednaska) in 5 minutes !!!'),
                      day_of_week='wed',
                      hour=15, minute=5)
    # Thursday
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have Matematika 2 (cvicenie) in 5 minutes !!!'),
                      day_of_week='thu',
                      hour=8, minute=10)
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have Fyzika 1 (cvicenie) in 5 minutes !!!'),
                      day_of_week='thu',
                      hour=9, minute=50)
    scheduler.add_job(send_notification, 'cron',
                      args=(message, 'Hey ! You will have ZSI (cvicenie) in 5 minutes !!!'),
                      day_of_week='thu',
                      hour=13, minute=25)


async def stop_notifications():
    scheduler.pause()


async def send_notification(message: Message, text: str):
    try:
        await message.answer(text)
    except Exception as e:
        # Обработка ошибок при отправке уведомления
        print(f"Ошибка при отправке уведомления: {e}")
