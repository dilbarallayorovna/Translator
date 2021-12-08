import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN, text_to_speech
from buttons import menu, voice
from statest import Translate
from googletrans import Translator
from aiogram.types import CallbackQuery



logging.basicConfig(level=logging.INFO)



bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user}😊\n Men botman🤖\nMen sizga tarjimada yordam beraman🤝\nTarjima turini tanlang", reply_markup=menu)
    await Translate.lang.set()



@dp.message_handler(state=Translate.lang)
async def which_lang(message: types.Message, state: FSMContext):
    lang = message.text
    await state.update_data(
        {"lang": lang},
    )
    await message.answer(f"Tarjima qilishni istagan matningizni kiriting Mahrhamat")
    await Translate.next()
    # await Translate.trans.set()



@dp.message_handler(state=Translate.trans)
async def translate_text(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    lang = data.get("lang")
    tarjimon = Translator()
    if lang == "🇺🇿 Uzbek - 🇬🇧 English":
        tarjima = tarjimon.translate(text, dest="en")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="en")
    elif lang == "🇬🇧 English - 🇺🇿 Uzbek":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    elif lang == "🇺🇿 Uzbek - 🇷🇺 Russian":
        tarjima = tarjimon.translate(text, dest="ru")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="ru")
    elif lang == "🇷🇺 Russian - 🇺🇿 Uzbek":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    elif lang == "🇺🇿 Uzbek - 🇰🇿 Kazakh":
        tarjima = tarjimon.translate(text, dest="kz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="kz")
    elif lang == "🇰🇿 Kazakh - 🇺🇿 Uzbek":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    elif lang == "🇺🇿 Uzbek - 🇸🇦 Arabic":
        tarjima = tarjimon.translate(text, dest="ar")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="ar")
    elif lang == "🇸🇦 Arabic- 🇺🇿 Uzbbek":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    elif lang == "🇺🇿 Uzbek - 🇹🇷 Turkish":
        tarjima = tarjimon.translate(text, dest="tr")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    elif lang == "🇹🇷 Turkish - 🇺🇿 Uzbek":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    elif lang == "🇺🇿 Uzbek - 🇰🇷 Korean":
        tarjima = tarjimon.translate(text, dest="ko")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="ko")
    elif lang == "🇰🇷 Korean - 🇺🇿 Uzbek":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    elif lang == "🇺🇿 Uzbek - 🇨🇳 Chinese":
        tarjima = tarjimon.translate(text, dest="zh-cn")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="zh-CN")
    elif lang == "🇨🇳 Chinese - Uzbek":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    
    

    await Translate.audio.set()
    # await state.finish()



@dp.callback_query_handler(text='voice', state=Translate.audio)
async def send_audio(call: CallbackQuery):
    await call.message.answer_audio(open("audio.mp3", 'rb'), reply_markup=menu)
    os.remove("audio.mp3")
    await Translate.lang.set()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)