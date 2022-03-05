from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="👥 About user")],
        [KeyboardButton(text="📱 Send telephone number", request_contact=True)],
        [KeyboardButton(text="📍 Send location", request_location=True)],
        [KeyboardButton(text="📚 Our courses")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

user = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="🆔"), KeyboardButton(text="👤 Username")],
        [KeyboardButton(text="🥇 First name"), KeyboardButton(text="🥈 Last name")],
        [KeyboardButton(text="🔙 Go to back")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

