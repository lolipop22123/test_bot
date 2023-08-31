from aiogram import types
from config import db

def user_menu():
    mkp = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Просмотеть меню', callback_data='menu_user')
    mkp.add(btn1)
    return mkp


def admin_menu():
    mkp = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Добавить товар', callback_data='add_product')
    btn2 = types.InlineKeyboardButton('Отмена', callback_data='exit_admin')
    mkp.add(btn1, btn2)
    return mkp

# Клавиатура "Купить"
def buy_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Купить', callback_data='buy')
    btn2 = types.InlineKeyboardButton('⬅️', callback_data='prev')
    btn3 = types.InlineKeyboardButton('➡️', callback_data='next')
    keyboard.add(btn2, btn3).add(btn1)
    return keyboard

