import os
from keyboards import generate_language
from configs import *
import sqlite3

from dotenv import *
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from googletrans import Translator

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Questions(StatesGroup):
    src = State()
    dst = State()
    text = State()



@dp.message_handler(commands=['start', 'help', 'about', 'history'])
async def command_start(message: Message):
    if message.text == '/start':
        await message.answer('Здравствуйте, вас приветствует бот переводчик')
        await start_questions(message)
    elif message.text == '/help':
        await message.answer('Если у вас возникли проблемы то пишите сюда')
    elif message.text == '/about':
        await message.answer('Данный бот был создан при поддержки micros')
    elif message.text == '/history':
        await get_history(message)

async def get_history(message):
    chat_id = message.chat.id
    database = sqlite3.connect('bot.db')
    cursor = database.cursor()

    cursor.execute('''
    SELECT src, dst, original_text, translate_text FROM history
    WHERE telegram_id = ?
    ''', (chat_id,))

    history = cursor.fetchall()
    history = history[::-1]
    for src, dst, original_text, translate_text in history[:10]:
        await bot.send_message(chat_id, f'''Вы переводили
С языка: {src} 
На язык: {dst}
Ваш текст: {original_text}
Бот перевел: {translate_text}
''')

    database.close()



async def start_questions(message: Message):
    await Questions.src.set()
    await message.answer('С какого языка перевести', reply_markup=generate_language())


@dp.message_handler(content_types=['text'], state=Questions.src)
async def confirm_src_text(message: Message, state: FSMContext):
    if message.text in ['/start', '/help', '/about', '/history']:
        await state.finish()
        await command_start(message)
    elif message.text in LANGUAGES.values():
        async with state.proxy() as data:
            data['src'] = message.text

        #await Questions.dst.set()
        await Questions.next()
        await message.answer(f'Вы выбрали {message.text}\nВыберите на какой язык перевести', reply_markup=generate_language())

@dp.message_handler(content_types=['text'], state=Questions.dst)
async def confirm_src_text(message: Message, state: FSMContext):
    if message.text in ['/start', '/help', '/about', '/history']:
        await state.finish()
        await command_start(message)
    elif message.text in LANGUAGES.values():
        async with state.proxy() as data:
            data['dst'] = message.text

        await Questions.next()
        await message.answer(f"Начинаем перевод с {data['src']}, на {data['dst']}\nВведите текст, который хотите перевести",
                             reply_markup=ReplyKeyboardRemove())


@dp.message_handler(content_types=['text'], state=Questions.text)
async def confirm_text_translate(message: Message, state: FSMContext):
    if message.text in ['/start', '/help', '/about', '/history']:
        await state.finish()
        await command_start(message)
    else:
        async with state.proxy() as data:
            data['text'] = message.text

        src = data['src']
        dst = data['dst']
        text = data['text']

        translator = Translator()
        trans_text = translator.translate(text=text, src=get_keys(src), dest=get_keys(dst))

        chat_id = message.chat.id
        database = sqlite3.connect('bot.db')
        cursor = database.cursor()
        cursor.execute('''
        INSERT INTO history(telegram_id, src, dst, original_text, translate_text ) 
        VALUES (?, ?, ?, ?, ?) 
        ''', (chat_id, src, dst, text, trans_text.text))
        database.commit()
        database.close()




        await message.answer(trans_text.text)
        await state.finish()
        await start_questions(message)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
