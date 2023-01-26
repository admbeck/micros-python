#!/usr/bin/env python3
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def generate_categories(categories):
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = []
    for category in categories:
        btn = KeyboardButton(text=category[0])
        buttons.append(btn)
    markup.add(*buttons)
    return markup

def generate_download_button(image_id):
    markup = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text='Скачать изображение', callback_data=f'download_{image_id[0]}')
    button2 = InlineKeyboardButton(text='Скачать для мобильного', callback_data=f'mobile_{image_id[0]}')
    markup.row(button1, button2)
    return markup
