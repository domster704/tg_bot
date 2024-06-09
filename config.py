import json

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import async_sessionmaker

from db.db import engine

__env: dict = json.load(open("env.json"))

bot = Bot(token=__env["apiTG"],
          default=DefaultBotProperties(
              parse_mode=ParseMode.HTML
          ))

stateStorage = MemoryStorage()
dp = Dispatcher(storage=stateStorage)

__Session = async_sessionmaker(bind=engine)
session = __Session()
