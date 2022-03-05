import logging
from aiogram import Bot, Dispatcher, executor, types
from button import menu, user
from ibuttons import inline_menu, coursesMenu, fullstackMenu, about_django
TOKEN = "5167230229:AAHCIpLeFT2tAftPS_TDNgoXtMwfg8wwAmI"
from aiogram.dispatcher.filters import Text


# configure logging
logging.basicConfig(level=logging.INFO)


# Inintialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Start menu
@dp.message_handler(commands=["start"])
async def do_start(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Hello {user},\n✌️ Welcome to my simple bot,\n😇 You can choose any bootom and enjoy 🍦", reply_markup = menu)


# Help menu
@dp.message_handler(commands=["help"])
async def do_help(message: types.message):
    user = message.from_user.first_name
    await message.reply(f"Dear {user}, Welcome to my firs 🥇 bot,\nThis bot do some works 👨‍🏭,\nI always 🔄 update this bot.\nIf you need some help 🆘,\n@Amirkhan_Otaboyev is my telegram,\nYou are welcome 👍.")


# About user window
@dp.message_handler(text = "👥 About user")
async def about_user(message: types.Message):
    await message.answer("Choose a button ⬇️", reply_markup=user)


@dp.message_handler(text="🆔")
async def send_id(message: types.Message):
    uid = message.from_user.id
    await message.answer(f"Your 🆔: {uid}.")


@dp.message_handler(text="👤 Username")
async def send_uname(message: types.Message):
    uname = message.from_user.username
    await message.answer(f"Your username is @{uname}.")


@dp.message_handler(text="🥇 First name")
async def send_fname(message: types.Message):
    fname = message.from_user.first_name
    await message.answer(f"Your first name: {fname}.")


@dp.message_handler(text="🥈 Last name")
async def send_lname(message: types.Message):
    lname = message.from_user.last_name
    await message.answer(f"Your last name: {lname}.")


@dp.message_handler(text="🔙 Go to back")
async def go_back(message: types.Message):
    await message.answer("Main menu", reply_markup=menu)


@dp.message_handler(text="📚 Our courses")
async def get_ibutton(message:types.Message):
    await message.answer("Choose and take information about our courses ⬇️ ", reply_markup=inline_menu)


@dp.callback_query_handler(text="Python")
async def about_python(call: types.CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer_photo(
        photo="https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fc%2Fc3%2FPython-logo-notext.svg%2F640px-Python-logo-notext.svg.png&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPython_(programming_language)&tbnid=RmmUKq-2e8gHPM&vet=12ahUKEwiGsobTqqT2AhVy_bsIHfbRClUQMygAegUIARCkAQ..i&docid=3wRBXLyvECcz0M&w=640&h=640&q=python&ved=2ahUKEwiGsobTqqT2AhVy_bsIHfbRClUQMygAegUIARCkAQ",
        caption="You choose python tutorials.\nPython tutorials are divided into two section.\nFor more about each section\nplease choose one of the sections", reply_markup=coursesMenu
    )


@dp.callback_query_handler(text="PHP")
async def about_php(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.delete()
    await call.message.answer_photo(
        photo="https://www.google.com/imgres?imgurl=https%3A%2F%2Flaravelnews.imgix.net%2Fimages%2Fphplogo.jpg%3Fixlib%3Dphp-3.3.1&imgrefurl=https%3A%2F%2Flaravel-news.com%2Fannouncing-the-php-foundation&tbnid=szq3gjTgBlM3CM&vet=12ahUKEwjRy_uGq6T2AhUV0YUKHTluAyYQMygOegUIARDLAQ..i&docid=wiLrpciKQ-uj5M&w=2200&h=1100&q=php&ved=2ahUKEwjRy_uGq6T2AhUV0YUKHTluAyYQMygOegUIARDLAQ",
        caption="You choose PHP tutorials", reply_markup=fullstackMenu)


@dp.callback_query_handler(text="cancel")
async def iback(call: types.CallbackQuery):
    await call.message.answer("⬇ Choose a button", reply_markup=inline_menu)


@dp.callback_query_handler(text="Django")
async def get_django(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=about_django)


@dp.callback_query_handler(text="Go to coursesMenu")
async def go_cmenu(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=coursesMenu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)   # We use this for run our bot.