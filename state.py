from aiogram.dispatcher.filters.state import State, StatesGroup


class AddProductState(StatesGroup):
    name = State()        # Состояние для ввода названия товара
    description = State() # Состояние для ввода описания товара