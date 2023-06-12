import logging

from aiogram import Bot, Dispatcher, executor, types
from oxfordLoockup import getDifinitions
from googletrans import Translator
translator = Translator()

API_TOKEN = '5930224123:AAGOgAVxKpKolzPQIdDczoIHxtdUtMZUA_U'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom Speek English botiga xush kelibsiz")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Speek English bot \n Bu botga bron so'z kiritsangiz uni ma'nosini va tallafuzini sizga taqdim qildi \n Yoki 2 ta so'zdan ortiq matn kiritsangiz uni tarjima qiladi")



@dp.message_handler()
async def tarjima(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)

    else:
        pass
    if len=='en':
        word_id = message.text
    else:
        word_id = translator.translate(message.text, dest='en').text
    lookup = getDifinitions(word_id)
    if lookup:
        await message.reply(f"Word: {word_id} \nDifinitions:\n{lookup['definitions']}")
        if lookup.get('audio'):
            await message.reply_voice(lookup['audio'])
    else:
        await message.reply("Bunday so'z topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)