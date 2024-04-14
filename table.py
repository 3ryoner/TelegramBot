from datetime import datetime


def get_today_schedule():
    today = datetime.now().weekday()
    text = "Not found:("
    if today == 0:
        text = monday
    elif today == 1:
        text = tuesday
    elif today == 2:
        text = wednesday
    elif today == 3:
        text = thursday
    elif today == 4:
        text = friday
    elif today == 5:
        text = saturday
    elif today == 6:
        text = sunday
    return text


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
    f"\n\n(11. týždeň)  PPI  --->  Pisomka (10 bodov)"
    f"\n(11. týždeň)  Fizika 1  --->  Pisomka (20 bodov)"
    f"\n(14. týždeň) Matematika 2 ---> Započet (50 bodov)"
)

day_of_week_subjects = {
        'tue': [
            ("PPI (cvicenie)", dict(hour=9, minute=5)),
            ("ZSI (prednaska)", dict(hour=10, minute=45)),
            ("Programovanie (cvicenie)", dict(hour=13, minute=25)),
        ],
        'wed': [
            ("Programovanie (prednaska)", dict(hour=8, minute=10)),
            ("Matematika 2 (prednaska)", dict(hour=9, minute=50)),
            ("Fyzika I (prednáška)", dict(hour=12, minute=15)),
            ("PPI (prednaska)", dict(hour=15, minute=5)),
        ],
        'thu': [
            ("Matematika 2 (cvicenie)", dict(hour=8, minute=10)),
            ("Fyzika 1 (cvicenie)", dict(hour=9, minute=50)),
            ("ZSI (cvicenie)", dict(hour=13, minute=25)),
        ]
    }
