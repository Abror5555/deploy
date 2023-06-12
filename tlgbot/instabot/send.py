from aiogram import Bot, Dispatcher, executor, types
import logging
from insta import instadownloder
from aiogram.dispatcher.filters import Text


API_TOKEN = '5682607636:AAG9EMvAdSDHQ4v9ymcN_x6D8W8vai82rn4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom menga instagram linklarini yuboring")

@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message:types.Message):
    link = message.text
    data = instadownloder(link=link)
    if data == 'xato':
        await message.answer('Bu URL manzil orqali hechqanday narsa topaolmadik')
    else:
        if data['type']=='image':
            await message.answer_photo(photo=data['media'])
        elif data['type']=='video':
            await message.answer_video(video=data['media'])
        elif data['type']=='carousel':
            for i in data['media']:
                await message.answer_document(document=i)
        else:
            await message.answer('Bu URL manzil orqali hechqanday narsa topaolmadik')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
