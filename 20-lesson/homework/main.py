#!/usr/bin/env python3
import os
from database import *

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
async def command_start(message):
    if message.text == '/start':
        await message.answer('Hello, this is weather bot.')
        await start_polling(message)
    elif message.text == '/help':
        await message.answer('To use the bot just type the name of the city that you want to get info about.')
    elif message.text == '/about':
        await message.answer('Bot was created for learning purposes and uses OpenWeather API.')
    elif message.text == '/history':
        await message.answer('')

async def start_polling(message):
    await Questions.src.set()
    await message.answer('Type in the name of the city to get forecast.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
