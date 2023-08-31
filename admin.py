from config import dp, db, admins
from aiogram.dispatcher import FSMContext
from aiogram import types
from markups import admin_menu, user_menu
from state import AddProductState

@dp.message_handler(commands='admin')
async def admin(m:types.Message):
    if m.from_user.id in admins:
        await m.answer(f'Вы перешли в админ панель!', reply_markup=admin_menu())
    else:
        await m.answer(f'Вы не администратор!', reply_markup=user_menu())
        
@dp.callback_query_handler(text = 'add_product')
async def add_product(call:types.CallbackQuery):
    await call.message.answer("Введите название товара:")
    
    await AddProductState.name.set()  # Устанавливаем состояние для ввода названия

@dp.message_handler(state=AddProductState.name)
async def process_name_step(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    
    await message.answer("Введите описание товара:")
    await AddProductState.description.set()  # Устанавливаем состояние для ввода описания

@dp.message_handler(state=AddProductState.description)
async def process_description_step(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        
        # Получаем название и описание из состояния
        name = data['name']
        description = data['description']
   
        db.add_product(name, description)

        await message.answer("Товар успешно добавлен в базу данных!",reply_markup=admin_menu())
    
    await state.finish()  # Завершаем состояние после добавления товара

#Выход с админ-панели  
@dp.callback_query_handler(text = 'exit_admin')
async def add_product(call:types.CallbackQuery, state:FSMContext):
    await call.message.answer(f'Вы в главном меню!',reply_markup=user_menu())

    await state.finish()



