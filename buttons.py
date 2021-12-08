from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 Uzbek - 🇬🇧 English"),KeyboardButton(text="🇬🇧 English - 🇺🇿 Uzbek")],
        [KeyboardButton(text="🇺🇿 Uzbek - 🇷🇺 Russian"),KeyboardButton(text="🇷🇺 Russian - 🇺🇿 Uzbek")],
        [KeyboardButton(text="🇺🇿 Uzbek - 🇰🇿 Kazakh"), KeyboardButton(text="🇰🇿 Kazakh - 🇺🇿 Uzbek")],
        [KeyboardButton(text="🇺🇿 Uzbek - 🇸🇦 Arabic"), KeyboardButton(text="🇸🇦 Arabic- 🇺🇿 Uzbek")],
        [KeyboardButton(text="🇺🇿 Uzbek - 🇹🇷 Turkish"),KeyboardButton(text="🇹🇷 Turkish - 🇺🇿 Uzbek")],
        [KeyboardButton(text="🇺🇿 Uzbek - 🇰🇷 Korean"), KeyboardButton(text="🇰🇷 Korean - 🇺🇿 Uzbek")], 
        [KeyboardButton(text="🇺🇿 Uzbek - 🇨🇳 Chinese"),KeyboardButton(text="🇨🇳 Chinese - 🇺🇿 Uzbek")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

voice = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🎙 Audio tinglash", callback_data="voice"),
    ]
    ]
)