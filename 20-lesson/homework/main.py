#!/usr/bin/env python3
import os
from dotenv import *
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start', 'help', 'about', 'history'])
async def command_start(message: Message):
    if message.text == '/start':
        await message.answer('Здравствуйте, вас приветствует бот прогноза погоды')
        await start_questions(message)
    elif message.text == '/help':
        await message.answer('Если у вас возникли проблемы то пишите сюда')
    elif message.text == '/about':
        await message.answer('Очень сочувствую что вам приходится им пользоваться')
    elif message.text == '/history':
        await get_history(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
