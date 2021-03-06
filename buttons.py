from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="πΊπΏ Uzbek - π¬π§ English"),KeyboardButton(text="π¬π§ English - πΊπΏ Uzbek")],
        [KeyboardButton(text="πΊπΏ Uzbek - π·πΊ Russian"),KeyboardButton(text="π·πΊ Russian - πΊπΏ Uzbek")],
        [KeyboardButton(text="πΊπΏ Uzbek - π°πΏ Kazakh"), KeyboardButton(text="π°πΏ Kazakh - πΊπΏ Uzbek")],
        [KeyboardButton(text="πΊπΏ Uzbek - πΈπ¦ Arabic"), KeyboardButton(text="πΈπ¦ Arabic- πΊπΏ Uzbek")],
        [KeyboardButton(text="πΊπΏ Uzbek - πΉπ· Turkish"),KeyboardButton(text="πΉπ· Turkish - πΊπΏ Uzbek")],
        [KeyboardButton(text="πΊπΏ Uzbek - π°π· Korean"), KeyboardButton(text="π°π· Korean - πΊπΏ Uzbek")], 
        [KeyboardButton(text="πΊπΏ Uzbek - π¨π³ Chinese"),KeyboardButton(text="π¨π³ Chinese - πΊπΏ Uzbek")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

voice = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="π Audio tinglash", callback_data="voice"),
    ]
    ]
)