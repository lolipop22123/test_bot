from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import DB

admins = [531852145]


bot = Bot(token='6117739616:AAG96QtKRYpxAgCsH_XoAwseDay9rpna9v4', parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

db = DB('testbot', 'postgres', '1111', 'localhost')