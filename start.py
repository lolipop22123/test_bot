from config import dp, db
from aiogram import types
from markups import user_menu


@dp.message_handler(commands='start')
async def start_cmd(m:types.Message):
    await m.answer(f'Добро пожаловать {m.from_user.first_name}!', reply_markup=user_menu())

    db.add_user(m.from_user.id, m.from_user.username)

    