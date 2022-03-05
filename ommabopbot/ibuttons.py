from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Python web programming", callback_data="Python"), InlineKeyboardButton(text="PHP web programming", callback_data="PHP")],
        [InlineKeyboardButton(text="➕ Sign up", url="https://mohirdev.uz/courses/")]
    ]
)
about_django = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="What is Django tutorials", url="https://en.wikipedia.org/wiki/Django_(web_framework)"),
         InlineKeyboardButton(text="Go back", callback_data="Go to coursesMenu")]
    ]
)


coursesMenu = InlineKeyboardMarkup(row_width=2)

django = InlineKeyboardButton(text="Django web tutorrials", callback_data="Django")
coursesMenu.insert(django)

telegram = InlineKeyboardButton(text="Perfect telegram bot", callback_data="Telegram")
coursesMenu.insert(telegram)

back_button = InlineKeyboardButton(text="Back", callback_data="cancel")
coursesMenu.insert(back_button)



fullstackMenu = InlineKeyboardMarkup(row_width=2)

laravel = InlineKeyboardButton(text="Laravel web tutorials", callback_data="Laravel")
fullstackMenu.insert(laravel)

frontend = InlineKeyboardButton(text="Html, Css, Js", callback_data="Frontend")
fullstackMenu.insert(frontend)

back_button = InlineKeyboardButton(text="Back", callback_data="cancel")
fullstackMenu.insert(back_button)