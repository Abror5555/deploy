
import logging
from buttons import button
from api import create_user, create_feedback
from states import FeedbackState
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5942989784:AAETIACj3STccRjpm5D_Pl2vdU9giKNbCa8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
   
    await message.reply("Hello, welcome to Abror Qo'shshiyev personal telegram bot", reply_markup=button)
    create_user(message.from_user.username, message.from_user.first_name, message.from_user.id)

@dp.message_handler(Text(startswith="Supply and demand"))
async def feedback_1(message: types.Message):
    await message.answer("Send message text.")
    await FeedbackState.body.set()


@dp.message_handler(state = FeedbackState.body)
async def feedback_2(message: types.Message, state:FSMContext):
    await message.answer(create_feedback(message.from_user.first_name, message.from_user.id, message.text))
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)