from config import dp, db
from aiogram.dispatcher import FSMContext
from aiogram import types
from markups import buy_keyboard

class ProductPagination:
    products = []  # Список товаров (заполняется из базы данных)
    current_index = 0  # Текущий индекс товара

    @classmethod
    async def show_product(cls, call: types.CallbackQuery, product_index: int):
        product = cls.products[product_index]
        is_purchased = db.is_product_purchased(call.from_user.id, product[0])  # Проверяем статус покупки товара
        status_text = "Куплено" if is_purchased else "Не куплено"

        await call.message.edit_text(
            f"Название: {product[1]}\nОписание: {product[2]}\nСтатус: {status_text}",
            reply_markup=buy_keyboard()
        )
        
    @classmethod
    async def next_product(cls, call: types.CallbackQuery):
        cls.current_index = (cls.current_index + 1) % len(cls.products)
        await cls.show_product(call, cls.current_index)
        
    @classmethod
    async def prev_product(cls, call: types.CallbackQuery):
        cls.current_index = (cls.current_index - 1) % len(cls.products)
        await cls.show_product(call, cls.current_index)



@dp.callback_query_handler(text = 'menu_user')
async def add_product(call:types.CallbackQuery):
    print('1')
    products = db.get_all_products()

    if products:
        ProductPagination.products = products  # Заполнение списка товаров
        await ProductPagination.show_product(call, ProductPagination.current_index)
    else:
        await call.message.answer("Нет доступных товаров")


@dp.callback_query_handler(text='next')
async def next_product(call: types.CallbackQuery):
    await ProductPagination.next_product(call)

@dp.callback_query_handler(text='prev')
async def prev_product(call: types.CallbackQuery):
    await ProductPagination.prev_product(call)

@dp.callback_query_handler(text='buy')
async def buy_product(call: types.CallbackQuery):
    user_id = call.from_user.id
    products = db.get_all_products()

    if products:
        ProductPagination.products = products  # Заполнение списка товаров
        product_id = ProductPagination.products[ProductPagination.current_index][0]
        product_name = ProductPagination.products[ProductPagination.current_index][1]

        if db.add_products_good(user_id, product_id):
            await call.answer(f"Товар '{product_name}' куплен и добавлен в БД!")
        else:
            await call.answer(f"Товар '{product_name}' уже куплен!")

    else:
        await call.message.answer("Нет доступных товаров")